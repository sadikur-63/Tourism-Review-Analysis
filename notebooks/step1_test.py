
import pandas as pd

print("Tourism Review Analysis Project")

reviews = {
    "country": ["South Korea", "Bangladesh"],
    "review": [
        "Beautiful palace and friendly staff",
        "Amazing beach but transport was difficult"
    ],
    "rating": [5, 3]
}

df = pd.DataFrame(reviews)

print("\nTourism Reviews Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nAverage Rating:")
print(df["rating"].mean())
