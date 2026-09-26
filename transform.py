import pandas as pd

# Load the raw data
df = pd.read_csv("data/raw/train_and_test2.csv")

# Drop all the useless "zero" columns
zero_columns = [col for col in df.columns if col.startswith("zero")]
df = df.drop(columns=zero_columns)

# Rename the oddly-named survival column
df = df.rename(columns={"2urvived": "Survived"})

# Look at the cleaned result
print(df.head())
print("Shape after cleaning:", df.shape)
print("Columns after cleaning:", df.columns.tolist())

# Save the cleaned version to a new file
df.to_csv("data/processed_titanic.csv", index=False)
print("Cleaned file saved!")