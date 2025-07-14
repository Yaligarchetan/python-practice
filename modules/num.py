import numpy as np
# Example usage of numpy
# Create a 1D array 
'''
arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1.shape)    # (5,)
print(arr2.shape)    # (2, 3)
print(arr2.size)     # Total elements: 6
print(arr2.dtype)    # Data type (usually int64 or float64)

# array operations
# Element-wise addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)    # [5 7 9]

# Element-wise multiplication
print(a * b)    # [4 10 18]

# Scalar operations
print(a * 2)    # [2 4 6]

# Universal functions (ufuncs)
print(np.sqrt(a))    # [1. 1.414 1.732]
print(np.exp(a))     # [2.718, 7.389, 20.085]
'''

# Array slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[1])     # 20
print(arr[1:4])   # [20 30 40]

# 2D slicing
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[1, 2])   # element at 2nd row, 3rd col -> 6
print(arr2d[:, 1])   # all rows, 2nd column -> [2 5 8]

#6. Creating arrays of zeros, ones, and ranges

print(np.zeros((3,3)))      # 3x3 matrix of zeros
print(np.ones(5))           # array of ones length 5
print(np.arange(0, 10, 2))  # from 0 to 10 step 2 -> [0 2 4 6 8]
print(np.linspace(0, 1, 5)) # 5 numbers evenly spaced between 0 and 1

#7. Reshaping arrays

arr = np.arange(1, 13)  # array from 1 to 12
print(arr.reshape((3, 4)))  # reshape to 3 rows, 4 columns

# 8. Aggregate functions
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))      # 15
print(np.mean(arr))     # 3.0
print(np.max(arr))      # 5
print(np.min(arr))      # 1
print(np.std(arr))      # Standard deviation