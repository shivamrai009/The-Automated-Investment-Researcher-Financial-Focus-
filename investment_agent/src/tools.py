import yfinance as yf
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Tool for getting stock price data
def get_stock_price(ticker: str):
    """
    Fetches the current stock price and basic info for a given ticker symbol (e.g., AAPL, TSLA).
    """
    try:
        stock = yf.Ticker(ticker)
        # Get fast info
        info = stock.fast_info
        # Get last close price if current is unavailable
        price = info.last_price
        
        return f"The current price of {ticker} is ${price:.2f}."
    except Exception as e:
        return f"Error fetching price for {ticker}: {str(e)}"

# 2. Tool for getting financial news
def get_financial_news(query: str):
    """
    Searches for the latest financial news about a company or market trend.
    """
    search = DuckDuckGoSearchRun()
    return search.run(query)