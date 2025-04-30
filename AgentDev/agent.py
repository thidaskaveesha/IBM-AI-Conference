# Connect to mcp 
from mcp import StdioServerParameters

## LLM Agent Capabilities 
from smolagent import ToolCallingAgent, ToolCollection, LiteLLMModel

# LLM Model
llm = LiteLLMModel(model_id="ollama_chat/gpt-3.5-turbo", 
                   api_base="http://localhost:11434", 
                   num_ctx=8192
)

# MCP connection params
server_params = StdioServerParameters(
    command='uv',
    args=['run', "server.py"],
    enviorment = None
)

# Connect to the MCP server and run the agent
with ToolCollection.from_mcp(server_params, trust_remote_code= True) as tool_collection : 
    agent = ToolCallingAgent(
        model =llm,
        tools = [*tool_collection.tools]
    )
    agent.run("What is IBM Stock Price?")
    print(agent.response) # Print the response from the agent
