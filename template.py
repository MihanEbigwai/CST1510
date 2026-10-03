"""
RECORD CHECK  -  my version
===========================

Name  :  Joe-Ebigwai Oronmihan David
Lane  :  AI
Date  :  25th September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

label = input("Label: ")
used = float(input("Used: "))
total = float(input("Total: "))


difference = total - used
percent = (used / total) * 100
ratio = used / difference


# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here
print(f"{'Items Used:':<18} {used:>10.2f}")
print(f"{'Total Items:':<18} {total:>10.2f}")
print(f"{'Unused Items:':<18} {difference:>+10.2f}")
print(f"{'Percentage Used:':<18} {percent:>10.2f}%")
print(
    f"{'Used:Unused Ratio:':<18} {ratio:>10.2f}"
)  # ratio makes it easier to represent data when comparing two quantities. In a case of 100 items received and 20 used, with the ratio we can see that for every 1 item that was used, 4 were not used. This makes it easier to understand the comparison rather than just a difference or percentage, making data presentation much more efficient.
print("=" * 34)
print(f"For every 1 item unused, {ratio:.2f} was used")
print("=" * 34)

# When the total is 0, it returns a ZeroDivisionError, an error that occurs when you try to divide with 0.
