import streamlit as st
import pandas as pd
import google.generativeai as genai

def setup_page():
    st.set_page_config(page_title="Electricity Data Chatbot", page_icon="⚡")

@st.cache_data
def load_data():
    # Updated to absolute path on E drive using a raw string 'r'
   return pd.read_csv(r"E:\data\pakistan_household_electricity.csv.csv")

def get_ai_model(api_key):
    genai.configure(api_key=api_key)
    
    # DYNAMIC MODEL SELECTION
    # This script searches for the first model available to your key
    # that supports 'generateContent'
    available_models = [
        m for m in genai.list_models() 
        if 'generateContent' in m.supported_generation_methods
    ]
    
    if not available_models:
        raise Exception("No models found that support generateContent with this API key.")
    
    # Use the first valid model found
    selected_model_name = available_models[0].name
    return genai.GenerativeModel(selected_model_name)