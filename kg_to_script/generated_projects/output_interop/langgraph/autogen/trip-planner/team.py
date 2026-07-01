
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


def book_accommodation_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    book_accommodation_tool

    Description:
    Tool invoked to create an accommodation booking using provided order details (accommodation, tripDetails). Tool call originates from LangGraph thread.submit messages in the UI.
    """
    return (
        "Tool 'book_accommodation_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


book_accommodation_tool = FunctionTool(
    book_accommodation_tool_impl,
    description="""Tool invoked to create an accommodation booking using provided order details (accommodation, tripDetails). Tool call originates from LangGraph thread.submit messages in the UI. """
)


# ==================================================
# Agents
# ==================================================


trip_planner_agent = AssistantAgent(
    name="trip_planner_agent",
    model_client=model_client,
    system_message="""
Role:
assistant

Goal:
assistant

Background:
Used by the trip planner LLM to format messages and construct tool calls for bookings.
""",
)



