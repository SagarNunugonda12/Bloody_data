import pandas as pd

df = pd.read_csv("../data/customers.csv")

print(df)
print(type(df))
print(df.shape)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.columns)
print(df.dtypes)
print(df["Name"])
print(df[["Name","City"]])
