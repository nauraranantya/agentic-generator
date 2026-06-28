"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : 
Objectives:
  - : 
Human Agents:
  - admin ()
Resources:
  - : Historic prices and metadata for Nvidia (NVDA) covering the past month. Intended to be retrieved via Python code. Source and retrieval instructions preserved in CodeArtifact description.
  - : Artifact produced by Engineer: Python scripts to retrieve NVDA historic prices, compute monthly performance metrics, and produce serialized outputs (csv, json, plots). Implementation details intentionally captured as a high-level description (no SDK-specific code insertion in ontology).
  - : Results produced by Executor after running CodeArtifact: computed performance metrics, figures, and any data files used by Writer to compose the blog.
  - : Draft blog post in markdown format produced by Writer based on execution results. Contains title, textual analysis of stock performance, and optionally code-derived figures. Writer instructed to use pseudo ```md``` code block for content.
  - : Blog draft refined by Writer after Admin (user_proxy) provides comments. Final deliverable of workflow.
"""

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.agents import UserProxyAgent

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


def coding_environment_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    coding_environment_tool

    Description:
    Conceptual tool representing the environment used by Executor to run code. Config captured as key/value on Config individual.
    """
    return (
        "Tool 'coding_environment_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


coding_environment_tool = FunctionTool(
    coding_environment_tool_impl,
    description="Conceptual tool representing the environment used by Executor to run code. Config captured as key/value on Config individual."
)


# ==================================================
# Agents
# ==================================================


planner_agent = AssistantAgent(
    name="planner_agent",
    model_client=model_client,
    system_message="""
Role:
Planner

Goal:
Planner

Background:
Planner. Given a task, determine what information is needed to complete the task. After each step is done by others, check the progress and instruct the remaining steps
""",
)


engineer_agent = AssistantAgent(
    name="engineer_agent",
    model_client=model_client,
    system_message="""
Role:
Engineer

Goal:
Engineer

Background:
Engineer: writes code per planner's plan
""",
)


executor_agent = AssistantAgent(
    name="executor_agent",
    model_client=model_client,
    system_message="""
Role:
Executor

Goal:
Executor

Background:
Executor: execute code and return execution results (no human input).
""",
)


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=model_client,
    system_message="""
Role:
Writer

Goal:
Writer

Background:
Writer: write blogs based on the code execution results and take feedback from the admin to refine the blog.
""",
)


# ==================================================
# Human Agents (UserProxy)
# ==================================================

admin = UserProxyAgent(
    name="admin",
    description="",
)

