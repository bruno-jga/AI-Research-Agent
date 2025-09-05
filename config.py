import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    news_api_key=os.getenv("NEWS_API_KEY")
    openai_api_key=os.getenv("OPENAI_API_KEY")
    telegram_token=os.getenv("TELEGRAM_TOKEN")
    telegram_chat_id=os.getenv("TELEGRAM_CHAT_ID")

settings = Settings()