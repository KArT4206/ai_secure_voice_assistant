from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        return f"Sentiment analysis failed: {str(e)}"
