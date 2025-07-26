from crewai import Task

def build_tasks(agents, inputs):
    research_task = Task(
        description=(
            f"Analyze job posting URL: {inputs['job_posting_url']} and extract job requirements."
        ),
        expected_output="Structured list of required skills and qualifications.",
        agent=agents['researcher'],
        async_execution=True
    )

    profile_task = Task(
        description=(
            f"Create a profile using GitHub: {inputs['github_url']} and write-up: {inputs['personal_writeup']}"
        ),
        expected_output="Comprehensive professional profile with skills and experiences.",
        agent=agents['profiler'],
        async_execution=True
    )

    resume_task = Task(
        description="Tailor the resume to match the job and profile.",
        expected_output="Updated resume aligned with job needs.",
        output_file="output/tailored_resume.md",
        agent=agents['resume_strategist'],
        context=[research_task, profile_task]
    )

    interview_task = Task(
        description="Generate potential interview questions and talking points.",
        expected_output="List of questions and discussion topics.",
        output_file="output/interview_materials.md",
        agent=agents['interview_preparer'],
        context=[research_task, profile_task, resume_task]
    )

    return [research_task, profile_task, resume_task, interview_task]
