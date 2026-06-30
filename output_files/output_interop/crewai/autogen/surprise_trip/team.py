"""
Auto-generated AutoGen Team: SurpriseTravelCrew
Goals:
  - Goal: personalized activity planner: Research and find cool things to do at the destination, including activities and events that match the traveler's interests and age group
  - Goal: restaurant scout: Find highly-rated restaurants and dining experiences at the destination, and recommend scenic locations and fun activities
  - Goal: itinerary compiler: Compile all researched information into a comprehensive day-by-day itinerary, ensuring the integration of flights and hotel information
Objectives:
  - : Produce a per-day list of recommended activities and events including details and suitability rationale.
  - : Produce recommended restaurants and scenic locations with ratings and descriptions for each relevant day.
  - : Produce a single integrated itinerary document that schedules flights, hotel, day plans, activities and restaurants.
Resources:
  - Itinerary_Instance: Pydantic output schema named Itinerary:
- name: string (funny name for itinerary)
- day_plans: List[DayPlan], each DayPlan:
    - date: string
    - activities: List[Activity], each Activity:
        - name: string
        - location: string
        - description: string
        - date: string
        - cousine: string
        - why_its_suitable: string
        - reviews: Optional[List[str]]
        - rating: Optional[float]
    - restaurants: List[str]
    - flight: Optional[str]
- hotel: string
This resource is the output_json schema referenced by itinerary_compilation_task.
  - ExampleRunInputs: Example runtime inputs used in main.run and train():
    {
      'origin': 'São Paulo, GRU',
      'destination': 'New York, JFK',
      'age': 31,
      'hotel_location': 'Brooklyn',
      'flight_information': 'GOL 1234, leaving at June 30th, 2024, 10:00',
      'trip_duration': '14 days'
    }
    This is a sample input bundle used for kickoff/train in the repository.
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


def serper_dev_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SerperDevTool

    Description:
    Search / web tools used to query the web (as configured in the source crew).
    """
    return (
        "Tool 'serper_dev_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


serper_dev_tool = FunctionTool(
    serper_dev_tool_impl,
    description="""Search / web tools used to query the web (as configured in the source crew)."""
)


def scrape_website_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ScrapeWebsiteTool

    Description:
    Tool to scrape website content; used by agents for gathering reviews and details.
    """
    return (
        "Tool 'scrape_website_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


scrape_website_tool = FunctionTool(
    scrape_website_tool_impl,
    description="""Tool to scrape website content; used by agents for gathering reviews and details."""
)


def my_custom_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    MyCustomTool

    Description:
    Example custom tool present in source (tools/custom_tool.py). This example tool is included in the repository but commented-out in crew agent configuration and not used by default.
    """
    return (
        "Tool 'my_custom_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


my_custom_tool = FunctionTool(
    my_custom_tool_impl,
    description="""Example custom tool present in source (tools/custom_tool.py). This example tool is included in the repository but commented-out in crew agent configuration and not used by default."""
)


# ==================================================
# Agents
# ==================================================


personalized_activity_planner = AssistantAgent(
    name="personalized_activity_planner",
    model_client=model_client,
    system_message="""
Role:
Activity Planner

Goal:
Research and find cool things to do at the destination, including activities and events that match the traveler's interests and age group

Background:
Use internet search tools and recommendation engines to gather information; produce day-by-day activities with name, location, description and suitability rationale.
""",
)


restaurant_scout = AssistantAgent(
    name="restaurant_scout",
    model_client=model_client,
    system_message="""
Role:
Restaurant Scout

Goal:
Find highly-rated restaurants and dining experiences at the destination, and recommend scenic locations and fun activities

Background:
Use internet search tools, restaurant review sites, and travel guides to find restaurants and scenic locations aligned with traveler preferences.
""",
)


itinerary_compiler = AssistantAgent(
    name="itinerary_compiler",
    model_client=model_client,
    system_message="""
Role:
Itinerary Compiler

Goal:
Compile all researched information into a comprehensive day-by-day itinerary, ensuring the integration of flights and hotel information

Background:
Compile all researched information into a comprehensive day-by-day itinerary for the trip; ensure integration of flights, hotel information, activities, and restaurants. Use text formatting and document creation tools.
""",
)



