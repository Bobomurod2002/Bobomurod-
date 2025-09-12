#1
import pandas as pd

# 1. Ma’lumotlarni o‘qish
sales_df = pd.read_csv(r"c:\Users\User\Documents\sales_data.csv")

# 2. Kategoriya bo‘yicha agregat statistikalar
category_stats = sales_df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    average_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
)

# 3. Har bir kategoriyada eng ko‘p sotilgan mahsulot
top_products = sales_df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
top_products = top_products.groupby("Category").first()

# 4. Eng katta savdo kuni
sales_df["TotalSales"] = sales_df["Quantity"] * sales_df["Price"]
top_sales_date = sales_df.groupby("Date")["TotalSales"].sum().idxmax()

#2
# 1. Ma’lumotlarni o‘qish
orders_df = pd.read_csv(r"c:\Users\User\Documents\customer_orders.csv")

# 2. 20 tadan kam buyurtma qilganlarni chiqarib tashlash
customer_order_counts = orders_df.groupby("CustomerID")["OrderID"].count()
valid_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_orders = orders_df[orders_df["CustomerID"].isin(valid_customers)]

# 3. O‘rtacha narxi $120 dan katta bo‘lgan mijozlar
avg_price_per_customer = orders_df.groupby("CustomerID")["Price"].mean()
high_price_customers = avg_price_per_customer[avg_price_per_customer > 120]

# 4. Mahsulot bo‘yicha jami soni va summasi
product_stats = orders_df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
)
filtered_products = product_stats[product_stats["total_quantity"] >= 5]
filtered_products

##3
import sqlite3

# 1. SQLite dan ma’lumot olish
conn = sqlite3.connect(R"c:\Users\User\Documents\population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# 2. Salary Bandlarni yuklash
salary_bands = pd.read_excel(r"c:\Users\User\Documents\population_salary_analysis.xlsx")

# Maosh kategoriyalariga ajratish
import numpy as np

# Salary Band faylini yuklash
salary_bands = pd.read_excel(r"c:\Users\User\Documents\population_salary_analysis.xlsx")

# Bandlarni min va max qilib ajratish funksiyasi
def parse_salary_band(band):
    band = band.replace(",", "").replace("$", "").strip()
    if "till" in band:
        max_salary = int(band.replace("till", "").strip())
        return 0, max_salary
    elif "-" in band:
        parts = band.split("-")
        return int(parts[0].strip()), int(parts[1].strip())
    elif "+" in band:
        return int(band.replace("+", "").strip()), np.inf
    else:
        return np.nan, np.nan

salary_bands[["min_salary", "max_salary"]] = salary_bands["Salary Band"].apply(
    lambda x: pd.Series(parse_salary_band(x))
)

print(salary_bands)


# 3. Har bir salary category uchun hisob
def categorize_salary(salary):
    for _, row in salary_bands.iterrows():
        if row["min_salary"] <= salary <= row["max_salary"]:
            return row["Salary Band"]
    return "Unknown"

population_df["SalaryCategory"] = population_df["salary"].apply(categorize_salary)


# 4. Har bir shtat bo‘yicha hisob
summary = population_df.groupby("SalaryCategory").agg(
    PopulationCount=("salary", "count"),
    AvgSalary=("salary", "mean"),
    MedianSalary=("salary", "median")
).reset_index()

# Aholi foizini qo‘shish
total_population = len(population_df)
summary["PopulationPercent"] = (summary["PopulationCount"] / total_population) * 100

print(summary)
#print(population_df.columns)

#print(salary_bands.columns)
