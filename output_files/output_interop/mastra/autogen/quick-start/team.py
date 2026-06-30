
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


def console_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    console_tool

    Description:
    Represents the runtime logging facility used by the step (the source prints to console via console.log). Modeled as a Tool to indicate the step uses an execution tool.
    """
    return (
        "Tool 'console_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


console_tool = FunctionTool(
    console_tool_impl,
    description="""Represents the runtime logging facility used by the step (the source prints to console via console.log). Modeled as a Tool to indicate the step uses an execution tool."""
)


# ==================================================
# Agents
# ==================================================


cat_one = AssistantAgent(
    name="cat_one",
    model_client=model_client,
    system_message="""
Role:
feline expert

Goal:
feline expert

Background:
Default agent-level instructions to guide behavior when the agent is asked about cat species. This prompt is intended to be used by the agent as its core persona/instructions.
""",
)



