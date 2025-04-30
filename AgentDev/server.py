# MCP Server
# Import libaries 
# pip install fastmcp yfinance uv

import yfinance as yf
from colorama import Fore

# MCP Dependencies 
from mcp.server.fastmcp import FastMCP

# Instantiate the MCP server
mcp = FastMCP('yfinanceServer')

# Wrap the server with a decorator to handle exceptions

@mcp.tool()
def get_stock_data(stock_ticker: str) -> str:
    """
    This tool returns the stock data for a given stock ticker.
    :param stock_ticker: The stock ticker symbol (e.g., 'AAPL' for Apple)
    :return: A string containing the latest data or an error message.
    """
    try:
        # Fetch stock data using yfinance
        data = yf.Ticker(stock_ticker)
        prices = data.history(period='1mo')
        print(Fore.GREEN + f"Stock prices for {stock_ticker} is {prices['High']}" + Fore.RESET)
        return str(f"Stock prices for ${stock_ticker} is ${prices['High']}")
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    mcp.run(transport="stdio")