# Program to performs sentiment analysis on product reviews.
import os
os.system('cls||clear')

# Load pandas and spacy
import pandas as pd
import spacy
from spacy.tokens import Doc
from textblob import TextBlob
nlp = spacy.load('en_core_web_sm')

'''TextBlob installation wasn't working, and diplayed an error:
AttributeError: [E046] Can't retrieve unregistered extension attribute 
'blob'. Did you forget to call the set_extension method? Hence I
resolved it by finding solution on ChatGPT by getting below code.
ChatGPT conversation provided in separate pdf document. Didn't share the
conversational link as it also had my personal chats'''


# Define a function to get TextBlob polarity for a Doc object
def get_blob_polarity(doc):
    return TextBlob(doc.text).sentiment.polarity


# Function to perform sentiment analysis
def sentiment_analysis(review):
    print(f"\nReview: {review}")
    doc = nlp(review)
    
    # Removing stopwords and punctuations
    filtered_tokens = [token.text for token in doc if not token.is_stop
                       and not token.is_punct]
    cleaned_review = " ".join(filtered_tokens)
    doc = nlp(cleaned_review)
    
    polarity = doc._.blob # Checking polarity using Textblob library
    if polarity > 0:
        sentiment = "Positive"
    elif polarity == 0:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"
    print("Sentiment:", sentiment, "\n")

    
# Register the custom extension attribute 'blob' with spaCy Doc objects
Doc.set_extension("blob", getter=get_blob_polarity, force=True)

# Load product reviews text file
df = pd.read_csv('amazon_product_reviews.csv', delimiter=',', engine='python')
reviews_data = df['reviews.text'].to_frame()

# Preprocess the data
clean_data = reviews_data.dropna(subset=['reviews.text'])
clean_data['reviews.text'] = clean_data['reviews.text'].str.strip()
print(clean_data.head(10))

# Provide reviews for test
user_input = int(input("\nPlease enter a number to select review from " 
                       "the list to test the sentiment:"))
# Passing the selected review
analyzed_sentiment = sentiment_analysis(clean_data.iloc[user_input, 0])

# Perform similarity test between two reviews
my_review_of_choice_1 = nlp(clean_data['reviews.text'][6])
my_review_of_choice_2 = nlp(clean_data['reviews.text'][73])
similarity = my_review_of_choice_1.similarity(my_review_of_choice_2)
print(f"\nSimilarity between these two reviews is: {similarity}\n")
print(clean_data['reviews.text'][22], "\n")
print(clean_data['reviews.text'][103], "\n")