from newsapi_client import get_ai_news
from ai_summarizer import summarize_news
from telegram_client import send_telegram

def run_pipeline():
    print("Fetching news...")
    news_json = get_ai_news()
    
    print("Summarizing...")
    summary = summarize_news(news_json)
    
    print("Sending via WhatsApp...")
    send_telegram(summary)
    print("Done!")

if __name__ == "__main__":
    run_pipeline()
