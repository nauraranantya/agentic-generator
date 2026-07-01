
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


def tool_get_weather_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_get_weather

    Description:
    Get current weather for a location
    """
    return (
        "Tool 'tool_get_weather' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_get_weather = FunctionTool(
    tool_get_weather_impl,
    description="""Get current weather for a location """
)


# ==================================================
# Agents
# ==================================================


weather_agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    system_message="""
Role:
weather assistant

Goal:
weather assistant

Background:
You are a weather assistant.
""",
)



