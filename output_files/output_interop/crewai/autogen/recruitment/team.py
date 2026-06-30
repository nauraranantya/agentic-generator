"""
Auto-generated AutoGen Team: RecruitmentCrew
Goals:
  - Find potential candidates for the job: Find potential candidates for the job specified in inputs (job_requirements). Use multiple public resources to assemble candidate brief profiles and contact info.
  - Match the candidates to the best jobs and score them: Evaluate candidates relative to the job_requirements, compute scores and rank candidates with justifications.
  - Develop outreach strategies for the selected candidates: Produce outreach methods and message templates tailored to prioritized candidates.
  - Report the best candidates to the recruiters: Assemble a concise report for recruiters with profiles, scores, and outreach plan; follow output formatting instruction from tasks configuration.
Objectives:
  - Find and report best candidates for a job opening: Coordinate research, matching/scoring, outreach strategy, and reporting to produce a ranked and actionable list of candidates for a given job requirement input.
Capabilities:
  - candidate_research: Search public data sources and extract candidate basic profile information.
  - candidate_matching_and_scoring: Evaluate candidates against job requirements and produce a numeric or ordinal score and justification.
  - outreach_strategy_development: Design outreach approaches and generate template messages for contacting candidates.
  - candidate_reporting: Compose recruiter-facing reports summarizing findings, scores and outreach strategies.
  - search_api: 
  - web_scraping: 
  - retrieve_linkedin_profiles: 
Resources:
  - candidates_raw_list: Raw list of found candidate profiles and their basic contact/profile information produced by research_candidates_task.
  - candidates_scored: Candidates evaluated and scored by match_and_score_candidates_task; contains scores and justifications.
  - outreach_plan: Outreach methods and message templates produced by outreach_strategy_task.
  - final_report_for_recruiters: Compiled report produced by report_candidates_task with recommended candidates, scores, and outreach templates.
"""

from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


def tool_serperdev_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SerperDevTool

    Description:
    Search / knowledge tool (SerperDev) used by agents for web search or knowledge lookups.
    """
    return (
        "Tool 'tool_serperdev' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_serperdev = FunctionTool(
    tool_serperdev_impl,
    description="""Search / knowledge tool (SerperDev) used by agents for web search or knowledge lookups."""
)


def tool_scrapewebsite_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ScrapeWebsiteTool

    Description:
    General web scraping tool used to extract structured information from web pages.
    """
    return (
        "Tool 'tool_scrapewebsite' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_scrapewebsite = FunctionTool(
    tool_scrapewebsite_impl,
    description="""General web scraping tool used to extract structured information from web pages."""
)


def tool_linkedin_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    RetrieveLinkedInprofiles

    Description:
    Retrieve LinkedIn profiles given a list of skills. Input is a comma-separated list of skills. Returns candidate name, position, location, and profile link. Implemented via a web client that navigates LinkedIn search and extracts entries (requires a LinkedIn session cookie in environment).
    """
    return (
        "Tool 'tool_linkedin' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_linkedin = FunctionTool(
    tool_linkedin_impl,
    description="""Retrieve LinkedIn profiles given a list of skills. Input is a comma-separated list of skills. Returns candidate name, position, location, and profile link. Implemented via a web client that navigates LinkedIn search and extracts entries (requires a LinkedIn session cookie in environment)."""
)


# ==================================================
# Agents
# ==================================================


researcher = AssistantAgent(
    name="researcher",
    model_client=model_client,
    system_message="""
Role:
Job Candidate Researcher

Goal:
Find potential candidates for the job specified in inputs (job_requirements). Use multiple public resources to assemble candidate brief profiles and contact info.

Background:
Agent-level base instruction for researcher.
""",
)


matcher = AssistantAgent(
    name="matcher",
    model_client=model_client,
    system_message="""
Role:
Candidate Matcher and Scorer

Goal:
Evaluate candidates relative to the job_requirements, compute scores and rank candidates with justifications.

Background:
Agent-level base instruction for matcher.
""",
)


communicator = AssistantAgent(
    name="communicator",
    model_client=model_client,
    system_message="""
Role:
Candidate Outreach Strategist

Goal:
Produce outreach methods and message templates tailored to prioritized candidates.

Background:
Agent-level base instruction for communicator.
""",
)


reporter = AssistantAgent(
    name="reporter",
    model_client=model_client,
    system_message="""
Role:
Candidate Reporting Specialist

Goal:
Assemble a concise report for recruiters with profiles, scores, and outreach plan; follow output formatting instruction from tasks configuration.

Background:
Agent-level base instruction for reporter.
""",
)



