
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


def my_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    my_tool

    Description:
    My tool description
    """
    return (
        "Tool 'my_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


my_tool = FunctionTool(
    my_tool_impl,
    description="""My tool description """
)


# ==================================================
# Agents
# ==================================================


chef_agent = AssistantAgent(
    name="chef_agent",
    model_client=model_client,
    system_message="""
Role:
Chef

Goal:
Chef

Background:
You are a Chef.
""",
)



