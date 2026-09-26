import pandas as pd

df = pd.read_csv("data/raw/imdb_reviews.csv")

print("Before cleaning:", df.shape)

# Remove any duplicate reviews
df = df.drop_duplicates()

# Remove rows where the review text is empty/missing
df = df.dropna(subset=["text"])

# Rename 'label' to something more descriptive
df = df.rename(columns={"label": "sentiment"})

# Optional: make sentiment human-readable instead of 0/1
df["sentiment"] = df["sentiment"].map({0: "negative", 1: "positive"})

print("After cleaning:", df.shape)
print(df.head())

df.to_csv("data/processed_imdb.csv", index=False)
print("Saved cleaned file to data/processed_imdb.csv")