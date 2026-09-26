from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

df = dataset.to_pandas()

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

df.to_csv("data/raw/imdb_reviews.csv", index=False)
print("Saved to data/raw/imdb_reviews.csv")