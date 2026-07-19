"""
File: pandas_practice.py
Description: Practice reading and exploring a dataset.
"""

import pandas as pd

customers = pd.read_csv("datasets/customer.csv")

print("First 10 Rows:")
print(customers.head(10))

print("\nColumn Names:")
print(customers.columns)

print("\nDataset Shape:")
print(customers.shape)

print("\nMissing Values:")
print(customers.isnull().sum())