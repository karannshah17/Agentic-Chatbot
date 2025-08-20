
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

        return self.user_controls
        