from faker import Faker
from pymongo import MongoClient
import random

# Connect to MongoDB
client = MongoClient('mongodb://dbadmin:dbadmin@127.0.0.1:27017/')
# Replace 'your_database_name' with your actual database name
db = client['demodb']
students_collection = db['students']

# Create a Faker instance
fake = Faker()

# Function to generate random student data


# Function to generate random student data
def generate_student():
    student_id = random.randint(100000, 999999)  # Adjust the range as needed
    name = fake.name()
    birth_year = fake.random_int(1980, 2005)
    email = fake.email()
    address = fake.address()
    country = fake.country()
    class_id = fake.random_int(1, 10)
    courses = [fake.word() for _ in range(random.randint(1, 5))]
    grades = {course: random.randint(60, 100) for course in courses}

    return {
        "student_id": student_id,
        "name": name,
        "birth_year": birth_year,
        "email": email,
        "address": address,
        "country": country,
        "class_id": class_id,
        "courses": courses,
        "grades": grades
    }


# Generate and insert 100,000 documents
for _ in range(100000):
    student_data = generate_student()
    students_collection.insert_one(student_data)

print("Data generation complete.")
