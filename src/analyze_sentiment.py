
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

df = pd.read_csv("data/raw/tourism_reviews.csv")

# Count reviews in each sentiment category
sentiment_counts = df["Sentiment"].fillna("Unknown").value_counts()

print("Sentiment Distribution")
print("=" * 30)
print(sentiment_counts)

# Create a bar chart
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")

plt.title("Tourism Review Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "outputs/figures/sentiment_distribution.png",
    dpi=300
)
plt.close()

# Save the counts
sentiment_counts.to_csv("outputs/tables/sentiment_counts.csv")

print("\nSentiment chart and summary saved successfully!")
