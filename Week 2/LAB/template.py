"""
record check  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  AI
Date  : 3rd October 2026

Run it:   python template.py
"""

over_limit_count = 0
warning_count = 0
ok_count = 0

while True:

    label = input("Dataset name (or quit to stop): ").strip()
    if label.lower() == "quit":
        break
    value = float(input("Rows loaded: "))
    limit = float(input("Rows expected: "))

    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1

    elif percent >= 90:
        status = "WARNING"
        warning_count += 1

    else:
        status = "OK"
        ok_count += 1

    print("=" * 34)
    print(f"RECORD CHECK FOR {label}")
    print(f"{'TOTAL VALUE RECORDED:':<30} {value:>6.2f}")
    print(f"{'TOTAL LIMIT (EXPECTED VALUE):':<30} {limit:>6.2f}")
    print(f"{'DIFFERENCE:':<30} {difference:>+6.2f}")
    print(f"{'PERCENTAGE USED:':<30} {percent:>6.2f} %")
    print(f"STATUS = {status}")
    print("=" * 34)

print("=" * 34)
print(f"Total number of records that came back as STATUS: OVER LIMIT = {over_limit_count}")
print(f"Total number of records that came back as STATUS: WARNING = {warning_count}")
print(f"Total number of records that came back as STATUS: OK = {ok_count}")
print("=" * 34)

# a limit of zero causes a division by zero error
