from crewai import Agent

researcher = Agent(
    role="Senior Research Analyst",

    goal="""
    Gather accurate company information and
    summarize key business insights.
    """,

    backstory="""
    You are an elite market researcher specializing
    in startups, SaaS, and technology companies.
    """,

    llm="gpt-4.1-mini",

    verbose=True
)