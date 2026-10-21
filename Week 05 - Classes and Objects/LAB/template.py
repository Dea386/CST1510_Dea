"""
RECORD CHECK  -  my version
===========================

Name  : Dea Kambo
Lane  :   Cyber      
Date  : 21/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
class Record:

  def __init__(self, label, value, limit):
    self.label = label
    self.value = value
    self.limit = limit

  def status(self):
    if self.limit == 0:
      return "OK"
    percentage = (self.value / self.limit) * 100
    if percentage >= 100:
      return "OVER LIMIT"
    elif percentage >= 90:
      return "WARNING"
    else:
      return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
def load_records(path):
  records_list = []
  with open(path, "r") as file:
    for line in file:
      line = line.strip()
      if line:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) == 3:
          label = parts[0]  
          value = float(parts[1])  
          limit = float(parts[2])  
          records_list.append(Record(label, value, limit))
  return records_list
records = load_records("Week 05 - Classes and Objects/LAB/records_sample.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
over_limit_count = 0

for record in records:
  print()
  print("=" * 34)
  print(f"  SECURITY CHECK  -  {record.label}")
  print("=" * 34)

  current_status = record.status()

  print(f"Failed Logins   : {record.value}")
  print(f"Attempt Limit   : {record.limit}")
  print(f"Threat Status   : {current_status}")

  if current_status == "OVER LIMIT":
    over_limit_count += 1

  print("=" * 34)

print(f"\nTotal IPs OVER LIMIT: {over_limit_count}")


