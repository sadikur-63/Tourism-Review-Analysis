
import pandas as pd

# Load the tourism reviews dataset
df = pd.read_csv("data/raw/tourism_reviews.csv")

print("TOURISM REVIEW ANALYSIS")
print("=" * 40)

# 1. Dataset overview
print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# 2. Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Average rating by destination
print("\nTop 10 destinations by average rating:")
destination_ratings = (
    df.groupby("Location_Name")["Rating"]
    .agg(["mean", "count"])
    .rename(columns={"mean": "Average_Rating", "count": "Review_Count"})
    .sort_values("Average_Rating", ascending=False)
)

print(destination_ratings.head(10).round(2))

# 4. Sentiment distribution
print("\nSentiment distribution:")
print(df["Sentiment"].value_counts(dropna=False))

# 5. Save results
destination_ratings.to_csv(
    "outputs/destination_ratings.csv"
)

print("\nAnalysis complete!")
print("Results saved to outputs/destination_ratings.csv")
