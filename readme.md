\# Multi-Agent AI Research Analyst



A multi-agent AI company research assistant built using CrewAI, LangChain, ChromaDB, and OpenAI.



\## Features



\- Multi-agent orchestration with CrewAI

\- Retrieval-Augmented Generation (RAG)

\- Vector database using ChromaDB

\- Web search integration with Tavily

\- AI-generated executive reports

\- Streamlit frontend



\---



\## Architecture



User Query

↓

Web Search Tool

↓

RAG Pipeline

↓

Vector Database

↓

Research Agent

↓

Analysis Agent

↓

Writer Agent

↓

Executive Report



\---



\## Example Workflow



1\. User enters company name

2\. System searches web for company information

3\. Data is chunked and embedded

4\. ChromaDB stores semantic vectors

5\. AI agents analyze retrieved context

6\. Final executive report is generated



\---



\## Installation



```bash

pip install -r requirements.txt

```



Create a `.env` file:



```env

OPENAI\_API\_KEY=your\_key

TAVILY\_API\_KEY=your\_key

```



Run app:



```bash

streamlit run app.py

```



\---



\## Demo



Add screenshots or demo video here.



