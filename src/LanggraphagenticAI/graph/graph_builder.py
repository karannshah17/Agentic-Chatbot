from langgraph.graph import StateGraph,START,END
from src.LanggraphagenticAI.State.state import AgentState
from src.LanggraphagenticAI.nodes.chatbot_node import chatbot_node

class GraphBuilder:
    def __init__(self, llm_instance):
        self.llm = llm_instance        
        self.graph = StateGraph(AgentState)
    
    def basic_chatnpt_build(self):
        self.chatbot_node =chatbot_node(self.llm) 
        self.graph.add_node("chatbot", self.chatbot_node.process)
        self.graph.add_edge(START,"chatbot")
        self.graph.add_edge("chatbot",END)
      
    
    def setup_graph(self,usecase:str):
        if usecase == "Basic Chatbot":
            self.basic_chatnpt_build()

        return self.graph.compile()
