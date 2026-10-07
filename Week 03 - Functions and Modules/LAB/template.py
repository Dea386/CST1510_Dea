"""
RECORD CHECK  -  my version
===========================

Name  : Dea
Lane  :   Cyber      
Date  : 7/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    if percent >= 100:
        return "OVERLIMIT"
    elif percent >= 90:
        return "WARNING"
    else: 
        return "OK"

def check(failed_logins,total_attempts):
    difference = failed_logins - total_attempts
    percent = (failed_logins / total_attempts)
    return difference, percent 

def print_report(source_ip,failed_logins,total_attempts, difference, percent , status):
    print("=" * 25)
    print(f"Failed Logins: {failed_logins:>12.2f}")
    print(f"Total Attempts: {total_attempts:>12.2f}")
    print(f"Difference: {difference:>12.2f}")
    print(f"Percentage: {percent:>11.2f}%")
    print(f"Status: {status>12}")
    print("=" * 25)

over_limit_count = 0

while True:
   source_ip = input("Enter Source_IP or 'quit' to stop ")
   if source_ip.lower() == "quit":
       break

   failed_logins = float(input("Enter Failed Logins "))
   total_attempts = float(input("Enter Total Attempts"))

difference , percent = check(failed_logins,total_attempts)
status = status = status_of(percent)
if status == "OVERLIMIT":
    over_limit_count += 1

print_report(source_ip,failed_logins,total_attempts,difference,percent,status)
print(f"/nTotal items OVERLIMIT: {over_limit_count}")



