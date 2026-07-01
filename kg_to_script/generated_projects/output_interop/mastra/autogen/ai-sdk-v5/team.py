
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


def get_weather_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    getweather

    Description:
    Get current weather for a location
    """
    return (
        "Tool 'get_weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_weather_tool = FunctionTool(
    get_weather_tool_impl,
    description="""Get current weather for a location"""
)


# ==================================================
# Agents
# ==================================================


weather_agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    system_message="""
Role:
Weather assistant

Goal:
Weather assistant

Background:
You are a Weather assistant.
""",
)



team = RoundRobinGroupChat(
    participants=[
        weather_agent,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Task to fetch current weather for a specified location. Implemented by invoking the 'get-weather' tool. The agent will ask the user for a location if not provided.

Expected Output:
Completed: fetch_current_weather


Task:
A provenance-style record that the agent participates in the fetch current weather task.

Expected Output:
Completed: weather_agent_participation_placeholder

"""
