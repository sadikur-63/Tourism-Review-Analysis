
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create the figures folder if it doesn't exist
os.makedirs("outputs/figures", exist_ok=True)

# Load destination rating results
ratings = pd.read_csv("outputs/destination_ratings.csv")

# Select the 10 destinations with the highest average ratings
top10 = ratings.sort_values(
    "Average_Rating", ascending=False
).head(10)

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(
    top10["Location_Name"],
    top10["Average_Rating"]
)

plt.title("Top 10 Tourism Destinations by Average Rating")
plt.xlabel("Destination")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save the chart
plt.savefig("outputs/figures/top_destinations.png", dpi=300)
plt.close()

print("Chart saved to outputs/figures/top_destinations.png")
