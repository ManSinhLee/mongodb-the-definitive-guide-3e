import pymongo
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://dbadmin:dbadmin@127.0.0.1:27017/")
db = client["demodb"]  # Replace with your actual database name
collection = db["citizens"]  # Replace with your actual collection name

# Generate a list of 20 books
all_books = [
    "The Catcher in the Rye", "To Kill a Mockingbird", "1984", "The Great Gatsby",
    "Pride and Prejudice", "The Hobbit", "The Lord of the Rings", "The Alchemist",
    "The Shining", "Brave New World", "Fahrenheit 451", "One Hundred Years of Solitude",
    "The Chronicles of Narnia", "The Harry Potter Series", "The Hunger Games",
    "The Kite Runner", "The Da Vinci Code", "The Bible", "The Art of War"
]

# Randomly choose 5 books
selected_books = random.sample(all_books, 5)

# Update the existing documents in the collection
update_result = collection.update_many(
    {},
    {"$addToSet": {"favorite_books": {"$each": selected_books}}}
)

print(f"Number of documents matched: {update_result.matched_count}")
print(f"Number of documents modified: {update_result.modified_count}")
