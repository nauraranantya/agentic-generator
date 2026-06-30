"""
Auto-generated AutoGen Team: TravelAISystemMastraexampleapp
Goals:
  - Plan Trip: 
  - Format Output: 
Objectives:
  - Assemble trip components: 
Capabilities:
  - Find Flights: Capability to search and select flight options.
  - Find Hotels: Capability to search and select hotels.
  - Find Attractions: Capability to search and select attractions.
  - Search Airbnb: Capability to search airbnb locations and listings.
  - Analyze Travel Results: Capability to analyze raw agent search outputs and reformat into application schema.
Resources:
  - outboundFlight (Flight object): Domain Flight object produced by searchFlights: includes airline, flightNumber, departure/arrival airports/cities/times, duration, price, legs.
  - returnFlight (Flight object): Return flight object (same structure as outbound).
  - accommodation (Hotel or Airbnb listing): Hotel or Airbnb domain object with fields: name, rating, pricePerNight or price, images, location, address, description, amenities.
  - attractions (list of Attraction): Array of Attraction items recommended for trip.
  - Formatted travel plan (travelSchema): Final application JSON matching travelSchema with flights.outbound, flights.return, accommodation, attractions.
"""

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


def search_flights_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    GetFlightInfosearchFlights

    Description:
    Fetches flight information for a given date range, origin and destination. Origin and Destination are Airport codes like DFW.AIRPORT or SEA.AIRPORT
    """
    return (
        "Tool 'search_flights_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_flights_tool = FunctionTool(
    search_flights_tool_impl,
    description="""Fetches flight information for a given date range, origin and destination. Origin and Destination are Airport codes like DFW.AIRPORT or SEA.AIRPORT"""
)


def search_hotels_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchHotelssearchHotels

    Description:
    Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'search_hotels_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_hotels_tool = FunctionTool(
    search_hotels_tool_impl,
    description="""Searches for hotels in a specified location. Destination is a cityId like 20015732 for 20015733"""
)


def search_attractions_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchAttractionssearchAttractions

    Description:
    Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'search_attractions_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_attractions_tool = FunctionTool(
    search_attractions_tool_impl,
    description="""Searches for attractions in a specified location. Destination is a cityId like 20015732 for 20015733"""
)


def search_airbnb_location_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchAirbnbLocationsearchAirbnbLocation

    Description:
    Searches for Airbnb places in a specified location. Place is a city name like New York, NY
    """
    return (
        "Tool 'search_airbnb_location_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_airbnb_location_tool = FunctionTool(
    search_airbnb_location_tool_impl,
    description="""Searches for Airbnb places in a specified location. Place is a city name like New York, NY"""
)


def search_airbnb_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchAirbnbsearchAirbnb

    Description:
    Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733
    """
    return (
        "Tool 'search_airbnb_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_airbnb_tool = FunctionTool(
    search_airbnb_tool_impl,
    description="""Searches for Airbnb in a specified location. Place is a cityId like 20015732 for 20015733"""
)


# ==================================================
# Agents
# ==================================================


travel_agent = AssistantAgent(
    name="travel_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
Agent-level instruction used on agent initialization
""",
)


travel_analyzer = AssistantAgent(
    name="travel_analyzer",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
Analyzer agent base instructions.
""",
)



