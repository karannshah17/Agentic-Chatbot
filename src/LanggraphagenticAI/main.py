import dis
from signal import raise_signal
from sys import exception
import streamlit as st
from src.LanggraphagenticAI.LLMs.groqllm import GroqLLM
from src.LanggraphagenticAI.graph.graph_builder import GraphBuilder
from src.LanggraphagenticAI.ui.streamlitui.loadui import LoadStreamlitUI
from src.LanggraphagenticAI.ui.streamlitui.display_result import displayyREsultStreamlit

def load_agentic_ai_app():
    """
    Load and run streamlit applciation with Streamlite UI
    """
    ui = LoadStreamlitUI()
    user_input=ui.render()

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.time_frame 
    else :
        user_message = st.chat_input("Enter your message:")


    if user_message:
        try:
            obj_llm=GroqLLM(user_controls=user_input)
            model=obj_llm.get_llm_model()
            if not model:
                st.error("reerror in model") 
            

            usecase=user_input.get("usecase")
            print("DEBUG: model =", model)
            
            graph_buil=GraphBuilder(model)
            print("DEBUG: graph_builder =", graph_buil)
            try:
                graph=graph_buil.setup_graph(usecase)
                displayyREsultStreamlit(usecase=usecase,graph=graph,user_message=user_message).display_result_on_ui()
            except Exception as e :
                st.error(f"Hry errors generating graph{e}")
                return

        
        except Exception as e:
            st.error(f"gr errors generating graph{e}")
            return
            
