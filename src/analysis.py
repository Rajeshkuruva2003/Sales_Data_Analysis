import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

# Data cleaning and validation
df = df.drop_duplicates()
df = df.dropna(subset=["region", "category", "product", "quantity", "unit_price"])
df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]
df["sales"] = df["quantity"] * df["unit_price"]

# Business analysis
monthly = df.groupby(df["order_date"].dt.to_period("M"))["sales"].sum()
region = df.groupby("region")["sales"].sum().sort_values(ascending=False)
category = df.groupby("category")["sales"].sum().sort_values(ascending=False)
product = df.groupby("product")["sales"].sum().sort_values(ascending=False)

print("Total Revenue:", round(df["sales"].sum(), 2))
print("\nRevenue by Region:\n", region)
print("\nRevenue by Category:\n", category)
print("\nTop 5 Products:\n", product.head())

monthly.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month"); plt.ylabel("Sales"); plt.tight_layout()
plt.savefig("reports/monthly_sales.png"); plt.close()

region.plot(kind="bar", title="Sales by Region")
plt.xlabel("Region"); plt.ylabel("Sales"); plt.tight_layout()
plt.savefig("reports/region_sales.png"); plt.close()

df.to_csv("reports/clean_sales_data.csv", index=False)
