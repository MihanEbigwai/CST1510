
"""
RECORD CHECK - my version
Name: Joe-Ebigwai Oronmihan David
Lane: AI
Date: 18th October 2026
"""

def check_record(value, limit):
    """Calculate difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "WITHIN LIMIT"

    return difference, percent, status


def print_report(message):
    """Print a report or message."""
    print(message)


def load_records(path):
    """Read records from a text file."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            records.append({
                "label": label,
                "value": int(value),
                "limit": int(limit)
            })

    return records


def save_results(path, results):
    """Write record statuses to a file."""
    with open(path, "w") as file:
        for label, status in results:
            file.write(f"{label},{status}\n")


try:
    records = load_records("records.txt")
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

save_results("results.txt", results)
