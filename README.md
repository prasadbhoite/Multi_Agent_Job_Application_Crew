
# 🧠 Multi-Agent Job Application Assistant

This project is a **modular Streamlit app** powered by **CrewAI agents** to assist users with job applications. It uses AI agents to:

- Tailor resumes to job descriptions
- Prepare interview materials
- Extract and process resume content from Markdown and PDF files

---

## 🚀 Features

- ✅ Upload your resume in `.md` or `.pdf` format
- ✅ AI-powered tailoring of your resume
- ✅ Custom interview prep
- ✅ Modular and extensible codebase
- ✅ Built with [CrewAI](https://docs.crewai.com/) for multi-agent orchestration
- ✅ User-friendly interface using [Streamlit](https://streamlit.io)

---

## 📂 Folder Structure

```
multi_agent_job_application_crew/
│
├── streamlit_app.py                # Main Streamlit app
├── requirements.txt
├── README.md
├── output/                         # Stores tailored resume and interview prep
├── src/
│   ├── components/
│   │   ├── agents.py               # Agent definitions
│   │   ├── tools.py                # Custom tools (PDF/MD parsing, etc.)
│   │   └── sidebar.py             # Sidebar input UI
│   └── crew_manager.py            # Crew creation & execution logic
```

---

## 📄 Resume Formats Supported

- Markdown (`.md`)
- PDF (`.pdf`) — Parsed using [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/prasadbhoite/multi_agent_job_application_crew.git
cd multi_agent_job_application_crew
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure to include `pymupdf` in `requirements.txt`:
>
> ```
> -e .
> streamlit
> crewai
> openai
> python-dotenv
> chromadb
> crewai-tools
> pysqlite3-binary
> pymupdf
> ```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 📝 Example Usage

1. Upload your resume (`.md` or `.pdf`)
2. Enter job description and other details in the sidebar
3. Click **"🚀 Run Job Application Crew"**
4. Download your **Tailored Resume** and **Interview Prep**

---

## 🧠 AI Agents Used

You can define multiple specialized agents like:

- **Resume Optimizer**
- **Job-Match Analyst**
- **Interview Coach**

Agents collaborate using CrewAI to produce tailored outputs.

---

## 📦 Deployment

This app can be deployed easily on:

- [Streamlit Cloud](https://streamlit.io/cloud)
- Render, Hugging Face Spaces, or your own server

Ensure you use Python **3.10** for compatibility with `crewai_tools`.

---

## 📜 License

MIT License. Feel free to adapt or extend the app for your own use.

---

## ✨ Credits

Built with ❤️ using [Streamlit](https://streamlit.io), and [CrewAI](https://crewai.com).
