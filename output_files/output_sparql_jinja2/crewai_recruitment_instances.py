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

@tool('tool_serperdev')
def tool_serperdev(query: str) -> str:
    """SerperDevTool"""
    return f"[Tool stub: tool_serperdev] Executed with input: {query}"


@tool('tool_scrapewebsite')
def tool_scrapewebsite(query: str) -> str:
    """ScrapeWebsiteTool"""
    return f"[Tool stub: tool_scrapewebsite] Executed with input: {query}"


@tool('tool_linkedin')
def tool_linkedin(query: str) -> str:
    """Retrieve LinkedIn profiles"""
    return f"[Tool stub: tool_linkedin] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

agent_researcher = Agent(
    role='Job Candidate Researcher',
    goal="""Find potential candidates for the job specified in inputs (job_requirements). Use multiple public resources to assemble candidate brief profiles and contact info.""",
    backstory='Job Candidate Researcher',
    tools=[tool_serperdev, tool_scrapewebsite, tool_linkedin],
    verbose=True
)

agent_matcher = Agent(
    role='Candidate Matcher and Scorer',
    goal='Evaluate candidates relative to the job_requirements, compute scores and rank candidates with justifications.',
    backstory='Candidate Matcher and Scorer',
    tools=[tool_serperdev, tool_scrapewebsite],
    verbose=True
)

agent_communicator = Agent(
    role='Candidate Outreach Strategist',
    goal='Produce outreach methods and message templates tailored to prioritized candidates.',
    backstory='Candidate Outreach Strategist',
    tools=[tool_serperdev, tool_scrapewebsite],
    verbose=True
)

agent_reporter = Agent(
    role='Candidate Reporting Specialist',
    goal="""Assemble a concise report for recruiters with profiles, scores, and outreach plan; follow output formatting instruction from tasks configuration.""",
    backstory='Candidate Reporting Specialist',
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

task_research_candidates = Task(
    description="""Conduct thorough research to find potential candidates for the specified job.
Utilize various online resources and databases to gather a comprehensive list of potential candidates.
Ensure that the candidates meet the job requirements provided.

Job Requirements:
{job_requirements}""",
    expected_output='A list of 10 potential candidates with their contact information and brief profiles highlighting their suitability.',
    agent=agent_researcher
)

task_match_and_score = Task(
    description="""Evaluate and match the candidates to the best job positions based on their qualifications and suitability.
Score each candidate to reflect their alignment with the job requirements, ensuring a fair and transparent assessment process.
Don't try to scrape people's linkedin, since you don't have access to it.

Job Requirements:
{job_requirements}""",
    expected_output='A ranked list of candidates with detailed scores and justifications for each job position.',
    agent=agent_matcher
)

task_outreach_strategy = Task(
    description="""Develop a comprehensive strategy to reach out to the selected candidates.
Create effective outreach methods and templates that can engage the candidates and encourage them to consider the job opportunity.

Job Requirements:
{job_requirements}""",
    expected_output="""A detailed list of outreach methods and templates ready for implementation, including communication strategies and engagement tactics.""",
    agent=agent_communicator
)

task_report_candidates = Task(
    description="""Compile a comprehensive report for recruiters on the best candidates to put forward.
Summarize the findings from the previous tasks and provide clear recommendations based on the job requirements.""",
    expected_output="""A detailed report with the best candidates to pursue, no need to include the job requirements formatted as markdown without '```', including profiles, scores, and outreach strategies.""",
    agent=agent_reporter
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[agent_researcher, agent_matcher, agent_communicator, agent_reporter],
        tasks=[task_research_candidates, task_match_and_score, task_outreach_strategy, task_report_candidates],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
