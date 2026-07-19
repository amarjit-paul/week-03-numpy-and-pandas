"""
File: reading_csv.py
Description: Reading a CSV file using Pandas.
"""

import pandas as pd

customers = pd.read_csv("datasets/customer.csv")

print("First 5 Rows:")
print(customers.head())

print("\nLast 5 Rows:")
print(customers.tail())