
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


def tool_extract_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_extract

    Description:
    Tool name: "extract"
Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM.
Schema (Zod, represented informally):
{
  location: string (describe: The location to plan the trip for. Can be a city, state, or country.),
  startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),
  endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),
  numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.)
}
Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.
    """
    return (
        "Tool 'tool_extract' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_extract = FunctionTool(
    tool_extract_impl,
    description="""Tool name: "extract"
Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM.
Schema (Zod, represented informally):
{
  location: string (describe: The location to plan the trip for. Can be a city, state, or country.),
  startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),
  endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),
  numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.)
}
Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location."""
)


def tool_classify_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_classify

    Description:
    Tool name: "classify"
Purpose: Classify whether trip details remain relevant to the user's most recent request.
Schema:
{
  isRelevant: boolean (describe: Whether the trip details are still relevant to the user's request.)
}
Notes: When invoked, tool_choice is set to "classify" in the implementation.
    """
    return (
        "Tool 'tool_classify' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_classify = FunctionTool(
    tool_classify_impl,
    description="""Tool name: "classify"
Purpose: Classify whether trip details remain relevant to the user's most recent request.
Schema:
{
  isRelevant: boolean (describe: Whether the trip details are still relevant to the user's request.)
}
Notes: When invoked, tool_choice is set to "classify" in the implementation."""
)


def tool_list_accommodations_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_list_accommodations

    Description:
    Tool name: "list-accommodations"
Purpose: A tool to list accommodations for the user. Implementation populates an accommodations list (id, name, price, rating, city, image) using a data generator.
Schema: {} (no input schema fields required in the implementation).
Produces: An accommodations list resource used to populate UI.
    """
    return (
        "Tool 'tool_list_accommodations' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_list_accommodations = FunctionTool(
    tool_list_accommodations_impl,
    description="""Tool name: "list-accommodations"
Purpose: A tool to list accommodations for the user. Implementation populates an accommodations list (id, name, price, rating, city, image) using a data generator.
Schema: {} (no input schema fields required in the implementation).
Produces: An accommodations list resource used to populate UI."""
)


def tool_list_restaurants_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_list_restaurants

    Description:
    Tool name: "list-restaurants"
Purpose: A tool to list restaurants for the user. Implementation uses trip details to produce a restaurants list.
Schema: {}.
Produces: A restaurants list resource used to populate UI.
    """
    return (
        "Tool 'tool_list_restaurants' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_list_restaurants = FunctionTool(
    tool_list_restaurants_impl,
    description="""Tool name: "list-restaurants"
Purpose: A tool to list restaurants for the user. Implementation uses trip details to produce a restaurants list.
Schema: {}.
Produces: A restaurants list resource used to populate UI."""
)


# ==================================================
# Agents
# ==================================================


trip_planner_agent = AssistantAgent(
    name="trip_planner_agent",
    model_client=model_client,
    system_message="""
Role:
assistant / trip-planner

Goal:
assistant / trip-planner

Background:
You are a assistant / trip-planner.
""",
)



