import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def summarize_news(articles):
    titles_and_desc = "\n".join(
        [f"- {a['title']}: {a.get('description','')}" for a in articles]
    )
    
    prompt = ChatPromptTemplate.from_template(
        """You are an assistant that summarizes AI news.
        Given the following articles, create a concise, friendly digest 
        in natural language (max ~200 words).
        
        Articles:
        {articles}
        
        Now write the digest:
        """
    )
    
    chain = prompt | llm
    result = chain.invoke({"articles": titles_and_desc})
    return result.content
