"""
File: numpy_arrays.py
Description: Creating and working with NumPy arrays.
"""

import numpy as np

# Creating a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("NumPy Array:")
print(numbers)

print("\nData Type:")
print(type(numbers))

print("\nArray Shape:")
print(numbers.shape)

print("\nArray Size:")
print(numbers.size)

print("\nData Type of Elements:")
print(numbers.dtype)