from faker import Faker
from pymongo import MongoClient

# Initialize Faker and MongoDB connection
fake = Faker()
# Update with your MongoDB connection string
client = MongoClient("mongodb://dbadmin:dbadmin@localhost:27017")
db = client["demodb"]  # Replace with your database name
collection = db["users"]  # Replace with your collection name

# Function to generate a fake address


def generate_fake_address():
    return {
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.zipcode(),
    }


# Update existing users with fake addresses
users = db.users.find({})  # Replace with your query to select users

for user in users:
    fake_address = generate_fake_address()

    # Update the "addresses" array for each user
    collection.update_one(
        {"_id": user["_id"]},
        {"$push": {"addresses": fake_address}},
    )

# Close the MongoDB connection
client.close()
