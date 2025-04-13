from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Sample text
text = input("Enter Text: ")

# Analyze sentiment
result = sentiment_analyzer(text)
print(result)
