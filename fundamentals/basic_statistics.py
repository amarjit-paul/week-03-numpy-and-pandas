"""
File: basic_statistics.py
Description: Calculating basic statistics using Pandas.
"""

import pandas as pd

customers = pd.read_csv("datasets/customer.csv")

print("Average Age:")
print(customers["Age"].mean())

print("\nMaximum Age:")
print(customers["Age"].max())

print("\nMinimum Age:")
print(customers["Age"].min())

print("\nSummary Statistics:")
print(customers.describe())