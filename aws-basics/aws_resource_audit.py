import boto3
import json
from datetime import datetime
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError


REGION = "ap-south-1"
REPORT_FILE = "aws_resource_audit_report.json"


def mask_value(value, visible=4):
    text = str(value)
    if len(text) <= visible:
        return "[redacted]"
    return "[redacted]..." + text[-visible:]


def get_identity():
    sts = boto3.client("sts", region_name=REGION)
    identity = sts.get_caller_identity()

    return {
        "account": mask_value(identity.get("Account", "")),
        "arn": "[redacted]",
        "user_id": mask_value(identity.get("UserId", "")),
    }


def audit_ec2():
    ec2 = boto3.client("ec2", region_name=REGION)
    response = ec2.describe_instances()

    instances = []

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            name = "Unnamed"

            for tag in instance.get("Tags", []):
                if tag.get("Key") == "Name":
                    name = tag.get("Value", "Unnamed")

            instances.append({
                "name": name,
                "instance_id": mask_value(instance.get("InstanceId", "")),
                "state": instance.get("State", {}).get("Name", "unknown"),
                "instance_type": instance.get("InstanceType", "unknown"),
                "public_ip_present": "PublicIpAddress" in instance,
                "private_ip_present": "PrivateIpAddress" in instance,
            })

    return instances


def audit_s3():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    buckets = []

    for bucket in response.get("Buckets", []):
        buckets.append({
            "bucket_name": "[redacted]",
            "created": str(bucket.get("CreationDate")),
        })

    return buckets


def main():
    try:
        report = {
            "generated_at": str(datetime.now()),
            "region": REGION,
            "identity": get_identity(),
            "ec2_instances": audit_ec2(),
            "s3_buckets": audit_s3(),
        }

        with open(REPORT_FILE, "w") as file:
            json.dump(report, file, indent=4)

        print("AWS resource audit completed")
        print(f"EC2 instances found: {len(report['ec2_instances'])}")
        print(f"S3 buckets found: {len(report['s3_buckets'])}")
        print(f"Report written to {REPORT_FILE}")

    except NoCredentialsError:
        print("No AWS credentials found. Run aws configure or check your profile.")

    except ClientError as error:
        print("AWS client error:", error.response.get("Error", {}).get("Message"))

    except BotoCoreError as error:
        print("Boto3/Botocore error:", error)

    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()