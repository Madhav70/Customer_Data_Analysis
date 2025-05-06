import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('customers-100.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.describe(include='all'))
print(df.isnull().sum())
for col in df.columns:
    print(col)
city_counts = df['City'].value_counts().sort_values(ascending=False)

# Plot the bar chart
plt.figure(figsize=(12, 6))
city_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Customers per City')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')

# Drop rows with invalid dates (if any)
df = df.dropna(subset=['Subscription Date'])

# Extract year-month for grouping
df['Subscription Month'] = df['Subscription Date'].dt.to_period('M').astype(str)

# Plot the histogram
plt.figure(figsize=(12, 6))
df['Subscription Month'].value_counts().sort_index().plot(kind='bar', color='orange')
plt.title('Customer Sign-ups per Month')
plt.xlabel('Month')
plt.ylabel('Number of Sign-ups')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
city_counts = df['City'].value_counts().sort_values(ascending=False)

# Plot the bar chart
plt.figure(figsize=(12, 6))
city_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Customers per City', fontsize=16)
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
city_counts.head(10).plot(kind='bar', figsize=(10,5), color='green')
plt.title('Top 10 Cities by Customer Count')
import seaborn as sns

top_cities = city_counts.head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_cities.index, y=top_cities.values, palette='Blues_d')
plt.title('Top 10 Cities by Number of Customers')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
for i, val in enumerate(top_cities.values):
    plt.text(i, val + 0.5, val, ha='center')
plt.tight_layout()
plt.show()
country_counts = df['Country'].value_counts()

# Plot bar chart
plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Number of Customers per Country')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()