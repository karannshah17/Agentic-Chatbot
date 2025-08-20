from src.LanggraphagenticAI.State.state import AgentState

class chatbot_node:
    def __init__(self,llm):
        self.model=llm

    def process(self, state: AgentState) -> dict:
        return{"messages":self.model.invoke(state["messages"])}


