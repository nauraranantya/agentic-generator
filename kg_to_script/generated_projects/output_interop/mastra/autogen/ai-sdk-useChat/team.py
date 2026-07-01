"""
Auto-generated AutoGen Team: MastraApplicationSystem
Human Agents:
  - developer_fajar_ekaputra ()
  - developer_kabul_kurniawan ()
Capabilities:
  - get weather capability: Capability to obtain current weather information for a given location (geocoding + weather API calls, returns normalized weather fields).
Resources:
  - city: Trigger input parameter: the city string provided to the workflow (e.g., 'Seattle').
  - weather-forecast: Array of daily forecast objects with the following structure:
[
  {
    date: string,
    maxTemp: number,
    minTemp: number,
    precipitationChance: number,
    condition: string,
    location: string
  },
  ...
]
This resource is the output of the fetch-weather task and the input to the plan-activities task.
  - activities-text: Textual output produced by the planning agent. Format: exact template as specified in planningAgent instructions (per-day headers, WEATHER SUMMARY, MORNING/AFTERNOON/INDOOR sections, SPECIAL CONSIDERATIONS). Typically a single concatenated string assembled from streamed LLM output.
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


def get_weather_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    getweather

    Description:
    Get current weather for a location. Tool accepts an input { location: string } and returns an object containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location.
    """
    return (
        "Tool 'get_weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_weather_tool = FunctionTool(
    get_weather_tool_impl,
    description="""Get current weather for a location. Tool accepts an input { location: string } and returns an object containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location."""
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


planning_agent = AssistantAgent(
    name="planning_agent",
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


# ==================================================
# Human Agents (UserProxy)
# ==================================================

developer_fajar_ekaputra = UserProxyAgent(
    name="developer_fajar_ekaputra",
    description="""""",
)
developer_kabul_kurniawan = UserProxyAgent(
    name="developer_kabul_kurniawan",
    description="""""",
)

