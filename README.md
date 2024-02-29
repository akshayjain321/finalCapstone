# Project Name: NLP Applications - Sentiment Analysis

## Description:
This program performs sentiment analysis on the product review selected by the user
The data is read from Amazon product reviews from the CSV file 'amazon_product_reviews.csv'.
It is then pre-processed before performing the sentiment analysis operation.
Lastly, semantic similarity is performed between the two selected reviews

## Installation Section

### Prerequisites
Python 3.6 or newer
pip (Python package installer)

### Clone the Repository
First, clone the project repository to your local machine. Open your terminal and run:
git clone https://github.com/yourusername/yourprojectname.git

### Install all the required packages using pip. The project requires pandas, spaCy, TextBlob, and additional resources for spaCy.
pip install pandas spacy textblob
python -m textblob.download_corpora
python -m spacy download en_core_web_sm

### Running the Program
python sentiment_analysis.py

## Usage Section
This section explains how to use the sentiment analysis program to analyze product reviews and determine their sentiment (Positive, Neutral, Negative).

### Running the Sentiment Analysis
Start the Program:
With your environment setup and dependencies installed, start the program by running:
python sentiment_analysis.py

### Input Selection:
The program will prompt you to enter a number corresponding to the review you wish to analyze from the preloaded dataset. Enter a valid number to proceed. For example:
Please enter a number to select a review from the list to test the sentiment: 5

### View the Analysis:
After entering your selection, the program will display the selected review, perform sentiment analysis, and output the sentiment result:
Review: [The review text...]
Sentiment: Positive

### Understanding the Output
Review: This is the text of the review that was analyzed.
Sentiment: The output sentiment can be one of three types:
  Positive: The review has a positive sentiment.
  Neutral: The review is neither positive nor negative.
  Negative: The review has a negative sentiment.

## Credits: 
This program has been created by Akshay Jain
