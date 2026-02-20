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

@tool('websitesearchtool')
def websitesearchtool(query: str) -> str:
    """WebsiteSearchTool"""
    return f"[Tool stub: websitesearchtool] Executed with input: {query}"


@tool('serperdevtool')
def serperdevtool(query: str) -> str:
    """SerperDevTool"""
    return f"[Tool stub: serperdevtool] Executed with input: {query}"


@tool('filereadtool')
def filereadtool(query: str) -> str:
    """FileReadTool"""
    return f"[Tool stub: filereadtool] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

researchagent = Agent(
    role='Research Analyst',
    goal='Analyze the company website and provided description to extract insights on culture, values, and specific needs.',
    backstory="""Expert in analyzing company cultures and identifying key values and needs from various sources, including websites and brief descriptions.""",
    tools=[websitesearchtool, serperdevtool],
    verbose=True
)

writeragent = Agent(
    role='Job Description Writer',
    goal='Use insights from the Research Analyst to create a detailed, engaging, and enticing job posting.',
    backstory="""Skilled in crafting compelling job descriptions that resonate with the company's values and attract the right candidates.""",
    tools=[websitesearchtool, serperdevtool, filereadtool],
    verbose=True
)

reviewagent = Agent(
    role='Review and Editing Specialist',
    goal="""Review the job posting for clarity, engagement, grammatical accuracy, and alignment with company values and refine it to ensure perfection.""",
    backstory="""A meticulous editor with an eye for detail, ensuring every piece of content is clear, engaging, and grammatically perfect.""",
    tools=[websitesearchtool, serperdevtool, filereadtool],
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

researchcompanyculturetask = Task(
    description="""Analyze the provided company website and the hiring manager's company's domain {company_domain},
description {company_description}. Focus on understanding the company's culture, values, and mission.
Identify unique selling points and specific projects or achievements highlighted on the site.
Compile a report summarizing these insights, specifically how they can be leveraged in a job posting
to attract the right candidates.""",
    expected_output="""A comprehensive report detailing the company's culture, values, and mission, along with specific selling
points relevant to the job role. Suggestions on incorporating these insights into the job posting should be included.""",
    agent=researchagent
)

researchrolerequirementstask = Task(
    description="""Based on the hiring manager's needs: {hiring_needs}, identify the key skills, experiences,
and qualities the ideal candidate should possess for the role. Consider the company's current projects,
its competitive landscape, and industry trends. Prepare a list of recommended job requirements
and qualifications that align with the company's needs and values.""",
    expected_output="""A list of recommended skills, experiences, and qualities for the ideal candidate, aligned with
the company's culture, ongoing projects, and the specific role's requirements.""",
    agent=researchagent
)

draftjobpostingtask = Task(
    description="""Draft a job posting for the role described by the hiring manager: {hiring_needs}.
Use the insights on {company_description} to start with a compelling introduction,
followed by a detailed role description, responsibilities, and required skills and qualifications.
Ensure the tone aligns with the company's culture and incorporate any unique benefits or
opportunities offered by the company. Specific benefits: {specific_benefits}.""",
    expected_output='A detailed, engaging job posting (introduction, role, responsibilities, requirements, benefits).',
    agent=writeragent
)

reviewandeditjobpostingtask = Task(
    description="""Review the draft job posting for the role {hiring_needs}. Check for clarity, engagement, grammatical accuracy,
and alignment with the company's culture and values. Edit and refine the content, ensuring it speaks directly
to the desired candidates and accurately reflects the role's unique benefits and opportunities. Provide
feedback for any necessary revisions.""",
    expected_output='A polished, error-free job posting formatted in markdown, plus feedback for improvements.',
    agent=reviewagent
)

industryanalysistask = Task(
    description="""Conduct an in-depth analysis of the industry related to the company's domain {company_domain}.
Investigate current trends, challenges, and opportunities within the industry, utilizing market reports,
recent developments, and expert opinions. Assess how these factors could impact the role being hired
for and the overall attractiveness of the position to potential candidates.
Consider how the company's position within this industry and its response to these trends could be leveraged to attract top talent.
Include in your report how the role contributes to addressing industry challenges or seizing opportunities.""",
    expected_output='A detailed industry analysis report identifying trends, challenges, opportunities and strategic recommendations.',
    agent=researchagent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[researchagent, writeragent, reviewagent],
        tasks=[researchcompanyculturetask, researchrolerequirementstask, draftjobpostingtask, reviewandeditjobpostingtask, industryanalysistask],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
