import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["titanic_project"]  # same database, different collection
collection = db["imdb_reviews"]

df = pd.read_csv("data/processed_imdb.csv")
records = df.to_dict(orient="records")

# Simple insert this time (no natural unique ID in this dataset like Passengerid)
result = collection.insert_many(records)

print(f"Inserted {len(result.inserted_ids)} documents into MongoDB!")

client.close()