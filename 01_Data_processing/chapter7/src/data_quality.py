import csv
import os

# Define dynamic paths based on the script location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_PATH = os.path.join(BASE_DIR, "raw", "customers.csv")
CLEANED_DIR = os.path.join(BASE_DIR, "cleaned")
REJECTED_DIR = os.path.join(BASE_DIR, "rejected")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

CLEANED_PATH = os.path.join(CLEANED_DIR, "cleaned_customers.csv")
REJECTED_PATH = os.path.join(REJECTED_DIR, "rejected_customers.csv")
REPORT_PATH = os.path.join(REPORTS_DIR, "quality_report.txt")

def process_data_quality():
    # Ensure destination directories exist
    os.makedirs(CLEANED_DIR, exist_ok=True)
    os.makedirs(REJECTED_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)

    # 1. Read CSV Data
    rows = []
    headers = []
    with open(RAW_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)

    total_rows = len(rows)
    total_cols = len(headers)

    # 2. Profiling & Deduplication
    missing_values = {header: 0 for header in headers}
    seen_rows = set()
    unique_rows = []
    duplicate_count = 0

    for row in rows:
        # Check missing values per column
        for header, val in zip(headers, row):
            if not val.strip():
                missing_values[header] += 1

        # Check for exact duplicate rows
        row_tuple = tuple(row)
        if row_tuple in seen_rows:
            duplicate_count += 1
        else:
            seen_rows.add(row_tuple)
            unique_rows.append(row)

    # 3. Validation Rules
    valid_records = []
    rejected_records = []
    rule_failures = {
        "Age must be positive (> 0)": 0,
        "Email must contain '@'": 0,
        "Name cannot be empty": 0
    }

    for row in unique_rows:
        row_dict = dict(zip(headers, row))
        failures = []

        # Rule 1: Name cannot be empty
        if not row_dict["Name"].strip():
            failures.append("Name cannot be empty")

        # Rule 2: Age must be positive
        try:
            age = float(row_dict["Age"])
            if age <= 0:
                failures.append("Age must be positive (> 0)")
        except ValueError:
            failures.append("Age must be positive (> 0)")  # Handles missing or non-numeric age

        # Rule 3: Email must contain '@'
        if "@" not in row_dict["Email"]:
            failures.append("Email must contain '@'")

        # Record classification
        if failures:
            for failure in failures:
                rule_failures[failure] += 1
            # Append rejection reason to the rejected row for tracking
            rejected_records.append(row + ["; ".join(failures)])
        else:
            valid_records.append(row)

    # 4. Save Split Data
    with open(CLEANED_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(valid_records)

    with open(REJECTED_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers + ["RejectionReason"])
        writer.writerows(rejected_records)

    # 5. Generate quality_report.txt
    report_content = f"""===================================
      DATA QUALITY & PROFILING REPORT
===================================

--- 1. PROFILING SUMMARY ---
Total Records      : {total_rows}
Total Columns      : {total_cols}
Duplicate Records  : {duplicate_count}

Missing Values Per Column:
"""
    for col, count in missing_values.items():
        report_content += f"  - {col}: {count}\n"

    report_content += f"""
--- 2. PIPELINE VALIDATION ---
Valid Records Saved    : {len(valid_records)}
Rejected Records Saved : {len(rejected_records)}

Validation Failures By Rule:
"""
    for rule, count in rule_failures.items():
        report_content += f"  - {rule}: {count}\n"

    report_content += "===================================\n"

    with open(REPORT_PATH, mode="w", encoding="utf-8") as f:
        f.write(report_content)

    print("Data quality pipeline completed successfully!")
    print(f"Report generated at: {REPORT_PATH}\n")
    print(report_content)

if __name__ == "__main__":
    process_data_quality()