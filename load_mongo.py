import os
import pandas as pd
from pymongo import MongoClient, UpdateOne
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["titanic_project"]
collection = db["passengers"]

df = pd.read_csv("data/processed_titanic.csv")
records = df.to_dict(orient="records")

operations = [
    UpdateOne(
        {"Passengerid": record["Passengerid"]},
        {"$set": record},
        upsert=True
    )
    for record in records
]

result = collection.bulk_write(operations)

print(f"Matched (already existed): {result.matched_count}")
print(f"Newly inserted: {result.upserted_count}")
print(f"Modified: {result.modified_count}")

client.close()