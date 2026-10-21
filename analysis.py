import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


connection = sqlite3.connect("sales.db")

df = pd.read_sql_query("SELECT * FROM sales", connection)

df["revenue"] = df["quantity"] * df["unit_price"]

product_revenue = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(product_revenue)

df["month"] = df["date"].str[:7]

monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
    .sort_index()
)
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

total_revenue = df["revenue"].sum()
total_quantity = df["quantity"].sum()
total_orders = df["order_id"].nunique()
best_product = product_revenue.idxmax()
product_revenue.to_csv("product_revenue.csv")
monthly_revenue.to_csv("monthly_revenue.csv")
category_revenue.to_csv("category_revenue.csv")



print("\nCSV files created successfully!")
print("\nBusiness Summary:")
print(f"Total Revenue: {total_revenue}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Total Orders: {total_orders}")
print(f"Best Product: {best_product}")

print("\nRevenue by Category:")
print(category_revenue)
print("\nMonthly Revenue:")
print(monthly_revenue)
connection.close()