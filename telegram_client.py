import os
import requests
from config import Settings

telegram_token = Settings.telegram_token
telegram_chat_id=Settings.telegram_chat_id


def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        "chat_id": telegram_chat_id,
        "text": message,
        "parse_mode": "Markdown",  # optional: supports Markdown/HTML formatting
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


