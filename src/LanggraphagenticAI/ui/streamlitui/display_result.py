import streamlit as st
from langchain_core.messages import HumanMessage,ToolMessage,AIMessage
import json


class displayyREsultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase=usecase
        self.graph=graph 
        self.usermessage=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.usermessage
        if usecase=="Basic Chatbot":
             for event in graph.stream({"messages": ("user",user_message)}):
                
                for value in event.values():
                    
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
                
            
        elif usecase == "Chatbot with Tool":
            with st.chat_message("user"):
                        st.write(user_message)
            placeholder = st.empty()
            messages_list = []  
            #initial_state= {"messages":[user_message]}
            for event in graph.stream({"messages": [("user", user_message)]}): 
                
                for node_name, node_data in event.items():
                     if node_name == "chatbot":
                        #st.write(node_data["messages"])
                        if "messages" in node_data:
                            for m in node_data["messages"]: 
                                 ##placeholder.markdown(m.content,unsafe_allow_html=True)
                                 if m.content != '':
                                    messages_list.append(m.content)
                                    styled_messages = ""
                                    for msg in messages_list:
                                        styled_messages += f"""
                                        <div style="
                                            background-color:#f0f2f6; 
                                            border-radius:15px; 
                                            padding:10px; 
                                            margin:5px 0;
                                            max-width:100%;
                                        ">
                                            🤖 {msg}
                                        </div>
                                        """
                                        placeholder.markdown(styled_messages, unsafe_allow_html=True)
            
            # Build styled HTML for chat
                                
                                
                                # Display all messages with styles
                                

            


            # Display assistant/tool response
           
        elif usecase == "AI News":
            frequency = self.usermessage
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_ai_news.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()
                    #{frequency}_ai_news.md
                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
    
