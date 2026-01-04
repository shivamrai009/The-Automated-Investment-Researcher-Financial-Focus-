import streamlit as st
import yfinance as yf
import pandas as pd
from agent import get_agent

st.set_page_config(page_title="AI Investment Researcher", page_icon="📈", layout="wide")

st.title("📈 AI Investment Researcher")
st.markdown("Enter a company name or ticker to generate a research report.")

# User Input
ticker = st.text_input("Ticker Symbol (e.g., NVDA, TSLA, AAPL):").upper()

if st.button("Analyze Stock"):
    if ticker:
        # Create two tabs
        tab1, tab2 = st.tabs(["🤖 AI Report", "📊 Price Chart"])

        # TAB 1: AI Agent Report
        with tab1:
            with st.spinner(f"Agent is researching {ticker}..."):
                try:
                    agent = get_agent()
                    
                    # 1. Define the System Persona here
                    system_instruction = (
                        "You are a Senior Investment Analyst. "
                        "You have access to tools for finding stock prices and news. "
                        "1. ALWAYS use the 'Get Stock Price' tool first. "
                        "2. THEN use the 'Search Financial News' tool to find reasons for the price movement. "
                        "3. Finally, answer the user's question with a recommendation (Buy/Sell/Hold)."
                    )
                    
                    # 2. Define the User Query
                    user_query = f"Analyze {ticker} and give me a recommendation."
                    
                    # 3. Pass both to the agent
                    # LangGraph accepts a list of tuples: ("role", "content")
                    messages = [
                        ("system", system_instruction), 
                        ("user", user_query)
                    ]
                    
                    result = agent.invoke({"messages": messages})
                    
                    # 4. Display the Final Answer
                    final_answer = result["messages"][-1].content
                    st.markdown(final_answer)
                    
                except Exception as e:
                    st.error(f"Error: {e}")

        # TAB 2: Stock Price Chart
        with tab2:
            st.subheader(f"{ticker} - 1 Year Price History")
            try:
                # Fetch 1 year of data
                data = yf.download(ticker, period="1y", progress=False)
                
                # Plot the "Close" price
                if not data.empty:
                    # Handle multi-index columns if yfinance returns them
                    if isinstance(data.columns, pd.MultiIndex):
                        data = data['Close']
                    st.line_chart(data)
                else:
                    st.warning("No price data found.")
            except Exception as e:
                st.error(f"Could not load chart: {e}")

    else:
        st.warning("Please enter a ticker symbol.")