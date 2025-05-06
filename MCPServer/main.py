# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("HelloWorld")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.

    Args:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: The sum of the two input numbers.
    """
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Generates a personalized greeting for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A personalized greeting in the format 'Hello, {name}!'.
    """
    return f"Hello, {name}!"
