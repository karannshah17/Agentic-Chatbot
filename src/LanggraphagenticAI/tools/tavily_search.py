from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def tavily_search(max_results: int = 2):
    tools = [TavilySearchResults(max_results=max_results)]
    return tools

def create_tool_node(tools):
    return ToolNode(tools=tools)