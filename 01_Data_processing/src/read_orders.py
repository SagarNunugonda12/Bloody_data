import csv
import os

# Define the file paths based on the structure
# Assumes you are running this from the project root directory
csv_file_path = os.path.join("data", "orders.csv")

# Initialize counters and accumulators
total_revenue = 0.0
total_orders = 0
 
print("--- Processing Orders ---")

try:
    # 1. Open the CSV file
    with open(csv_file_path, mode="r", newline="", encoding="utf-8") as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header row (OrderID, Customer, Product, Price)
        header = next(csv_reader)
        
        # 2. Read every record
        for row in csv_reader:
            # Unpack the row data
            order_id = row[0]
            customer = row[1]
            product = row[2]
            price = float(row[3])  # Convert price string to a number
            
            # 3. Print each order in a readable format
            print(f"Order #{order_id}: {customer} bought a {product} for ₹{price:,.2f}")
            
            # 4. Calculate total revenue
            total_revenue += price
            
            # 5. Count the total number of orders
            total_orders += 1

    # Print the final summary
    print("\n--- Summary Report ---")
    print(f"Total Orders Processed: {total_orders}")
    print(f"Total Revenue Generated: ₹{total_revenue:,.2f}")

except FileNotFoundError:
    print(f"Error: Could not find '{csv_file_path}'. Please ensure the file exists and you are running the script from the correct root folder.")