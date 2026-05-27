import pandas as pd
data = pd.read_csv("sample_data/marketing_data.csv")

print("CSV loaded successfully.")
print()
print("First 5 rows:")
print(data.head())
print()
print("Columns:")
print(data.columns.tolist())
print()
print("Total revenue:", data["revenue"].sum())
print("Total spend:", data["spend"].sum())
