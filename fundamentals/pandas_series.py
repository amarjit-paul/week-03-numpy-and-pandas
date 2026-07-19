"""
File: pandas_series.py
Description: Creating and using a Pandas Series.
"""

import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)

print("\nAverage Marks:")
print(marks.mean())

print("\nMaximum Marks:")
print(marks.max())

print("\nMinimum Marks:")
print(marks.min())