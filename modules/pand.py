# ============================
# Pandas Basics for Beginners
# ============================

import pandas as pd

# ------------------------
# 1. What is pandas?
# ------------------------
"""
Pandas is a powerful Python library for data analysis and manipulation.
It provides two main data structures:
- Series: 1D labeled array
- DataFrame: 2D labeled table (like an Excel spreadsheet or SQL table)
"""

# --------------------------
# 2. Creating a DataFrame
# --------------------------

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NYC', 'LA', 'Chicago', 'Houston'],
}

df = pd.DataFrame(data)

# --------------------------
# 3. Exploring the DataFrame
# --------------------------

print("\nHead of DataFrame:\n", df.head())         # First 5 rows
print("\nDescribe DataFrame:\n", df.describe())    # Summary stats (numeric)
print("\nShape of DataFrame:", df.shape)           # (rows, columns)
print("\nColumn Names:", df.columns.tolist())      # ['Name', 'Age', 'City']
print("\nInfo Summary:")
df.info()                                          # Data types and non-null info
print("\nMissing Values:\n", df.isnull().sum())    # Check for missing values

# --------------------------
# 4. Accessing Columns & Rows
# --------------------------

print("\nAccess 'Name' column:\n", df['Name'])             # Access a column
print("\nAccess first row using iloc:\n", df.iloc[0])      # Access by index
print("\nAccess rows where Age > 30:\n", df[df['Age'] > 30])

# --------------------------
# 5. Adding & Modifying Columns
# --------------------------

df['Salary'] = [50000, 60000, 70000, 80000]       # Adding new column
df['Senior'] = df['Age'] > 30                     # Conditional column

print("\nDataFrame with new columns:\n", df)

# --------------------------
# 6. Basic Operations
# --------------------------

print("\nAverage Age:", df['Age'].mean())         # Mean of Age
print("Max Salary:", df['Salary'].max())          # Max of Salary

# --------------------------
# 7. Sorting & Filtering
# --------------------------

print("\nSorted by Age:\n", df.sort_values(by='Age'))
print("\nFiltered (City == 'NYC'):\n", df[df['City'] == 'NYC'])

# --------------------------
# 8. Grouping & Aggregation
# --------------------------

# Group by City and calculate average age
grouped = df.groupby('City')['Age'].mean()
print("\nAverage Age by City:\n", grouped)

