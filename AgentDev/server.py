# MCP Server
# Import libaries 
# pip install fastmcp yfinance uv
import yfinance as yf
from colorama import Fore

# MCP Dependencies 
from mcp.server.fastmcp import FastMCP

# Instantiate the MCP server
mcp = FastMCP('yfinanceServer')

# Wrap the server with a tool decorator
# This allows the server to be used as a tool in the MCP framework 
@mcp.tool()
# Define the function to get stock data
def get_stock_data(stock_ticker: str) -> str:
    """
    This tool returns the stock data for a given stock ticker.
    :param stock_ticker: The stock ticker symbol (e.g., 'AAPL' for Apple)
    :return: A string containing the latest data or an error message.
    """
    try:
        # Get stock data using yfinance and add it into the data varible 
        data = yf.Ticker(stock_ticker)
        # Get the stock prices for the last month
        prices = data.history(period='1mo')
        # Get the last price from the data
        print(Fore.GREEN + f"Stock prices for {stock_ticker} is {prices['High']}" + Fore.RESET)
        # Return the High price as a string
        return str(f"Stock prices for ${stock_ticker} is ${prices['High']}")
    except Exception as e:
        return {'error': str(e)}

# Run the server
if __name__ == '__main__':
    mcp.run(transport="stdio")

# uv run mcp dev server.py