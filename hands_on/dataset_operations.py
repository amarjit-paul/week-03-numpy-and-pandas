"""
File: dataset_operations.py
Description: Perform filtering and grouping operations.
"""

import pandas as pd

customers = pd.read_csv("datasets/customer.csv")

# Customers older than 30
older_customers = customers[customers["Age"] > 30]

print("Customers Older Than 30:")
print(older_customers.head())

print("\nAverage Age by Gender:")
print(customers.groupby("Gender")["Age"].mean())

print("\nCustomers by Location:")
print(customers["Location"].value_counts())