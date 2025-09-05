import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from config import Settings

openai_api_key=Settings.openai_api_key

llm = ChatOpenAI(model="gpt-5-nano-2025-08-07", temperature=0, api_key=openai_api_key)

def summarize_news(articles):
    titles_and_desc = "\n".join(
        [f"- {a['title']}: {a.get('description','')}" for a in articles]
    )
    
    prompt = ChatPromptTemplate.from_template(
        """You are an assistant that summarizes AI news.
        Given the following articles, create a concise, friendly digest 
        in natural language (max ~300 words).
        
        Articles:
        {articles}
        
        Now write the digest:
        """
    )
    
    chain = prompt | llm
    result = chain.invoke({"articles": titles_and_desc})
    return result.content
