"""
record check  -  my version
===========================

Name  :  Joe-Ebigwai Oronmihan David
Lane  :  AI
Date  :  25th September 2026

Run it:   python template.py
"""

label = input("Dataset Label: ")
used = float(input("Total Used: "))
total = float(input("Total: "))


difference = total - used
percent = (used / total) * 100
rows_over_target = max(used - total, 0)


# =================================================================== output

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"{'Items Used:':<18} {used:>10.2f}")
print(f"{'Total Items:':<18} {total:>10.2f}")
print(f"{'Unused Items:':<18} {difference:>+10.2f}")
print(f"{'Percentage Used:':<18} {percent:>10.2f}%")
# extra rows can be a clue that data was loaded twice
print(f"{'Rows Over Target:':<18} {rows_over_target:>10.2f}")
print("=" * 34)

# a total of zero causes a division by zero error
