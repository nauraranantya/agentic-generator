
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


def tool_get_cat_facts_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_get_cat_facts

    Description:
    Fetches cat facts
    """
    return (
        "Tool 'tool_get_cat_facts' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_get_cat_facts = FunctionTool(
    tool_get_cat_facts_impl,
    description="""Fetches cat facts """
)


# ==================================================
# Agents
# ==================================================


cat_one = AssistantAgent(
    name="cat_one",
    model_client=model_client,
    system_message="""
Role:
feline-expert

Goal:
feline-expert

Background:
You are a feline-expert.
""",
)



