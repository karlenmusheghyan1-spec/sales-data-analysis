
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

plt.figure(figsize=(8, 5))

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("product_revenue.png")
plt.show()


monthly_revenue = (
    df.assign(month=df["date"].str[:7])
    .groupby("month")["revenue"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(8, 5))
monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()

connection.close()