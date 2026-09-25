"""
RECORD CHECK  -  my version
===========================

Name  : Dea Kambo
Lane  :  Cyber     
Date  :23/09/2026

Run it:   python template.py

"""


# ==================================================================== INPUT
# 1. Ask the user for your three values.

ip_source = input("enter your IP Source ")    
failed_login = float(input("Enter number of failed logins "))
total_attempts = float(input("Enter toal attempts "))

# 2. Work out what you were NOT given. 
attempt_left = total_attempts - failed_login
percent_failed_attempts = (failed_login/total_attempts) * 100

# total number of active users
user_count = float(input("enter number of users "))
attempts_per_user = total_attempts/ user_count



print("=" * 25)
print("RECORD CHECK - srv-01")
print("=" * 25)
print("Failed Attempts", ":", failed_login )
print("Total Attempts",":", total_attempts)
print(f"Attempts Left : {attempt_left:<+8.2f}" )
print(f"Percentage of failed attempts, : {percent_failed_attempts:.2f} %")
print("Attempts Per user",attempts_per_user)
print("=" * 25)





