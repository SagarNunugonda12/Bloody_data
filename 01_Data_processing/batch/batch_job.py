import csv
import os

# Locate the file dynamically
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "orders.csv")

print("--- [BATCH] Triggering Scheduled Daily Job ---")

try:
    total_revenue = 0.0
    
    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header
        
        for row in csv_reader:
            total_revenue += float(row[2])
            
    print(f"[BATCH SUCCESS] Final Total Revenue Calculated: ₹{total_revenue:,.2f}")
    print("--- [BATCH] Job Completed. Exiting Resources. ---")

except FileNotFoundError:
    print(f"Error: Missing file at {csv_path}")