#Homework1
import pandas as pd
import numpy as np

# DataFrame yaratish
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Ustun nomlarini o'zgartirish (funksiya orqali)
df = df.rename(columns=lambda x: x.lower().replace(" ", "_"))

# 2. Dastlabki 3 qatorni chiqarish
print(df.head(3))

# 3. O‘rtacha yoshni hisoblash
print("Mean age:", df['age'].mean())

# 4. Faqat 'first_name' va 'city' ustunlarini chiqarish
print(df[['first_name', 'city']])

# 5. Yangi 'salary' ustunini qo‘shish (tasodifiy qiymatlar bilan)
df['salary'] = np.random.randint(4000, 8000, size=len(df))
print(df)

# 6. Statistik ma’lumotlarni chiqarish
print(df.describe())

#Homework2
import pandas as pd

# DataFrame yaratish
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data)

# 1. Maksimal qiymatlar
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# 2. Minimal qiymatlar
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# 3. O‘rtacha qiymatlar
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

#Homework3
import pandas as pd

# DataFrame yaratish
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data)

# 'Category' ustunini indeksga aylantirish
expenses = expenses.set_index('Category')

# 1. Har bir kategoriya bo‘yicha maksimal xarajat
print("Max expense per category:\n", expenses.max(axis=1))

# 2. Har bir kategoriya bo‘yicha minimal xarajat
print("Min expense per category:\n", expenses.min(axis=1))

# 3. Har bir kategoriya bo‘yicha o‘rtacha xarajat
print("Average expense per category:\n", expenses.mean(axis=1))
