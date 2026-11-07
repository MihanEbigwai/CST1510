"""
record check - Student Survey Quality Checker

Name  : Joe-Ebigwai Oronmihan David
Lane  : AI
Date  : 07/11/2026

Run from the CST1510 folder: python "Week 7/LAB/template.py"
"""

# ============================ functions

def parse_line(raw_line):
    """turn a messy survey line into a dictionary with clean keys and numbers"""

    parts = raw_line.strip().lower().split(",")

    survey = parts[0].strip()
    if not survey:
        raise ValueError("Missing survey name")
    record = {"survey": survey}

    for part in parts[1:]:
        # split at the first equals sign so the rest stays in the value
        key, value = part.strip().split("=", 1)
        key = key.strip()
        value = value.strip()

        if key in ("rating", "age"):
            record[key] = int(value)

    if "rating" not in record or "age" not in record:
        raise ValueError("Missing rating or age")

    return record


def status_of(record):
    """flag survey records with a rating below 3"""

    if record["rating"] < 3:
        return "FLAGGED"
    else:
        return "OK"


# ================================ input

raw_records = []

with open("Week 7/LAB/survey_records.txt") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


# ===================== process + output

total_records = 0
flagged_records = 0
invalid_records = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)

        print(record, "-", status)

        total_records += 1

        if status == "FLAGGED":
            flagged_records += 1

    except ValueError as error:
        invalid_records += 1
        print("Invalid record:", raw_record.strip())
        print("Error:", error)


# ============================== summary

print(
    f"Summary: {total_records} valid records, "
    f"{flagged_records} flagged, {invalid_records} invalid."
)
