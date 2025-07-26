### ✅ 1. streamlit_app.py
# Handle SQLite for ChromaDB
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except (ImportError, KeyError):
    pass



import streamlit as st
import os
from src.components.sidebar import render_sidebar
from src.crew_manager import run_job_application_crew

st.set_page_config(page_title="Job Application CrewAI", layout="wide")
st.title("🧠 Multi-Agent Job Application Assistant")

# Render sidebar and input fields
config, inputs = render_sidebar()

# Resume Upload
resume_file = st.file_uploader("📎 Upload your Resume (Markdown only)", type=["md"])
if resume_file:
    resume_path = f"output/{resume_file.name}"
    with open(resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    inputs["resume_path"] = resume_path

# Run Crew
if st.button("🚀 Run Job Application Crew"):
    with st.status("Running CrewAI Agents...", expanded=True):
        result = run_job_application_crew(inputs, resume_path=inputs.get("resume_path", "./fake_resume.md"))
        st.success("🎯 All tasks completed!")

        st.markdown("## 📝 Results")
        st.markdown(result)

        if os.path.exists("output/tailored_resume.md"):
            with open("output/tailored_resume.md", "r") as f:
                st.download_button("📄 Download Tailored Resume", f.read(), file_name="tailored_resume.md")

        if os.path.exists("output/interview_materials.md"):
            with open("output/interview_materials.md", "r") as f:
                st.download_button("🎤 Download Interview Prep", f.read(), file_name="interview_materials.md")
