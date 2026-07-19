"""
File: pandas_dataframe.py
Description: Creating and working with a Pandas DataFrame.
"""

import pandas as pd

student_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(student_data)

print("DataFrame:")
print(df)

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)
