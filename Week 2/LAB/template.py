"""
RECORD CHECK  -  my version
===========================

Name  : Joe-Ebigwai Oronmihan David
Lane  :  AI 
Date  : 3rd October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

overLimitCounter = 0
warningCounter = 0
okCounter = 0

while True:

# ==================================================================== INPUT

    label = input("Enter the dataset name:")  
    if label == "quit":
        break
    value = float(input("Enter total loaded(value recorded): "))     
    limit = float(input("Enter the total expected(limit): "))     

    

    difference = limit - value   
    percent = (value/limit)*100       

    if percent >= 100:
        status = "OVER LIMIT!!!"
        overLimitCounter+=1

    elif percent >= 90:
        status = "WARNING!"
        warningCounter+=1

    else:
        status = "OK"
        okCounter+=1



# =================================================================== OUTPUT
    print("="*34)
    print(f"RECORD CHECK FOR {label}")
    print(f"{"TOTAL VALUE RECORDED:":<30} {value:>6.2f}")
    print(f"{"TOTAL LIMIT(EXPECTED VALUE):":<30} {limit:>6.2f}")
    print(f"{"DIFFERENCE:":<30} {difference:>+6.2f}")
    print(f"{"PERCENTAGE USED:":<30} {percent:>6.2f} %")
    print(f"STATUS = {status}")  # replace with your if / else (or if / elif / else)
    print("="*34)


# your report lines go here
print("="*34)
print(f"Total number of records that came back as STATUS: OVER LIMIT = {overLimitCounter}")
print(f"Total number of records that came back as STATUS: WARNING = {warningCounter}")
print(f"Total number of records that came back as STATUS: OK = {okCounter}")
print("="*34)

#Encountered ZeroDivisionError when total = 0

