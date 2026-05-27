import requests
import json
import logging
from datetime import datetime
from pathlib import Path


logging.basicConfig(
    filename="api_health_checker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


urls = [
    "https://google.com",
    "https://github.com",
    "https://fake-domain-123456789.com"
]


report_file = Path("api_health_report.json")


def check_url(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            logging.info(f"{url} is UP with status {response.status_code}")
            return {
                "url": url,
                "status": "UP",
                "status_code": response.status_code,
                "error": None
            }

        logging.warning(f"{url} returned status {response.status_code}")
        return {
            "url": url,
            "status": "UNHEALTHY",
            "status_code": response.status_code,
            "error": f"Unexpected status code: {response.status_code}"
        }

    except requests.exceptions.Timeout:
        logging.error(f"{url} timed out")
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "error": "Request timed out"
        }

    except requests.exceptions.RequestException as error:
        logging.error(f"{url} failed: {error}")
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "error": str(error)
        }


results = []

for url in urls:
    result = check_url(url)
    results.append(result)


summary = {
    "generated_at": str(datetime.now()),
    "total_urls": len(results),
    "up_count": sum(1 for item in results if item["status"] == "UP"),
    "down_count": sum(1 for item in results if item["status"] == "DOWN"),
    "unhealthy_count": sum(1 for item in results if item["status"] == "UNHEALTHY"),
    "results": results
}


with open(report_file, "w") as file:
    json.dump(summary, file, indent=4)


print("API health check completed")
print(f"Total URLs: {summary['total_urls']}")
print(f"UP: {summary['up_count']}")
print(f"DOWN: {summary['down_count']}")
print(f"UNHEALTHY: {summary['unhealthy_count']}")
print(f"Report saved to {report_file}")