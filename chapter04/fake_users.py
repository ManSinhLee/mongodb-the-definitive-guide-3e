import random
from faker import Faker
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient("mongodb://dbadmin:dbadmin@127.0.0.1:27017/")
db = client["demodb"]  # Replace with your actual database name
# Replace with your actual collection name
collection = db["citizens"]

# Instantiate Faker with a specific seed for reproducibility
fake = Faker()
Faker.seed(0)

# List of email domains
email_domains = ['gmail.com', 'outlook.com',
                 'microsoft.com', 'openai.com', 'amazon.com']

# Function to generate income data


def generate_income():
    return [{str(year): random.randint(50000, 100000)} for year in range(2020, 2024)]


# Generate and insert 1,000,000 documents
for _ in range(111):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email_domain = random.choice(email_domains)
    username = f"{first_name}_{last_name}"
    email = f"{first_name.lower()}.{last_name.lower()}@{email_domain}"

    document = {
        "name": f"{first_name} {last_name}",
        "username": username,
        "age": fake.random_int(min=18, max=80),
        "job": fake.job(),
        "country": fake.country(),
        "contact": {"phone": fake.phone_number(), "email": email},
        "addresses": [
            {
                "street": fake.street_address(),
                "city": fake.city(),
                "state": fake.state_abbr(),
                "zip": fake.zipcode(),
            }
        ],
        "income": generate_income(),
        "favorite_books": [
            fake.word() for _ in range(random.randint(1, 5))
        ]
    }

    # Insert document into MongoDB
    collection.insert_one(document)

print("Documents inserted successfully.")
