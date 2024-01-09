from faker import Faker
from pymongo import MongoClient
from bson import ObjectId
from random import randint, choice
from datetime import datetime, timedelta

fake = Faker()

# Connect to MongoDB
client = MongoClient('mongodb://dbadmin:dbadmin@127.0.0.1:27017/')
db = client['demodb']  # Replace 'demodb' with your actual database name
citizens_collection = db['citizens']

# Function to generate a random U.S. citizen document


def generate_citizen():
    return {
        '_id': ObjectId(),
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'dateOfBirth': datetime.combine(
            fake.date_of_birth(minimum_age=18, maximum_age=150),
            datetime.min.time()
        ),
        'socialSecurityNumber': fake.ssn(),
        'gender': choice(['Male', 'Female']),
        'maritalStatus': choice(['Single', 'Married', 'Divorced']),
        'contacts': {
            'emails': [fake.email() for _ in range(randint(1, 3))],
            'phones': [fake.phone_number() for _ in range(randint(1, 3))],
        },
        'addresses': [
            {
                'street': fake.street_address(),
                'city': fake.city(),
                'state': fake.state_abbr(),
                'zipCode': fake.zipcode(),
            }
            for _ in range(randint(1, 3))
        ],
        'employment': {
            'occupation': fake.job(),
            'employer': fake.company(),
            'annualIncome': randint(30000, 150000),
        },
        'education': {
            'degree': fake.random_element(['High School', 'Bachelor', 'Master', 'PhD']),
            'school': fake.company(),
            'graduationYear': randint(1970, 2022),
        },
        'votingHistory': {
            'registered': fake.boolean(chance_of_getting_true=80),
            'lastVoted': fake.date_this_decade(),
            'pollingLocation': fake.random_element(['Community Center', 'School', 'Library']),
        },
        'memberships': [fake.word() for _ in range(randint(1, 5))],
        'interests': [fake.word() for _ in range(randint(1, 5))],
        'emergencyContact': {
            'name': fake.name(),
            'relationship': fake.random_element(['Spouse', 'Sibling', 'Friend']),
            'phone': fake.phone_number(),
        },
    }


# Generate and insert 100,000 citizen documents
for _ in range(100000):
    citizen_data = generate_citizen()
    citizens_collection.insert_one(citizen_data)

print("Data generation complete.")
