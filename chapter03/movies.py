import faker
from pymongo import MongoClient
from datetime import datetime

# Connection URL
url = 'mongodb://admin:admin@localhost:27017'

# Database Name
db_name = 'demodb'

# Set the connection timeout in milliseconds
connect_timeout_ms = 5000  # 5 seconds

# Create a new MongoClient with connectTimeoutMS option
client = MongoClient(url, serverSelectionTimeoutMS=connect_timeout_ms)

try:
    # Use the database
    db = client[db_name]
    movies_collection = db['movies']

    # Number of movies to generate
    num_movies = 10

    # Array of possible genres
    genres = ['Action', 'Comedy', 'Drama', 'Horror',
              'Science Fiction', 'Adventure', 'Romance', 'Thriller', 'Fantasy']

    # Generate random movies with genres
    for _ in range(num_movies):
        movie = {
            'title': faker.Faker().sentence(),
            'releaseYear': datetime.now().year,
            'genre': faker.Faker().random_element(genres),
            'director': faker.Faker().name(),
        }

        movies_collection.insert_one(movie)
        print(f"Inserted movie: {movie['title']}")

finally:
    # Close the connection
    client.close()
