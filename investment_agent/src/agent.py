import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools import get_stock_price, get_financial_news

load_dotenv()

def get_agent():
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    tools = [get_stock_price, get_financial_news]

    # Simple creation without system prompt arguments
    agent = create_react_agent(llm, tools)
    
    return agent