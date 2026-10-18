
# Tourism Review Analysis

A Python data-analysis project exploring tourism reviews,
destination ratings, and visitor sentiment.

## Features

- Load tourism review data
- Analyze destination ratings
- Summarize positive, negative, and neutral sentiment
- Generate charts and CSV summaries

## Project Structure

- `data/raw/` — downloaded datasets
- `src/` — Python scripts
- `outputs/figures/` — generated charts
- `outputs/tables/` — summary tables
- `report/` — project report

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Analysis

```bash
python src/download_data.py
python src/analyze_reviews.py
python src/analyze_sentiment.py
python src/visualize_reviews.py
```

## Outputs

- `outputs/destination_ratings.csv`
- `outputs/tables/sentiment_counts.csv`
- `outputs/figures/top_destinations.png`
- `outputs/figures/sentiment_distribution.png`

## Results and Visualizations

### Sentiment Distribution
![Sentiment Distribution](outputs/figures/sentiment_distribution.png)

### Top-Rated Destinations
![Top-Rated Destinations](outputs/figures/top_destinations.png)

## Project Report
See [Project Report](report/project_report.md) for the methodology,
findings, limitations, and conclusion.

  
