
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


def yc_directory_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    yc_directory_tool

    Description:
    Get data from the 2024 YC directory
    """
    return (
        "Tool 'yc_directory_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


yc_directory_tool = FunctionTool(
    yc_directory_tool_impl,
    description="""Get data from the 2024 YC directory """
)


# ==================================================
# Agents
# ==================================================


yc_directory_agent = AssistantAgent(
    name="yc_directory_agent",
    model_client=model_client,
    system_message="""
Role:
directory

Goal:
directory

Background:
You are a directory.
""",
)



