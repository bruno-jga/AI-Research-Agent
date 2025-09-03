import os
import requests
from config import settings


def get_ai_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "artificial intelligence OR AI OR machine learning",
        "sortBy": "popularity",
        "pageSize": 10,
        "language": "en",
        "apiKey": settings.news_api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["articles"]

(get_ai_news())

