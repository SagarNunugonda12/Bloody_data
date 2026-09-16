import pandas as pd
df = pd.read_csv("../data/customers.csv")
name_series = df["Name"]
print(name_series)
print(type(name_series))
print(name_series.shape)
print(name_series.iloc[0])
print(name_series.iloc[-1])
print(type(df))
print("Number of rows:", df.shape[0])
print("Number of columns:",df.shape[1])

print("\n row access")
print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[2])
print(df.iloc[0:3])

print("Creating new column")
df["AgeNextYear"] = df["Age"] + 1
print(df[["Name", "Age", "AgeNextYear"]])

print("----------------")
df["CustomerType"] = ["Senior" if age >= 30 else "Young" for age in df["Age"]]