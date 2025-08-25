from src.LanggraphagenticAI.State.state import AgentState

class chatbot_with_Toolnode:
    def __init__(self,llm):
        self.model=llm

    def process(self, state: AgentState) -> dict:
        return{"messages":self.model.invoke(state["messages"])}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.model.bind_tools(tools)

        def chatbot_node(state: AgentState):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node
