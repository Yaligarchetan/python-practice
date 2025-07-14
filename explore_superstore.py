import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = r"C:\your\file\path of datasets[i used superstore datasets from kaggle]"
data = pd.read_excel(file_path, engine='xlrd')

# Convert date columns if needed
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

# 1. Peek at the data
print("First 5 rows:\n", data.head())
print("\nData shape:", data.shape)
print("\nColumns:\n", data.columns)
print("\nInfo:\n")
data.info()
print("\nSummary statistics:\n", data.describe())

# 2. Check missing data
print("\nMissing values per column:\n", data.isnull().sum())

# 3. Aggregate: total sales by Category
sales_by_category = data.groupby('Category')['Sales'].sum()
print("\nTotal Sales by Category:\n", sales_by_category)

# 4. Aggregate: average profit by Region
profit_by_region = data.groupby('Region')['Profit'].mean()
print("\nAverage Profit by Region:\n", profit_by_region)

# 5. Filter: orders with profit > 1000
high_profit = data[data['Profit'] > 1000]
print("\nOrders with Profit > 1000:\n", high_profit.head())

# 6. Add a new calculated column: Profit Margin (%)
data['Profit Margin (%)'] = data['Profit'] / data['Sales'] * 100

# 7. Sort data: top 10 most profitable orders
top_orders = data.sort_values('Profit', ascending=False).head(10)
print("\nTop 10 Most Profitable Orders:\n", top_orders[['Order ID', 'Profit']])

# 8. Visualization: Total Sales by Category (bar plot)
plt.figure(figsize=(8,5))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values)
plt.title('Total Sales by Category')
plt.ylabel('Total Sales')
plt.xlabel('Category')
plt.tight_layout()
plt.show()
