from crewai import Agent
from crewai_tools import FileReadTool, ScrapeWebsiteTool, MDXSearchTool, SerperDevTool

def build_agents(resume_path):
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    read_resume = FileReadTool(file_path=resume_path)
    semantic_search_resume = MDXSearchTool(mdx=resume_path)

    researcher = Agent(
        role="Tech Job Researcher",
        goal="Analyze job postings to identify essential qualifications",
        tools=[scrape_tool, search_tool],
        verbose=True,
        backstory=(
            "You're an expert at extracting meaningful information from job descriptions."
        )
    )

    profiler = Agent(
        role="Personal Profiler",
        goal="Create a detailed candidate profile",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory="You compile deep profiles from resumes, GitHub, and write-ups."
    )

    resume_strategist = Agent(
        role="Resume Strategist",
        goal="Tailor the resume to job requirements",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory="You ensure resumes align with job needs and highlight strengths."
    )

    interview_preparer = Agent(
        role="Interview Coach",
        goal="Generate interview prep materials",
        tools=[scrape_tool, search_tool, read_resume, semantic_search_resume],
        verbose=True,
        backstory="You prepare candidates with Q&A that reflect their resume and job."
    )

    return {
        "researcher": researcher,
        "profiler": profiler,
        "resume_strategist": resume_strategist,
        "interview_preparer": interview_preparer
    }
