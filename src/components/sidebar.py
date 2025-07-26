import streamlit as st
import os

def render_sidebar():
    with st.sidebar:
        st.header("🔧 Configuration")
        openai_api = st.text_input("OpenAI API Key", type="password")
        serper_api = st.text_input("Serper API Key", type="password")
        if openai_api:
            os.environ["OPENAI_API_KEY"] = openai_api
        if serper_api:
            os.environ["SERPER_API_KEY"] = serper_api

        st.markdown("### 📋 Job Info")
        job_posting_url = st.text_input("Job Posting URL")
        github_url = st.text_input("GitHub Profile URL")
        personal_writeup = st.text_area("Personal Summary (Short Bio)", height=100)

    config = {"openai": openai_api, "serper": serper_api}
    inputs = {
        "job_posting_url": job_posting_url,
        "github_url": github_url,
        "personal_writeup": personal_writeup
    }
    return config, inputs
