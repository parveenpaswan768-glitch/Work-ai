import streamlit as st

st.title("My AI Chat App")

user = st.text_input("Ask something")

if user:
    st.write("You asked:", user)
    st.write("AI Answer: Hello, I am your AI assistant!")
