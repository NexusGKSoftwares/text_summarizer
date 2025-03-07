from models.summarizer import TextSummarizer

summarizer = TextSummarizer()

def abstractive_summary(text):
    return summarizer.summarize(text)
