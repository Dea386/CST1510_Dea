# Week 6 — Extra Practice Projects

## Login Attempts Report (Cyber Security)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path(__file__).parent

df = pd.read_csv(folder / "login_attempts.csv")
print(df.head())
print(df.dtypes)
print(len(df))

print(df[df["failed"] >= 3])

failed_per_ip = df.groupby("ip")["failed"].sum()
print(failed_per_ip)

failed_sorted = failed_per_ip.sort_values(ascending=False)
print(failed_sorted)
print(failed_sorted[failed_sorted == failed_sorted.max()])  # shows ties too


df["suspicious"] = df["failed"].apply(lambda f: f >= 3)
print(df)

failed_per_ip.plot(kind="bar")
plt.title("Failed attempts per IP")
plt.xlabel("IP")
plt.ylabel("Failed attempts")
plt.tight_layout()
plt.savefig(folder / "failed_per_ip.png")
plt.close()


df[df["suspicious"] == True].to_csv(folder / "flagged_ips.csv", index=False)