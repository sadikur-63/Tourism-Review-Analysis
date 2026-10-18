
# Tourism Review Analysis Project

## 1. Introduction

Tourism reviews provide useful information about visitor experiences,
destination ratings, and satisfaction. This project analyzes tourism
review data to identify highly rated destinations and understand
the sentiment expressed in visitor reviews.

## 2. Project Objectives

- Analyze ratings across tourism destinations.
- Identify destinations with high average ratings.
- Examine positive, negative, and neutral review labels.
- Visualize the results using charts.
- Summarize findings that may help tourism stakeholders understand
  visitor feedback.

## 3. Dataset

The project uses a Sri Lankan tourism review dataset obtained
through the Hugging Face Datasets library.

The dataset includes fields such as destination name, rating,
review title, review text, and sentiment.

A total of 16,156 reviews were included in the reported
sentiment counts.

## 4. Methodology

Python and pandas were used to load and analyze the dataset.

The analysis included:
- Inspecting dataset dimensions and columns.
- Checking missing values and rating ranges.
- Calculating average ratings by destination.
- Counting sentiment labels.
- Creating charts with Matplotlib.
- Saving summaries and visualizations in the outputs folder.

## 5. Sentiment Analysis Results

The sentiment labels were distributed as follows:

| Sentiment | Number of Reviews | Percentage |
|---|---:|---:|
| Positive | 13,041 | 80.72% |
| Negative | 1,602 | 9.92% |
| Neutral | 1,513 | 9.36% |
| Total | 16,156 | 100% |

Positive reviews represent the largest category in this dataset.

## 6. Destination Rating Results

The highest-rated destination observed in the analysis was
Bundala National Park, with an average rating of approximately
4.70 out of 5 across 189 reviews.

Other highly rated destinations included:
- Udawalawe National Park
- Community Tsunami Museum
- Sigiriya The Ancient Rock Fortress
- Handunugoda Tea Estate

These results describe the analyzed dataset and do not
necessarily represent every visitor's experience.

## 7. Visualizations

The project generated the following charts:

1. `outputs/figures/top_destinations.png`
   - Compares average ratings across destinations.

2. `outputs/figures/sentiment_distribution.png`
   - Displays the distribution of review sentiment labels.

## 8. Limitations

- The dataset focuses on Sri Lankan tourism rather than destinations
  worldwide.
- The analysis depends on the accuracy and representativeness of
  the available reviews.
- The sentiment categories were already present in the dataset;
  this project did not independently train a sentiment classifier.
- Destinations with different numbers of reviews may not be directly
  comparable based only on average ratings.

## 9. Conclusion

This project demonstrates how Python can be used to analyze tourism
reviews, compare destination ratings, summarize sentiment labels,
and visualize visitor feedback.

Most reviews in the analyzed dataset were labeled positive.
The destination rating analysis also identified several locations
with high average ratings.

Future improvements could include more rigorous data cleaning,
statistical comparisons, and independent validation of sentiment
classification.

## 10. Tools Used

- Python
- pandas
- Matplotlib
- Hugging Face Datasets
- Ubuntu terminal
