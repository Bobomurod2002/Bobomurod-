import sqlite3
import pandas as pd

# Yangi database yaratish (RAMda, fayl emas)
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Jadval yaratish
cur.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Ma'lumotlarni qo'shish
cur.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Jadzia Dax -> Ezri Dax yangilash
cur.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Bajoranlarni chiqarish (Name va Age)
cur.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
rows = cur.fetchall()

# Natijani DataFrame ko'rinishida ko'rsatish
df = pd.DataFrame(rows, columns=["Name", "Age"])
# import caas_jupyter_tools
# caas_jupyter_tools.display_dataframe_to_user("Bajoranlar", df)
print(df)

conn.commit()
conn.close()
