from langchain_groq import ChatGroq
import streamlit as st
  # example LLM class'
import os

class GroqLLM:
    def __init__(self,user_controls):
        # Get the API key from Streamlit session state
       
        self.user_controls=user_controls

    def get_llm_model(self):
        try:
            """Initialize the Groq LLM instance."""
            groq_api_key=self.user_controls["groq_api_key"]
            selected_model=self.user_controls["model"]
            print("DEBUG: model =", selected_model)
            if groq_api_key=="":
                st.error("pPelase add groiq api")
            llm= ChatGroq(api_key=groq_api_key,model=selected_model)
        
        except Exception as e:
            raise ValueError(f"error occured {e}")

        return llm