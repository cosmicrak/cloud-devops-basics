from pathlib import Path
import argparse
import json
import logging
from datetime import datetime


logging.basicConfig(
    filename="argparse_log_parser.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Parse a log file and count matching log levels."
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )

    parser.add_argument(
        "--level",
        default="ERROR",
        help="Log level to search for, example: INFO, WARNING, ERROR"
    )

    return parser.parse_args()


def parse_log_file(log_file_path, level):
    log_file = Path(log_file_path)

    if not log_file.exists():
        logging.error(f"File not found: {log_file}")
        return {
            "status": "failed",
            "error": f"File not found: {log_file}",
            "matched_count": 0,
            "matched_lines": []
        }

    matched_count = 0
    matched_lines = []

    with open(log_file, "r") as file:
        for line in file:
            clean_line = line.strip()

            if level.upper() in clean_line.upper():
                matched_count += 1
                matched_lines.append(clean_line)

    logging.info(f"Parsed {log_file} for level {level}. Matches: {matched_count}")

    return {
        "status": "success",
        "file": str(log_file),
        "level": level.upper(),
        "matched_count": matched_count,
        "matched_lines": matched_lines
    }


def main():
    args = parse_arguments()

    result = parse_log_file(args.file, args.level)

    report = {
        "generated_at": str(datetime.now()),
        "result": result
    }

    with open("argparse_log_report.json", "w") as output:
        json.dump(report, output, indent=4)

    print("Log parsing completed")
    print(f"Status: {result['status']}")
    print(f"Matched count: {result['matched_count']}")
    print("Report saved to argparse_log_report.json")


if __name__ == "__main__":
    main()