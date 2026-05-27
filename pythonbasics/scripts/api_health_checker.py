import requests
import sqlite3
import logging
from datetime import datetime
from pathlib import Path


logging.basicConfig(
    filename="api_health_checker_sqlite.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


DB_FILE = Path("health_checks.db")


urls = [
    "https://google.com",
    "https://github.com",
    "https://fake-domain-123456789.com"
]


def create_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status TEXT NOT NULL,
            status_code INTEGER,
            error TEXT,
            checked_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_result(result):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO health_checks (url, status, status_code, error, checked_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        result["url"],
        result["status"],
        result["status_code"],
        result["error"],
        result["checked_at"]
    ))

    connection.commit()
    connection.close()


def check_url(url):
    checked_at = str(datetime.now())

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            logging.info(f"{url} is UP")
            return {
                "url": url,
                "status": "UP",
                "status_code": response.status_code,
                "error": None,
                "checked_at": checked_at
            }

        logging.warning(f"{url} returned unexpected status code {response.status_code}")
        return {
            "url": url,
            "status": "UNHEALTHY",
            "status_code": response.status_code,
            "error": f"Unexpected status code: {response.status_code}",
            "checked_at": checked_at
        }

    except requests.exceptions.Timeout:
        logging.error(f"{url} timed out")
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "error": "Request timed out",
            "checked_at": checked_at
        }

    except requests.exceptions.RequestException as error:
        logging.error(f"{url} failed: {error}")
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "error": str(error),
            "checked_at": checked_at
        }


def show_latest_results():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT url, status, status_code, error, checked_at
        FROM health_checks
        ORDER BY id DESC
        LIMIT 5
    """)

    rows = cursor.fetchall()
    connection.close()

    print("\nLatest health check results:")

    for row in rows:
        url, status, status_code, error, checked_at = row
        print(f"{checked_at} | {url} | {status} | {status_code} | {error}")


def main():
    create_database()

    up_count = 0
    down_count = 0
    unhealthy_count = 0

    for url in urls:
        result = check_url(url)
        save_result(result)

        if result["status"] == "UP":
            up_count += 1
        elif result["status"] == "DOWN":
            down_count += 1
        else:
            unhealthy_count += 1

    print("API health check completed")
    print(f"UP: {up_count}")
    print(f"DOWN: {down_count}")
    print(f"UNHEALTHY: {unhealthy_count}")

    show_latest_results()


if __name__ == "__main__":
    main()