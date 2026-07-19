"""
File: indexing_slicing.py
Description: Indexing and slicing NumPy arrays.
"""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original Array:")
print(numbers)

print("\nFirst Element:")
print(numbers[0])

print("\nLast Element:")
print(numbers[-1])

print("\nElements from Index 2 to 5:")
print(numbers[2:5])

print("\nFirst Four Elements:")
print(numbers[:4])

print("\nElements from Index 3 onwards:")
print(numbers[3:])