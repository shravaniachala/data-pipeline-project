import os
import pandas as pd
from pymongo import MongoClient, UpdateOne
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["titanic_project"]
collection = db["imdb_reviews"]

df = pd.read_csv("data/processed_imdb.csv")
df = df.reset_index().rename(columns={"index": "review_id"})
records = df.to_dict(orient="records")

batch_size = 1000
total_matched = 0
total_inserted = 0

for i in range(0, len(records), batch_size):
    batch = records[i:i + batch_size]
    operations = [
        UpdateOne(
            {"review_id": record["review_id"]},
            {"$set": record},
            upsert=True
        )
        for record in batch
    ]
    result = collection.bulk_write(operations)
    total_matched += result.matched_count
    total_inserted += result.upserted_count
    print(f"Processed batch {i // batch_size + 1} — matched: {result.matched_count}, inserted: {result.upserted_count}")

print(f"\nDone! Total matched: {total_matched}, Total newly inserted: {total_inserted}")

client.close()