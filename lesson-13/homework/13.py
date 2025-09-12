import datetime  # datetime modulini import qilamiz

dob_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()  # datetime.datetime ni ishlatish
today = datetime.date.today()  # date.today() o'rniga datetime.date.today() ishlatish

print(f"Tug‘ilgan sanangiz: {dob}")
print(f"Bugungi sana: {today}")

years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
months = (today.year - dob.year) * 12 + today.month - dob.month
days = (today - dob).days

import datetime
print(f"Sizning yoshingiz: {years} yil, {months} oy, {days} kun")
dob_str = input("Tug‘ilgan kuningiz (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
today = datetime.date.today()

next_birthday = dob.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"Keyingi tug‘ilgan kuningizga {days_left} kun qoldi 🎉")
from datetime import timedelta

import datetime
now_str = input("Hozirgi sana va vaqt (YYYY-MM-DD HH:MM): ")
now = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M")

hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

end_time = now + timedelta(hours=hours, minutes=minutes)
print("Uchrashuv tugash vaqti:", end_time)
from datetime import datetime

import datetime
import pytz

dt_str = "2025-09-12 15:30"
from_zone = "UTC"
to_zone = "Asia/Tashkent"

dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

dt_local = from_tz.localize(dt)
dt_converted = dt_local.astimezone(to_tz)

print("Natija:", dt_converted.strftime("%Y-%m-%d %H:%M"))
import time

import datetime
future_str = input("Kelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): ")
future = datetime.datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

import datetime
while True:       
    now = datetime.datetime.now()
    if now >= future:
        print("⏰ Vaqt tugadi!")
        break
    remaining = future - now
    print("Qolgan vaqt:", remaining, end="\r")
    time.sleep(1)
import re

email = input("Emailni kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("✅ To‘g‘ri email manzil")
else:
    print("❌ Noto‘g‘ri email manzil")
num = input("Telefon raqam kiriting (faqat raqamlar): ")

if len(num) == 10 and num.isdigit():
    formatted = f"({num[:3]}) {num[3:6]}-{num[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("❌ 10 ta raqam kiriting")
import re

password = input("Parolni kiriting: ")

if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'[0-9]', password)):
    print("✅ Kuchli parol")
else:
    print("❌ Parol kuchsiz (kamida 8 belgidan iborat, katta-harflar, kichik-harflar va raqam bo‘lishi kerak)")
text = "Python is powerful. Python is easy to learn. Python is everywhere."
word = input("Qidiriladigan so‘z: ")

positions = [i for i in range(len(text.split())) if text.split()[i].lower() == word.lower()]
print(f"'{word}' so‘zi {len(positions)} marta topildi. Indekslar:", positions)
import re

text = input("Matn kiriting (masalan: Today is 2025-09-10, tomorrow is 2025/09/11): ")
dates = re.findall(r'\d{4}[-/]\d{2}[-/]\d{2}', text)

print("Topilgan sanalar:", dates)
