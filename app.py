import streamlit as st
from config import setup_page, load_data, get_ai_model
from ai_engine import get_ai_response

st.title("⚡ Pakistan Electricity Data Chatbot")
st.write("Welcome! I am your AI assistant specialized in analyzing Pakistan's household electricity data. "
         "You can ask me about consumption trends, power outages, and how different factors "
         "like income level or city location affect energy usage.")

# Sidebar Configuration
st.sidebar.header("Configuration")

# 1. API Key Input Box
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

# 2. Link placed directly below the API Key box
st.sidebar.markdown("[Get your Gemini API Key here](https://aistudio.google.com/app/apikey)")

# Data Loading
try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Chat Logic
if api_key:
    try:
        model = get_ai_model(api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Process input
        if prompt := st.chat_input("Ask about electricity consumption or outages..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing..."):
                    response = get_ai_response(model, df, prompt)
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
    except Exception as e:
        st.error(f"Error initializing AI: {e}")
else:
    st.info("👈 Please enter your Gemini API key in the sidebar to begin.")