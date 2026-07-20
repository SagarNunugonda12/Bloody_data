import csv
import json
import os

# Define relative paths based on your structure
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "input", "customers.csv")
json_path = os.path.join(base_dir, "input", "customers.json")

print("--- [FORMAT COMPARISON PIPELINE] --- \n")

# 1. READ AND PRINT CSV
print("▶ Reading Customers CSV:")
csv_records = 0
with open(csv_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"   Header: {header}")
    for row in reader:
        csv_records += 1
        print(f"   Row {csv_records}: {row}")

print("\n" + "="*40 + "\n")

# 2. READ AND PRINT JSON
print("▶ Reading Customers JSON:")
with open(json_path, mode="r", encoding="utf-8") as file:
    json_data = json.load(file)
    json_records = len(json_data)
    for index, record in enumerate(json_data, 1):
        print(f"   Object {index}: {record}")

print("\n" + "="*40 + "\n")

# 3. METRIC COMPARISONS (File Sizes and Records)
csv_size = os.path.getsize(csv_path)
json_size = os.path.getsize(json_path)

print("📊 SYSTEM METRICS SUMMARY:")
print(f"CSV File Size : {csv_size} bytes | Total Records: {csv_records}")
print(f"JSON File Size: {json_size} bytes | Total Records: {json_records}")
print(f"⚠️ JSON is approximately {((json_size - csv_size)/csv_size)*100:.1f}% larger than CSV due to repeating column tags!")