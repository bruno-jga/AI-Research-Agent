# AI News 

AI News is a Python-based automation tool that fetches the latest **Artificial Intelligence news**, summarizes it with an LLM, and sends you a **daily digest on Telegram**.

---

## 📌 Features
- Fetches top 10 most popular AI-related articles from **NewsAPI**  
- Summarizes news into a short natural-language digest using **OpenAI LLMs**  
- Sends daily updates to **Telegram** (via your bot)  
- Runs automatically on a schedule (via APScheduler)  
- Modular design

---

## 📂 Project Structure
```
ai-news-agent/  
│── config.py             # loads environment variables  
├── settings.py           # loads environment variables  
├── newsapi_client.py     # fetch news from NewsAPI  
├── ai_summarizer.py      # summarize JSON with LLM  
├── telegram_client.py    # send messages via Telegram  
├── scheduler.py          # daily scheduled job  
├── main.py               # orchestrates pipeline  
│── requirements.txt  
│── README.md  
```

---

## ⚙️ Setup

### 1. Clone the repository
```
git clone https://github.com/yourusername/ai-news-agent.git
cd ai-news-agent
```

### 2. Create a virtual environment

```
python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
.venv\Scripts\activate      # on Windows
````

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create .env file

Add your API keys and IDs:
```
NEWSAPI_KEY=your_newsapi_key
OPENAI_API_KEY=your_openai_key
TELEGRAM_TOKEN=1234567890:AA...
TELEGRAM_CHAT_ID=987654321
```

## Getting Your Telegram Chat ID
1. Create a bot with @BotFather and get your bot token.

2. Start a chat with your bot in Telegram.

3. Send a message to the bot.

4. Visit https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates and copy the ```"chat":{"id": ... }``` value.

5. Use this ID as TELEGRAM_CHAT_ID in your ```.env```.


## Usage

Run once:
```
python scheduler.py
```
