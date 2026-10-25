"""
RECORD CHECK  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  AI 
Date  : 25th October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.


class Record:
    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the record's status based on its limit."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    


# ==================================================================== RECORDS
def load_records(path):
    """Read records from a file and return Record objects."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            value = float(value)
            limit = float(limit)

            records.append(Record(label, value, limit))

    return records


# ==================================================================== OUTPUT
from pathlib import Path

file_path = Path(__file__).resolve().parent / "records.txt"
records = load_records(file_path)

over_limit_count = 0

for record in records:

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print(f"    Value  -  {record.value}")
    print(f"    Limit  -  {record.limit}")
    print(f"    Status -  {record.status()}")
    print("=" * 34)

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Total Records OVER LIMIT - {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
