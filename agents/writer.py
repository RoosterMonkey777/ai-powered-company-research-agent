from crewai import Agent

writer = Agent(
    role="Executive Report Writer",

    goal="""
    Create polished executive summaries and
    concise company reports.
    """,

    backstory="""
    You write professional investment-grade
    business reports for executives.
    """,

    llm="gpt-4.1-mini",

    verbose=True
)