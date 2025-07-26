### ✅ 2. src/crew_manager.py

from crewai import Crew
from src.components.agents import build_agents
from src.components.tasks import build_tasks

def run_job_application_crew(inputs, resume_path="./fake_resume.md"):
    agents = build_agents(resume_path)
    tasks = build_tasks(agents, inputs)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )
    result = crew.kickoff(inputs=inputs)
    return result
