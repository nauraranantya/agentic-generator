
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


def tool_search_flights_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_search_flights

    Description:
    Fetches flight information for a given date range, origin and destination. Origin and Destination are Airport codes like DFW.AIRPORT or SEA.AIRPORT
    """
    return (
        "Tool 'tool_search_flights' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_flights = FunctionTool(
    tool_search_flights_impl,
    description="""Fetches flight information for a given date range, origin and destination. Origin and Destination are Airport codes like DFW.AIRPORT or SEA.AIRPORT """
)


def tool_search_hotels_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_search_hotels

    Description:
    Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'tool_search_hotels' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_hotels = FunctionTool(
    tool_search_hotels_impl,
    description="""Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733 """
)


def tool_search_attractions_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_search_attractions

    Description:
    Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'tool_search_attractions' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_attractions = FunctionTool(
    tool_search_attractions_impl,
    description="""Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733 """
)


def tool_search_airbnb_location_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_search_airbnb_location

    Description:
    Searches for Airbnb places in a specified location. Place is a city name like New York, NY
    """
    return (
        "Tool 'tool_search_airbnb_location' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_airbnb_location = FunctionTool(
    tool_search_airbnb_location_impl,
    description="""Searches for Airbnb places in a specified location. Place is a city name like New York, NY """
)


def tool_search_airbnb_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_search_airbnb

    Description:
    Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'tool_search_airbnb' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_airbnb = FunctionTool(
    tool_search_airbnb_impl,
    description="""Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733 """
)


# ==================================================
# Agents
# ==================================================


travel_agent = AssistantAgent(
    name="travel_agent",
    model_client=model_client,
    system_message="""
Role:
travel agent

Goal:
travel agent

Background:
You are a travel agent.
""",
)


travel_analyzer = AssistantAgent(
    name="travel_analyzer",
    model_client=model_client,
    system_message="""
Role:
travel analyzer

Goal:
travel analyzer

Background:
You are a travel analyzer.
""",
)



