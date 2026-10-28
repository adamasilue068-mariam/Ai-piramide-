import streamlit as st,google.generativeai as g
k=st.sidebar.text_input("API", type="password")
if q:=st.chat_input("Question"): g.configure(api_key=k); st.write(g.GenerativeModel("gemini-1.5-flash").generate_content(q).text)
                                                                  
                                                                  
                                                                
