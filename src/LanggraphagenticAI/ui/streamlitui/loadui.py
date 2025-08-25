
import streamlit as st
import os

from src.LanggraphagenticAI.ui.uiconfigfile import Config 

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def render(self):
        """Render the UI components in Streamlit."""
        st.set_page_config(page_title=self.config.page_title)
        st.title(self.config.page_title)
        st.session_state.IsFetchButtonClicked=False
        self.user_controls["llm"] = st.sidebar.selectbox(
        "LLM Options",
        self.config.llm_options
        )

        self.user_controls["usecase"] = st.sidebar.selectbox(
        "Use Case Options",
        self.config.usecase_options
        )

        self.user_controls["model"] = st.sidebar.selectbox(
        "Groq Model Options",
        self.config.groq_model_options
        )
        self.user_controls["groq_api_key"] =st.session_state["groq_api_key"] =st.sidebar.text_input(
        "Enter API Key / Password",
        type="password"
        )
        
        if self.user_controls["usecase"] == "Chatbot with Tool" or  "AI News":
            self.user_controls["TAVILY_API_KEY"] =os.environ["TAVILY_API_KEY"]= st.session_state["TAVILY_API_KEY"] = st.sidebar.text_input(
            "Tavily API Key",
            type="password"
        )   
            if not self.user_controls["TAVILY_API_KEY"]:
                st.sidebar.warning("⚠️ Tavily API Key is required for 'Chatbot with tool'.")

        if self.user_controls["usecase"] == "AI News":
            st.sidebar.markdown("### AI News Settings")
            time_frame =st.sidebar.selectbox(
            "Select time Frame",
            self.config.AI_NEWS_OPTIONS
            )
            ##self.user_controls["FETCH_NEWS"] = st.sidebar.button("📡 Fetch Latest AI News")
            
                       
            if st.sidebar.button('🔍 Fetch Latest AI News'):
                st.session_state.IsFetchButtonClicked=True
                st.session_state.time_frame=time_frame
                
            

        return self.user_controls
        