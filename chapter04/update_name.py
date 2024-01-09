import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://dbadmin:dbadmin@localhost:27017/")
db = client["demodb"]  # Replace with your actual database name
collection = db["users"]

# Find users without a 'name' field
users_without_name = collection.find({"name": {"$exists": False}})

# Update 'name' with the combination of 'first_name' and 'last_name'
for user in users_without_name:
    first_name = user.get("first_name", "")
    last_name = user.get("last_name", "")

    if first_name and last_name:
        full_name = f"{first_name} {last_name}"

        # Update the user document with the new 'name'
        collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"name": full_name}}
        )

print("Users updated successfully.")
