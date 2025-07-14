import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie','David'],
    'Age': [25, 30, 35, 40],
    'City': ['NYC', 'LA', 'Chicago','Houston'],
}
df = pd.DataFrame(data)
print("\n Data head",df.head())  # Display the first few rows of the DataFrame
print("\n Data describe",df.describe())  # Get summary statistics of the DataFrame
print("\n Data shape:", df.shape) # Get the shape of the DataFrame
print("\n Data columns:", df.columns)  # Get the column names of the DataFrame
print("\n Data info:", df.info())  # Get a concise summary of the DataFrame
print("\n Data isnull:", df.isnull().sum())  # Check for missing values