#find customers above age 25
import pandas as pd 
df = pd.read_csv("../data/customers.csv")
print("--- Task 1: Age > 28 ---")
print(df[df["Age"] > 25])
print("\n--- Task 2: City == Hyderabad ---")
print(df[df["City"] == "Hyderabad"])
print("\n--- Task 3: Age >= 30 AND City == Hyderabad ---")
print(df[(df["Age"] >= 30) & (df["City"] == "Hyderabad")])
print("\n--- Task 4: Customers in Hyd, Blr, Mumbai ---")
print(df[df["City"].isin(["Hyderabad", "Bangalore", "Mumbai"])])
print("\n--- Task 5: Age 25 through 30 ---")
print(df[df["Age"].between(25, 30)])