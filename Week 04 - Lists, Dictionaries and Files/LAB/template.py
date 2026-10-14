"""
RECORD CHECK  -  my version
===========================

Name  : Dea
Lane  :  cyber   
Date  :14/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def check_record(failed_logins, total_attempts):
    difference = failed_logins - total_attempts
    percent = (failed_logins / total_attempts) * 100 if total_attempts > 0 else 0
    if failed_logins > total_attempts:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status


def print_report(source_ip, failed_logins, total_attempts, difference, percent, status):
    print(
        f"{source_ip}: failed_logins={failed_logins}, total_attempts={total_attempts}, difference={difference}, percentage={percent:.1f}%, status={status}"
    )


def load_records(path):
    records = []
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                record = {
                    "source_ip": parts[0],
                    "failed_logins": int(parts[1]),
                    "total_attempts": int(parts[2]),
                }
                records.append(record)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found. Starting with empty list.")
    return records


data_file_path = "data.txt"
records = load_records(data_file_path)

over_limit_count = 0
results_data = []

# Loop through each record properly indented
for record in records:
    difference, percent, status = check_record(
        record["failed_logins"], record["total_attempts"]
    )

    if status == "OVER LIMIT":
        over_limit_count += 1

    # Print the report for each record
    print_report(
        record["source_ip"],
        record["failed_logins"],
        record["total_attempts"],
        difference,
        percent,
        status,
    )

    # Use the correct plural variable name 'results_data'
    results_data.append(f"{record['source_ip']},{status}\n")

print(f"\nTotal records OVER LIMIT: {over_limit_count}")

results_file_path = "results.txt"
try:
    with open(results_file_path, "w") as results_file:
        results_file.writelines(results_data)
    print(f"Results successfully written to {results_file_path}")
except IOError:
    print(f"Error: Could not write to file '{results_file_path}'")