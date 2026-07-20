import csv
import os

# Define relative file paths based on the structure
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_path = os.path.join(base_dir, "raw", "customers.csv")
processed_path = os.path.join(base_dir, "processed", "cleaned_customers.csv")
report_path = os.path.join(base_dir, "reports", "etl_report.txt")

# Initialize tracking metrics
total_raw_rows = 0
missing_values_count = 0
duplicates_removed = 0

seen_records = set()
cleaned_data = []

print("--- Starting ETL Pipeline ---")

# 1. READ THE RAW FILE
try:
    with open(raw_path, mode="r", newline="", encoding="utf-8") as file:
        # Check if file is empty
        if os.stat(raw_path).st_size == 0:
            print(f"[Error] The file at {raw_path} is completely empty!")
            exit()
            
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Extract header
        
        for row in csv_reader:
            total_raw_rows += 1
            
            # 2. DETECT MISSING VALUES
            has_missing = any(not item.strip() for item in row)
            if has_missing:
                missing_values_count += 1
            
            # 4. REPLACE MISSING AGES WITH "Unknown"
            if len(row) > 3 and not row[3].strip():
                row[3] = "Unknown"
                
            row_tuple = tuple(row)
            
            # 3. DETECT & REMOVE DUPLICATE ROWS
            if row_tuple in seen_records:
                duplicates_removed += 1
            else:
                seen_records.add(row_tuple)
                cleaned_data.append(row)

    # 5. SAVE CLEANED DATA TO PROCESSED FOLDER
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    with open(processed_path, mode="w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(cleaned_data)
    print(f"[Success] Cleaned data saved to: {processed_path}")

    # 6. GENERATE REPORT IN REPORTS FOLDER
    total_processed_rows = len(cleaned_data)
    
    report_content = f"""ETL PIPELINE SUMMARY REPORT
===========================
Total rows in the raw file:    {total_raw_rows}
Total rows after cleaning:     {total_processed_rows}
Number of duplicates removed:  {duplicates_removed}
Number of missing values found: {missing_values_count}
"""

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, mode="w", encoding="utf-8") as file:
        file.write(report_content)
    print(f"[Success] Report generated at: {report_path}")

except FileNotFoundError:
    print(f"[Error] Could not find raw file at {raw_path}. Verify your folder structures.")