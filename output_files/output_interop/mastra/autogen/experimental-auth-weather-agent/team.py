
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
    Get current weather for a location.

Behavior summary:
- Input: { location: string } (city name)
- Execution:
  1. Call geocoding API to resolve location -> latitude, longitude, name.
  2. Call weather API with latitude & longitude to get current and hourly weather.
  3. Map numeric weather_code to human-readable condition (mapping preserved in description).
  4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location.
- Errors: throws when location not found.
    """
    return (
        "Tool 'weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


weather_tool = FunctionTool(
    weather_tool_impl,
    description="""Get current weather for a location.

Behavior summary:
- Input: { location: string } (city name)
- Execution:
  1. Call geocoding API to resolve location -> latitude, longitude, name.
  2. Call weather API with latitude & longitude to get current and hourly weather.
  3. Map numeric weather_code to human-readable condition (mapping preserved in description).
  4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location.
- Errors: throws when location not found."""
)


# ==================================================
# Agents
# ==================================================


weather_agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    system_message="""
Role:
Weather Assistant

Goal:
Weather Assistant

Background:
You are a Weather Assistant.
""",
)



