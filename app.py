import streamlit as st
from datetime import datetime

from crewai import Task, Crew

from tools.search_tool import search_company
from tools.rag_tool import (create_vector_store,retrieve_context)

from agents.researcher import researcher
from agents.analyst import analyst
from agents.writer import writer

st.set_page_config(
    page_title="AI Company Research Assistant",
    layout="wide"
)

st.title("AI Company Research Assistant")
st.markdown(
    """
    ### System Architecture

    User Query → Web Search → RAG Pipeline →
    Vector DB → AI Agents → Executive Report
    """
)
st.sidebar.title("About")

st.sidebar.info(
    """
    AI-powered company research assistant
    built with:

    - CrewAI
    - LangChain
    - ChromaDB
    - OpenAI
    - Streamlit
    """
)
st.write(
    "Multi-agent company analysis using "
    "CrewAI + RAG + LangChain"
)

company = st.text_input(
    "Enter a company name",
    placeholder="Google"
)

current_date = datetime.now().strftime("%B %d, %Y")
if st.button("Analyze Company"):

    # --------------------------------
    # STATUS UI
    # --------------------------------

    status = st.status(
        "Running AI workflow...",
        expanded=True
    )

    # web search
    status.write("Searching the web for company data...")

    raw_data = search_company(company)

    with st.expander("Retrieved Web Data"):
        st.write(raw_data[:4000])


    # create vectordb

    status.write("Creating embeddings and vector store...")
    vectordb = create_vector_store(raw_data)

    # retrieve context

    status.write("Retrieving relevant context using RAG...")
    context = retrieve_context(
        vectordb,
        f"""
        Company overview,
        products,
        competitors,
        business model,
        latest news
        for {company}
        """
    )

    # create tasks

    status.write("Creating AI agent tasks...")

    research_task = Task(
        description=f"""
	Today's date is {current_date}.
        Research the company {company}.

        Context:
        {context}

        Your report should include:
        - Company overview
        - Products/services
        - Competitors
        - Recent news
        - Business model
        """,

        expected_output="""
        Detailed research summary
        with structured sections.
        """,

        agent=researcher
    )

    analysis_task = Task(
        description=f"""
	Today's date is {current_date}.
        Analyze the company {company}.

        Context:
        {context}

        Perform a SWOT analysis:
        - Strengths
        - Weaknesses
        - Opportunities
        - Threats/Risks

        Also analyze:
        - Market position
        - Competitive advantages
        """,

        expected_output="""
        Strategic business analysis.
        """,

        agent=analyst
    )

    writing_task = Task(
        description=f"""
        Create a polished executive report
        for {company} using the previous
        research and analysis.

        Make it concise, professional,
        and easy to read.
        """,

        expected_output="""
        Final executive report.
        """,

        agent=writer
    )

    # create crew

    status.write("Initializing AI agents...")

    crew = Crew(
        agents=[
            researcher,
            analyst,
            writer
        ],

        tasks=[
            research_task,
            analysis_task,
            writing_task
        ],

        verbose=True
    )

    # run crew

    status.write("Running multi-agent analysis workflow...")
    result = crew.kickoff()

    # status
    status.update(
        label="Analysis Complete",
        state="complete"
    )

    # diplay

    st.success("Executive Report Generated")
    st.subheader("Final Executive Report")
    st.markdown(result.raw)