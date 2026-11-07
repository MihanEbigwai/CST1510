"""
record check  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  AI
Date  : 25th October 2026

Run it:   python template.py
"""

from pathlib import Path

class Record:
    """a dataset with a loaded row count and a target"""

    def __init__(self, label, value, limit):
        """store the record's label, value and limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """return the record's status based on its limit"""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== records
def load_records(path):
    """read records from a file and return Record objects"""
    records = []

    with open(path, encoding="utf-8") as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            value = float(value)
            limit = float(limit)

            records.append(Record(label, value, limit))

    return records


# ==================================================================== output
file_path = Path(__file__).resolve().parent / "records.txt"
records = load_records(file_path)

over_limit_count = 0

for record in records:
    status = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print(f"    Value  -  {record.value}")
    print(f"    Limit  -  {record.limit}")
    print(f"    Status -  {status}")
    print("=" * 34)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Total Records OVER LIMIT - {over_limit_count}")
