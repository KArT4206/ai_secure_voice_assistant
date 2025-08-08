from transformers import pipeline

# Load summarization model once at import
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    try:
        if len(text.split()) < 20:
            return "Text too short to summarize."

        summary = summarizer(text, max_length=80, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Summarization failed: {str(e)}"
