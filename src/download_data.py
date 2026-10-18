


from datasets import load_dataset

print("Loading tourism review dataset...")

dataset = load_dataset(
    "UOM-CSE-E23/Sri-Lankan-Tourism-Review-Incongruence"
)

df = dataset["train"].to_pandas()

print("\nDataset loaded successfully!")
print("Rows and columns:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())

import os

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/tourism_reviews.csv", index=False)

print("\nDataset saved successfully!")
print("File: data/raw/tourism_reviews.csv")
