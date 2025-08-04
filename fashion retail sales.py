import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\work\python programs\fashion_retail_sales.csv")

# Convert 'Date Purchase' to datetime format safely
df['Date Purchase'] = pd.to_datetime(df['Date Purchase'], dayfirst=True, errors='coerce')

# Drop rows with missing critical values
df.dropna(subset=['Date Purchase', 'Item Purchased', 'Purchase Amount (USD)'], inplace=True)

# Convert USD to INR (Assume 1 USD = ₹83.00)
conversion_rate = 83.00
df['Purchase Amount (INR)'] = df['Purchase Amount (USD)'] * conversion_rate

# Set seaborn style
sns.set(style="whitegrid")

# 1. Total Sales by Item Purchased (INR)
plt.figure(figsize=(10, 6))
item_sales = df.groupby('Item Purchased')['Purchase Amount (INR)'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=item_sales, x='Purchase Amount (INR)', y='Item Purchased', palette='viridis', hue='Item Purchased', legend=False)
plt.title('Total Sales by Item Purchased (INR)')
plt.xlabel('Total Sales (INR)')
plt.ylabel('Item Purchased')
plt.tight_layout()
plt.show()
                
# 2. Sales Over Time (Monthly Trend in INR)
plt.figure(figsize=(12, 6))
daily_sales = df.groupby('Date Purchase')['Purchase Amount (INR)'].sum()
daily_sales.plot(marker='o')
plt.title('Sales Over Time (INR)')
plt.xlabel('Month')
plt.ylabel('Total Sales (INR)')
plt.tight_layout()
plt.show()

# 3. Review Rating Distribution
plt.figure(figsize=(8, 5))
order = sorted(df['Review Rating'].dropna().unique())
sns.countplot(data=df, x='Review Rating', palette='coolwarm', order=order, hue='Review Rating', legend=False)
plt.title('Review Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 4. Payment Method Usage
plt.figure(figsize=(8, 5))
payment_counts = df['Payment Method'].value_counts().reset_index()
payment_counts.columns = ['Payment Method', 'Count']
sns.barplot(data=payment_counts, x='Payment Method', y='Count', palette='Set2', hue='Payment Method', legend=False)
plt.title('Payment Method Usage')
plt.xlabel('Payment Method')
plt.ylabel('Number of Purchases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Top 10 Customers by Spending (INR)
plt.figure(figsize=(10, 6))
top_customers = df.groupby('Customer Reference ID')['Purchase Amount (INR)'].sum().nlargest(10).reset_index()
sns.barplot(data=top_customers, x='Purchase Amount (INR)', y='Customer Reference ID', palette='magma', hue='Customer Reference ID', legend=False)
plt.title('Top 10 Customers by Spending (INR)')
plt.xlabel('Total Spending (INR)')
plt.ylabel('Customer Reference ID')
plt.tight_layout()
plt.show()

# 6. Yeraly Revenue Trend (INR)
plt.figure(figsize=(12, 6))
df['Month'] = df['Date Purchase'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Purchase Amount (INR)'].sum().reset_index()
sns.lineplot(data=monthly_sales, x='Month', y='Purchase Amount (INR)', marker='o')
plt.title('Yearly Revenue Trend (INR)')
plt.xlabel('Yearly')
plt.ylabel('Total Revenue (INR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
