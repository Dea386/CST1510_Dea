"""
RECORD CHECK  -  my version
===========================

Name  : Dea Kambo
Lane  : Cyber      
Date  : 4/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path 
folder = Path(__file__).parent

# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv(folder /"login_attempts.csv")


# 2. Add a "percent" column: (value / limit) * 100.

df["percent"] = (df["failed"] / df["attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# 3. Print the DataFrame.
print("Full DataFrame:")
print(df)

print("\nRows that are not OK:")
print(df[df["status"] != "OK"])

counts = (
    df.groupby("status")
    .size()
    .reindex(["OK", "WARNING", "OVER LIMIT"], fill_value=0)
)
print("\nCount per status:")
print(counts)

df.to_csv("login_attempts_checked.csv", index=False)

counts.plot(kind="bar", color=["green", "orange", "red"])
plt.title("Source IPs per status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(folder /"status_counts.png")
plt.close()





