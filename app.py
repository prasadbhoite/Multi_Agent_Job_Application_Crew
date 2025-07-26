import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variable
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.set_page_config(page_title="Gemini Chatbot with Memory", page_icon="🧠")
st.title("💬 Gemini Chatbot with Memory")
