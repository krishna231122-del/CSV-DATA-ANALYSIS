import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv("sales.csv")

#adding total price column
df["total"] = df["Quantity"] * df["Price"]

#total revenue
total_revenue = df["total"].sum()
print(f"Total Revenue: ${total_revenue:.2f}")

#best selling product
best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
print(f"Best Selling Product: {best_selling_product}") 

#revenue by category
revenue_by_category = df.groupby("Category")["total"].sum()
print("Revenue by Category:")
print(revenue_by_category)

#revenue by region 
revenue_by_region = df.groupby("Region")["total"].sum()
print("Revenue by Region:")
print(revenue_by_region)

#average order value
average_order_value = df["total"].mean()
print(f"Average Order Value: ${average_order_value:.2f}")

#visualization
plt.figure(figsize=(6,4) )
revenue_by_category.plot(kind='bar', color='skyblue')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
