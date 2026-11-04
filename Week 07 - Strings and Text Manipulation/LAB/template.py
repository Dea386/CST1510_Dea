"""
RECORD CHECK  -  my version
===========================

Name  : Dea Kambo 
Lane  :  Cyber      
Date  : 4/11/26


Run it:   python template.py

"""

# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line 

def parse_line(raw_line):
    line = raw_line.strip().lower()
    record = {}
    for piece in line.split(","):
        key, value = piece.split("=")
        record[key.strip()] = value.strip()
    record["attempts"] = int(record["attempts"])   # raises ValueError if not a number
    return record


def status_of(record, limit=10):
    if record["result"] == "failed" and record["attempts"] >= limit:
        return "FLAGGED"
    return "OK"

# 2. Your raw, messy records - at least 5, deliberately varied in spacing

raw_records = [
    "  SRC=10.0.0.5 , ATTEMPTS=12 , RESULT=FAILED  \n",
    "src=192.168.1.20,attempts=3,result=failed\n",
    "SRC=172.16.0.9,   Attempts=25,Result=Failed\n",
    "  src = 10.0.0.77 ,ATTEMPTS = 1 , RESULT = SUCCESS\n",
    "SRC=203.0.113.4,ATTEMPTS=10,RESULT=FAILED\n",
    "SRC=10.0.0.8,ATTEMPTS=many,RESULT=FAILED\n",    # will not convert to a number
]

# Excellent: save the raw lines to a file, then load them back from it
with open("raw_records.txt", "w") as f:
    f.writelines(raw_records)

with open("raw_records.txt") as f:
    raw_records = f.readlines()


# 3. Parse and report on every record.
total = 0
flagged = 0
unparsed = 0

for raw_record in raw_records:
    if not raw_record.strip():          # skip blank lines
        continue
    total += 1
    try:
        record = parse_line(raw_record)
    except ValueError as error:
        unparsed += 1
        print("Could not parse:", raw_record.strip(), "->", error)
        continue

    status = status_of(record)
    if status == "FLAGGED":
        flagged += 1
    print(record, status)

print(f"Summary: {total} records, {flagged} flagged, {unparsed} could not be parsed")
