#1
import json

def parse_students(filename="students.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("Students Details:")
        for student in data.get("students", []):  # students ro'yxati ichida
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print(f"❌ File {filename} not found.")
    except json.JSONDecodeError:
        print("❌ Invalid JSON format.")

#2
def get_weather(city="Tashkent", api_key="YOUR_API_KEY_HERE"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"Weather in {city}:")
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])
    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)

#3
def load_books(filename="books.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"books": []}

def save_books(data, filename="books.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_book(title, author, year):
    data = load_books()
    data["books"].append({"title": title, "author": author, "year": year})
    save_books(data)
    print("✅ Book added successfully!")

def update_book(title, new_author=None, new_year=None):
    data = load_books()
    for book in data["books"]:
        if book["title"] == title:
            if new_author:
                book["author"] = new_author
            if new_year:
                book["year"] = new_year
            save_books(data)
            print("✅ Book updated successfully!")
            return
    print("❌ Book not found.")

def delete_book(title):
    data = load_books()
    data["books"] = [book for book in data["books"] if book["title"] != title]
    save_books(data)
    print("✅ Book deleted successfully!")

#4
def recommend_movie(genre, api_key="YOUR_OMDB_API_KEY"):
    url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "Search" not in data:
            print("❌ No movies found for this genre.")
            return

        movie = random.choice(data["Search"])
        print("🎬 Recommended Movie:")
        print("Title:", movie["Title"])
        print("Year:", movie["Year"])
        print("IMDb ID:", movie["imdbID"])
    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)


