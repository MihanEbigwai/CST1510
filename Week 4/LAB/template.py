"""
record check - my version
Name: Joe-Ebigwai Oronmihan David
Lane: AI
Date: 18th October 2026
"""

from pathlib import Path


def check_record(value, limit):
    """calculate difference, percentage and status"""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "WITHIN LIMIT"

    return difference, percent, status


def print_report(message):
    """print a report or message"""
    print(message)


def load_records(path):
    """read records from a text file"""
    records = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": int(value),
                "limit": int(limit)
            })

    return records


def save_results(path, results):
    """write record statuses to a file"""
    with open(path, "w", encoding="utf-8") as file:
        for label, status in results:
            file.write(f"{label},{status}\n")


# use the lab folder even if the script is run from somewhere else
lab_dir = Path(__file__).resolve().parent

records_path = lab_dir / "records.txt"
try:
    records = load_records(records_path)
except FileNotFoundError:
    print_report("Error: records.txt not found.")
    records = []

over_count = 0
results = []

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        f"\nDataset: {record['label']}\n"
        f"Rows loaded: {record['value']}\n"
        f"Rows expected: {record['limit']}\n"
        f"Difference: {difference}\n"
        f"Percentage: {percent:.2f}%\n"
        f"Status: {status}"
    )

    results.append((record["label"], status))

    if status == "OVER LIMIT":
        over_count += 1

print_report(f"\nTotal OVER LIMIT: {over_count}")

# keep the old report if the input file is missing
if records_path.is_file():
    save_results(lab_dir / "project_results.txt", results)
