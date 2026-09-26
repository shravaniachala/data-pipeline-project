import pandas as pd

df = pd.read_csv("data/raw/train_and_test2.csv")

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df['zero'].unique())
print(df['zero.1'].unique())