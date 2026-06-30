"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Top-level goal: identify and rank job opportunities for a given CV.
Objectives:
  - : Objective for producing a structured summary of the given CV.
  - : Objective for producing a ranked list of job matches for the candidate.
Resources:
  - : CV markdown file provided as input
  - : CSV file listing job opportunities
  - : Structured summary of the CV produced by read_cv_task; includes Professional Summary, Technical Skills, Work History, Education, Key Achievements.
  - : A ranked list of job opportunities that best match the CV, produced by match_cv_task; includes Job Title, Match Score, Key Matching Points.
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


def file_read_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    file_read_tool

    Description:
    Tool used to read file contents (used by cv_reader and matcher).
    """
    return (
        "Tool 'file_read_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


file_read_tool = FunctionTool(
    file_read_tool_impl,
    description="""Tool used to read file contents (used by cv_reader and matcher)."""
)


def csv_search_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    csv_search_tool

    Description:
    Tool used to search and parse CSV job listings (used by matcher).
    """
    return (
        "Tool 'csv_search_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


csv_search_tool = FunctionTool(
    csv_search_tool_impl,
    description="""Tool used to search and parse CSV job listings (used by matcher)."""
)


def my_custom_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    my_custom_tool

    Description:
    Custom tool implemented at src/match_to_proposal/tools/job_db_connect.py. Placeholder for an external DB connector. Implementation-specific behavior not modeled.
    """
    return (
        "Tool 'my_custom_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


my_custom_tool = FunctionTool(
    my_custom_tool_impl,
    description="""Custom tool implemented at src/match_to_proposal/tools/job_db_connect.py. Placeholder for an external DB connector. Implementation-specific behavior not modeled."""
)


# ==================================================
# Agents
# ==================================================


cv_reader = AssistantAgent(
    name="cv_reader",
    model_client=model_client,
    system_message="""
Role:
CV Reader

Goal:
CV Reader

Background:
Agent-level prompt to orient behavior. Use FileReadTool to access CV file. Produce a structured CV summary.
""",
)


matcher = AssistantAgent(
    name="matcher",
    model_client=model_client,
    system_message="""
Role:
Matcher

Goal:
Matcher

Background:
Agent-level prompt to orient behavior. Use CSVSearchTool and FileReadTool to access jobs CSV and CV summary.
""",
)



