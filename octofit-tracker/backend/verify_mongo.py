from pymongo import MongoClient

def verify_mongo_connection():
    try:
        # Connect to the MongoDB server
        client = MongoClient("mongodb://localhost:27017/")
        # Run a command to check the connection
        status = client.admin.command("ping")
        print("MongoDB connection successful:", status)
    except Exception as e:
        print("Error connecting to MongoDB:", e)

if __name__ == "__main__":
    verify_mongo_connection()
