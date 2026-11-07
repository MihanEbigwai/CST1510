"""
record check  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  IT
Date  : 11th October 2026

Run it:   python template.py
"""

# =================================================================== functions
# 1. define the functions. Each function does one job

def status_of(percent):
    """use the percentage to pick a status"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """return the difference and percentage used"""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """show the numbers and status for one record"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:10.2f}")
    print(f"  Total       : {limit:10.2f}")
    print(f"  Free        : {-difference:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def print_summary(count):
    """print the final number of over-limit records"""
    print(f"\nRecords OVER LIMIT: {count}")


# ==================================================================== input
# 2. ask for the three values. Repeat until the label is "quit"

over_limit_count = 0

while True:
    label = input("Hostname (or quit to stop): ").strip()

    if label.lower() == "quit":
        break

    value = float(input("GB used: "))
    limit = float(input("GB total: "))

    # ================================================================== process
    # 3. calculate the difference, percentage, and status

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # =================================================================== output
    # 4. print the report using print_report()

    print_report(label, value, limit, difference, percent, status)

# print the count once, after the loop ends
print_summary(over_limit_count)


# ==========================================================================
# 5. before you finish:
#
# [checked] Run it three times with different numbers
# [checked] Run it with a total of 0 and note the error (do not fix it yet)
# error: ZeroDivisionError: division by zero, in check()
# [checked] Check every function does one job
