"""
Auto-generated CrewAI Script
Source : AgentO Knowledge Graph
Pipeline: SPARQL extraction + Jinja2 template rendering
"""

from crewai import Agent, Task, Crew
from crewai.tools import tool
import os

# ===========================================================
# Tools
# ===========================================================

@tool('weaviatevectorsearchtool')
def weaviatevectorsearchtool(query: str) -> str:
    """Weaviate Vector Search Tool"""
    return f"[Tool stub: weaviatevectorsearchtool] Executed with input: {query}"


@tool('serperdevtool')
def serperdevtool(query: str) -> str:
    """SerperDev Web Search Tool"""
    return f"[Tool stub: serperdevtool] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

biomedicalmarketingagent = Agent(
    role='Industry researcher focused on biomedical trends and their applications in AI',
    goal='Industry researcher focused on biomedical trends and their applications in AI',
    backstory="""backstory: As a former biomedical product marketer turned AI strategist, you understand the complex language and regulatory landscape of biomedical innovation. With a keen eye on genomics, clinical research, and medical devices, it now leverages LLMs and vector search to explore how Weaviate’s capabilities can streamline scientific discovery and patient-centric campaigns.""",
    verbose=True
)

healthcaremarketingagent = Agent(
    role='AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.',
    goal='AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.',
    backstory="""backstory: Rooted in public health communications, this agent has evolved into a digital health consultant. You focus on how retrieval-augmented generation (RAG), semantic search, and hybrid models can be applied to solve healthcare-specific challenges—from patient triage to clinical support systems.""",
    verbose=True
)

financialmarketingagent = Agent(
    role='Insight analyst exploring innovations in finance, wealth tech, and regulatory tech',
    goal='Insight analyst exploring innovations in finance, wealth tech, and regulatory tech',
    backstory="""backstory: With experience at a fintech startup and a background in capital markets, this agent specializes in using structured + unstructured data to surface insights for analysts and advisors. Now, it’s looking into how vector databases and LLMs can automate tasks like fraud detection, investor personalization, and market research.""",
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

biomedagenttask = Task(
    description="""Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs.""",
    expected_output='Write an industry specific analysis of why this Weaviate feature would be useful for your industry of expertise.',
    agent=biomedicalmarketingagent
)

healthcareagenttask = Task(
    description="""Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs.""",
    expected_output='Write an industry specific analysis of why this Weaviate feature would be useful for your industry of expertise.',
    agent=healthcaremarketingagent
)

financialagenttask = Task(
    description="""Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs.""",
    expected_output='Write an industry specific analysis of why this Weaviate feature would be useful for your industry of expertise.',
    agent=financialmarketingagent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[biomedicalmarketingagent, healthcaremarketingagent, financialmarketingagent],
        tasks=[biomedagenttask, healthcareagenttask, financialagenttask],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
