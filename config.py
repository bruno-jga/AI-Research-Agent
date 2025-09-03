import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    news_api_key=os.getenv("NEWS_API_KEY")

settings = Settings()