
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


def weather_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    getweather

    Description:
    Tool to get current weather for a location. Wraps geocoding and open-meteo APIs and returns a simplified weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location).
    """
    return (
        "Tool 'weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


weather_tool = FunctionTool(
    weather_tool_impl,
    description="""Tool to get current weather for a location. Wraps geocoding and open-meteo APIs and returns a simplified weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location)."""
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


weather_explainer_agent = AssistantAgent(
    name="weather_explainer_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)



