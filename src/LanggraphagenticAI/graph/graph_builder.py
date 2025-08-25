from langgraph.graph import StateGraph,START,END
from src.LanggraphagenticAI.State.state import AgentState
from src.LanggraphagenticAI.nodes.chatbot_node import chatbot_node
from src.LanggraphagenticAI.nodes.chatbot_with_tool import  chatbot_with_Toolnode
from src.LanggraphagenticAI.nodes.fetchnews_node import AInews_node
from src.LanggraphagenticAI.tools.tavily_search import tavily_search,create_tool_node
from langgraph.prebuilt import ToolNode,tools_condition

class GraphBuilder:
    def __init__(self, llm_instance):
        self.llm = llm_instance        
        self.graph = StateGraph(AgentState)
    
    def basic_chatnpt_build(self):
        self.chatbot_node =chatbot_node(self.llm) 
        self.graph.add_node("chatbot", self.chatbot_node.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
    
    def chatbot_with_tool(self):
        
        tools=tavily_search()
        tool_node=create_tool_node(tools=tools)
        self.chatbot_node_tool =chatbot_with_Toolnode(self.llm) 
        
        
        self.graph.add_node("chatbot", self.chatbot_node_tool.create_chatbot(tools=tools))
        self.graph.add_node("tools", tool_node)

        self.graph.add_edge(START,"chatbot")
        self.graph.add_conditional_edges("chatbot",tools_condition)
        self.graph.add_edge("tools","chatbot")

    def ai_news_summariser(self):
        self.ai_news_node = AInews_node(self.llm)
        self.graph.add_node("fetchnews", self.ai_news_node.fetch_news)
        self.graph.add_node("summarisenews", self.ai_news_node.summarize_news)
        self.graph.add_node("saveresult", self.ai_news_node.save_news_summary)


        self.graph.add_edge(START,"fetchnews")
        self.graph.add_edge("fetchnews","summarisenews")
        self.graph.add_edge("summarisenews","saveresult")
        self.graph.add_edge("saveresult",END)

    
    
    def setup_graph(self,usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatnpt_build()
        if usecase == "Chatbot with Tool":
            self.chatbot_with_tool()
        if usecase == "AI News":
            self.ai_news_summariser()

        return self.graph.compile()
