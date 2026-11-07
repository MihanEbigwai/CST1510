"""
record check  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  AI 
Date  : Friday 6th November 2026

Run it:   python template.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

lab_dir = Path(__file__).resolve().parent
# use the same dataset records from weeks 4 and 5
records = pd.read_csv(lab_dir / "dataset_records.csv")
records["percent"] = (records["rows_loaded"] / records["rows_expected"]) * 100
records["status"] = records["percent"].apply(
    lambda percent: "OVER LIMIT" if percent >= 100 else "WARNING" if percent >= 90 else "OK"
)

print("Records that need attention")
print(records[records["status"] != "OK"].to_string(index=False))

# count all statuses here, including OK
counts = records.groupby("status").size()
print("\nRecords per status")
print(counts.to_string())

records.to_csv(lab_dir / "mini_project_report.csv", index=False)
ax = counts.plot(kind="barh", title="Record Check: Counts by Status")
ax.set_xlabel("Number of records")
ax.set_ylabel("Status")
plt.tight_layout()
plt.savefig(lab_dir / "mini_project_status_counts.png")
plt.close()
