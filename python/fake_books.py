import pymongo
from faker import Faker
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://dbadmin:dbadmin@localhost:27017/")
db = client["demodb"]  # Replace with your actual database name
collection = db["users"]

# Function to generate a random list of favorite books


def generate_favorite_books():
    book_titles = [
        "To Kill a Mockingbird",
        "1984",
        "The Great Gatsby",
        "Pride and Prejudice",
        "The Catcher in the Rye",
        "Harry Potter and the Sorcerer's Stone",
        "The Hobbit",
        "The Lord of the Rings",
        "The Hunger Games",
        "The Da Vinci Code",
    ]

    # Randomly select a subset of books
    num_books = random.randint(1, len(book_titles))
    return random.sample(book_titles, num_books)


# Update existing users with random favorite books
cursor = collection.find({})  # Retrieve all documents in the collection

for user in cursor:
    new_books = generate_favorite_books()

    # Update the user document with the new favorite_books
    collection.update_one(
        {"_id": user["_id"]},
        {"$set": {"favorite_books": new_books}}
    )

print("Users updated successfully.")
