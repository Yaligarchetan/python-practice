# =========================
# NumPy Basics for Beginners
# =========================

import numpy as np

# --------------------------
# 1. Creating NumPy Arrays
# --------------------------

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# 2D array (matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Shape, size, and data type
print("arr1 shape:", arr1.shape)    # (5,)
print("arr2 shape:", arr2.shape)    # (2, 3)
print("arr2 size:", arr2.size)      # 6
print("arr2 dtype:", arr2.dtype)    # typically int64 or float64

# -----------------------
# 2. Array Operations
# -----------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print("a + b:", a + b)      # [5 7 9]
print("a * b:", a * b)      # [4 10 18]

# Scalar operations
print("a * 2:", a * 2)      # [2 4 6]

# Universal functions (ufuncs)
print("sqrt(a):", np.sqrt(a))     # [1.         1.41421356 1.73205081]
print("exp(a):", np.exp(a))       # [ 2.71828183  7.3890561  20.08553692]

# -----------------------
# 3. Array Indexing/Slicing
# -----------------------

arr = np.array([10, 20, 30, 40, 50])
print("arr[1]:", arr[1])         # 20
print("arr[1:4]:", arr[1:4])     # [20 30 40]

# 2D slicing
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("arr2d[1, 2]:", arr2d[1, 2])   # 6
print("arr2d[:, 1]:", arr2d[:, 1])   # [2 5 8]

# -----------------------
# 4. Creating Special Arrays
# -----------------------

print("Zeros (3x3):\n", np.zeros((3, 3)))     # 3x3 matrix of zeros
print("Ones (length 5):", np.ones(5))        # array of ones
print("Arange (0-10 step 2):", np.arange(0, 10, 2))  # [0 2 4 6 8]
print("Linspace (0 to 1, 5 points):", np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1.  ]

# -----------------------
# 5. Reshaping Arrays
# -----------------------

arr = np.arange(1, 13)              # [1 2 3 ... 12]
reshaped = arr.reshape((3, 4))      # Reshape to 3 rows, 4 cols
print("Reshaped (3x4):\n", reshaped)

# -----------------------
# 6. Aggregate Functions
# -----------------------

arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))         # 15
print("Mean:", np.mean(arr))       # 3.0
print("Max:", np.max(arr))         # 5
print("Min:", np.min(arr))         # 1
print("Standard Deviation:", np.std(arr))   # std deviation

