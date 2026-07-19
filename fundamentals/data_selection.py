"""
File: data_selection.py
Description: Selecting rows and columns from a DataFrame.
"""

import pandas as pd

customers = pd.read_csv("datasets/customer.csv")

print("Customer ID and Age:")
print(customers[["Customer ID", "Age"]].head())

print("\nCustomers Older Than 30:")
print(customers[customers["Age"] > 30].head())
