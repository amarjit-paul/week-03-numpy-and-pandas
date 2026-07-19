"""
File: data_cleaning_and_aggregation.py
Description: Cleans, merges, and analyzes customer and purchase datasets.
"""

import pandas as pd

# Read datasets
customers = pd.read_csv("datasets/customer.csv")
items = pd.read_csv("datasets/item.csv")

# Merge datasets using Customer ID
merged_data = pd.merge(customers, items, on="Customer ID")

print("Merged Dataset (First 5 Rows):")
print(merged_data.head())

# Check for missing values
print("\nMissing Values:")
print(merged_data.isnull().sum())

# Remove rows with missing values
cleaned_data = merged_data.dropna()

print("\nShape Before Cleaning:", merged_data.shape)
print("Shape After Cleaning:", cleaned_data.shape)

# Average purchase amount
average_purchase = cleaned_data["Purchase Amount (USD)"].mean()
print("\nAverage Purchase Amount: $", round(average_purchase, 2))

# Average customer age
average_age = cleaned_data["Age"].mean()
print("Average Customer Age:", round(average_age, 2))

# Most popular category
print("\nMost Popular Category:")
print(cleaned_data["Category"].value_counts())

# Subscription status count
print("\nSubscription Status:")
print(cleaned_data["Subscription Status"].value_counts())

# Save cleaned dataset
cleaned_data.to_csv("outputs/cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully to outputs/cleaned_dataset.csv")