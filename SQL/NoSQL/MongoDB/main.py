import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# MongoDB configuration
MONGO_URI = (
    f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:"
    f"{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}"
    "@localhost:27017/?authSource=admin"
)

# Create client
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=50000
)


#CHECK CLUSTER
def cluster_check():
    print("SERVER INFO : ",client.server_info())
    print(client.admin.command("ping"))

#DATABASE LIST
def db_list():
    print(client.list_database_names())



db_list()

#DEFINE NEW DB
new_db = client["University"]

#CREATE NEW COLLECTIONS
south_us = new_db["School"]

#ADD VALUE IN DOCUMENT 
south_us.insert_one({
    "name": "Pranit",
    "age": 23,
    "salary": 50000,
    "skills": ["Python", "SQL", "MongoDB"]
})

print(south_us.find_one())
print(new_db.list_collection_names())

for doc in south_us.find():
    print(doc)
