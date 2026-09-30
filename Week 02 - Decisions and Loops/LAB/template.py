"""
RECORD CHECK  -  my version
===========================

Name  : Dea Kambo
Lane  : Cyber /     
Date  : 30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT

# 1. Ask the user for your three values.
overlimit = 0 

while True:
    ip_source = input("enter your IP Source or write 'quit' to stop ")
    if ip_source == "quit":
        break
    failed_login = float(input("Enter number of failed logins "))
    total_attempts = float(input("Enter toal attempts "))


# 2. Work out the difference and the percentage.       [Typical and above]
    difference = total_attempts - failed_login
    percent = (failed_login / total_attempts) * 100

    if percent > 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        overlimit += 1

# 4. Print the report.
    print("=" * 25)
    print(f"RECORD CHECK - {ip_source}")
    print("=" * 25)
    print("Failed Attempts", ":", failed_login)
    print("Total Attempts", ":", total_attempts)
    print(f"Free: {difference:<+8.2f}")
    print(f"Percentage: {percent:.2f} %")
    print("Status:", status)
    print("=" * 25)



#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {ip_source}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
