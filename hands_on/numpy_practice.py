"""
File: numpy_practice.py
Description: Practice basic NumPy operations.
"""

import numpy as np

numbers = np.array([12, 25, 37, 48, 59])

print("Original Array:")
print(numbers)

print("\nMean:")
print(np.mean(numbers))

print("\nMaximum:")
print(np.max(numbers))

print("\nMinimum:")
print(np.min(numbers))

print("\nSquared Values:")
print(numbers ** 2)