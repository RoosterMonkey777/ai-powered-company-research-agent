from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_company(company_name):

    response = client.search(
        query=f"{company_name} company overview latest news competitors",
        search_depth="advanced",
        max_results=5
    )

    results = []

    for r in response["results"]:
        results.append(r["content"])

    return "\n".join(results)