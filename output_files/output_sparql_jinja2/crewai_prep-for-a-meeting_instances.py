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

@tool('exasearchtool')
def exasearchtool(query: str) -> str:
    """ExaSearchTool"""
    return f"[Tool stub: exasearchtool] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

researcheragent = Agent(
    role='Research Specialist',
    goal='Conduct thorough research on people and companies involved in the meeting',
    backstory='Agent: researcher_agent_1',
    tools=[exasearchtool],
    verbose=True
)

industryanalystagent = Agent(
    role='Industry Analyst',
    goal='Analyze the current industry trends, challenges, and opportunities relevant to the meeting context',
    backstory='Agent: industry_analyst_agent_1',
    tools=[exasearchtool],
    verbose=True
)

meetingstrategyagent = Agent(
    role='Meeting Strategy Advisor',
    goal='Develop talking points, questions, and strategic angles for the meeting',
    backstory='Agent: meeting_strategy_agent_1',
    tools=[exasearchtool],
    verbose=True
)

briefingcoordinatoragent = Agent(
    role='Briefing Coordinator',
    goal='Compile research, analysis, and strategy into a concise briefing document',
    backstory='Agent: briefing_coordinator_agent_1',
    tools=[exasearchtool],
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

task_research = Task(
    description="""Conduct comprehensive research on each of the individuals and companies
involved in the upcoming meeting. Gather information on recent
news, achievements, professional background, and any relevant
business activities.

Participants: {participants}
Meeting Context: {context}

Note: asynchronous execution requested in source (async_execution=True).""",
    expected_output="""A detailed report summarizing key findings about each participant
and company, highlighting information that could be relevant for the meeting.""",
    agent=researcheragent
)

task_industryanalysis = Task(
    description="""Analyze the current industry trends, challenges, and opportunities
relevant to the meeting's context. Consider market reports, recent
developments, and expert opinions to provide a comprehensive
overview of the industry landscape.

Participants: {participants}
Meeting Context: {context}

Note: asynchronous execution requested in source (async_execution=True).""",
    expected_output="""An insightful analysis that identifies major trends, potential
challenges, and strategic opportunities.""",
    agent=industryanalystagent
)

task_meetingstrategy = Task(
    description="""Develop strategic talking points, questions, and discussion angles
for the meeting based on the research and industry analysis conducted.

Meeting Context: {context}
Meeting Objective: {objective}

Note: This task's context in the source is set to [research, industry_analysis], i.e., it depends on outputs from Task_Research and Task_IndustryAnalysis.""",
    expected_output="""Complete report with a list of key talking points, strategic questions
to ask to help achieve the meeting's objective during the meeting.""",
    agent=meetingstrategyagent
)

task_summaryandbriefing = Task(
    description="""Compile all the research findings, industry analysis, and strategic
talking points into a concise, comprehensive briefing document for
the meeting.
Ensure the briefing is easy to digest and equips the meeting
participants with all necessary information and strategies.

Meeting Context: {context}
Meeting Objective: {objective}

Note: This task's context in the source is set to [research, industry_analysis, meeting_strategy], i.e., depends on prior task outputs.""",
    expected_output="""A well-structured briefing document that includes sections for
participant bios, industry overview, talking points, and
strategic recommendations.""",
    agent=briefingcoordinatoragent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[researcheragent, industryanalystagent, meetingstrategyagent, briefingcoordinatoragent],
        tasks=[task_research, task_industryanalysis, task_meetingstrategy, task_summaryandbriefing],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
