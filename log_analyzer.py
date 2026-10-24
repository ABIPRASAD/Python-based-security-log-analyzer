
import csv
import json
from pathlib import Path


def analyze_log_file(filename):
    failed_count = 0
    failed_users = []
    events = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if "FAILED" in line:
                failed_count += 1

                username = line.split()[-1]
                failed_users.append(username)

                events.append({
                    "event": "Failed login",
                    "username": username,
                    "log_entry": line
                })

    return failed_count, failed_users, events


def export_reports(events):
    # Export to CSV
    with open(
        "security_report.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["event", "username", "log_entry"]
        )
        writer.writeheader()
        writer.writerows(events)

    # Export to JSON
    with open(
        "security_report.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(events, file, indent=4)


def main():
    filename = Path("security.log")

    try:
        failed_count, failed_users, events = analyze_log_file(filename)

        print("Total failed login attempts:", failed_count)
        print("Users in failed login events:", failed_users)

        export_reports(events)

        print("CSV report saved: security_report.csv")
        print("JSON report saved: security_report.json")

    except FileNotFoundError:
        print("Error: security.log was not found.")

    except (OSError, IndexError) as error:
        print("Unable to analyze the log file:", error)


if __name__ == "__main__":
    main()

