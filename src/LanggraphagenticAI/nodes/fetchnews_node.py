from tavily import TavilyClient
from src.LanggraphagenticAI.State.state import AgentState
from langchain_core.prompts import ChatPromptTemplate
import os

class AInews_node:
    def __init__(self,llm):
        self.tavily_client = TavilyClient(api_key="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")
        self.llm=llm
        self.state={}

    def fetch_news(self, state: dict) -> dict:
        frequency=state["messages"][0].content.lower() 
        frequency_map = {
        "daily": "day",
        "weekly": "week",
        "monthly": "month",
        "yearly": "year"
    }
        time_range = frequency_map.get(frequency)  

        response = self.tavily_client.search(
        query="please share latest news related to Artificial Intelligence",
        topic="news",        # or "news"
        time_range=time_range,      # options: "day", "week", "month", "year"
        days=30,
        max_results=10
    )    
        
        state['news_data']=response.get('results',[])
        self.state['news_data']= state['news_data']
          
        return state
    
    def summarize_news(self, state: dict) -> dict:
        """
        Summarizes news stored in state['news_data'] and stores result in state['news_summary'].
        """
        news_list = self.state['news_data']
        print('News List') 
        print(news_list) 
        news_list  
        
        # Convert the news list into a string
        news_text = "\n".join([
            f"- {article.get('content', '')}: {article.get('url', '')} :{article.get('published_date', '')}" 
            for article in news_list
        ])

        # Create a ChatPromptTemplate
        prompt = ChatPromptTemplate.from_template(
        "You are an AI assistant. Summarize the following AI news articles in Markdown format. "
        "Each item should include the date, title, and a brief summary. "
        "Sort the items so the latest news comes first.\n\n"
        "{news_text}"
        )

        # Initialize the chat model
       

        # Format the prompt
        formatted_prompt = prompt.format_prompt(news_text=news_text).to_messages()

        # Generate summary
        summary =  self.llm.invoke(formatted_prompt)

        # Store the summary in state
        state["news_summary"] = summary.content
        self.state['news_summary']=state["news_summary"]

        return state


    def save_news_summary(self, state: dict) -> dict:
        """
        Saves the summarized news (Markdown) into a .md file.
        The filename is generated dynamically using frequency + current date.
        Stores filename into state['news_filename'].
        """
        summary = self.state['news_summary']

        if not summary:
            summary = "# AI News Summary\n\n_No summary available._"

        # Get frequency from state['messages'][0], default 'weekly'
       
        if "messages" in state and len(state["messages"]) > 0:
            frequency = state["messages"][0].content.lower()

        # Generate dynamic filename
        print(frequency)
        os.makedirs("./AINEWS", exist_ok=True)
        filename = f"./AINEWS/{frequency}_ai_news.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(summary)

        # Store filename back in state
        state["news_filename"] = filename
        return state
