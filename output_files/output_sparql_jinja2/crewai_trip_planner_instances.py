"""
Auto-generated CrewAI Script
Source : AgentO Knowledge Graph
Pipeline: SPARQL extraction + Jinja2 template rendering
"""

from crewai import Agent, Task, Crew
from crewai.tools import tool
import os

# ===========================================================
# Tools
# ===========================================================

@tool('searchtools')
def searchtools(query: str) -> str:
    """SearchTools"""
    return f"[Tool stub: searchtools] Executed with input: {query}"


@tool('browsertools')
def browsertools(query: str) -> str:
    """BrowserTools"""
    return f"[Tool stub: browsertools] Executed with input: {query}"


@tool('calculatortools')
def calculatortools(query: str) -> str:
    """CalculatorTools"""
    return f"[Tool stub: calculatortools] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

cityselectionagent = Agent(
    role='City Selection Expert',
    goal='Select the best city based on weather patterns, seasonal events, and travel costs',
    backstory='An expert in analyzing travel data to pick ideal destinations',
    tools=[searchtools, browsertools],
    verbose=True
)

localexpertagent = Agent(
    role='Local Expert at this city',
    goal='Provide in-depth local guide content, hidden gems, and practical tips.',
    backstory="A knowledgeable local guide with extensive information about the city, it's attractions and customs",
    tools=[searchtools, browsertools],
    verbose=True
)

travelconciergeagent = Agent(
    role='Amazing Travel Concierge',
    goal='Create a 7-day travel itinerary with detailed daily plans, budgets, packing suggestions, and logistics.',
    backstory='Specialist in travel planning and logistics with decades of experience',
    tools=[searchtools, browsertools, calculatortools],
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

identifytask = Task(
    description="""Analyze and select the best city for the trip 
based on specific criteria such as weather patterns, seasonal
events, and travel costs. This task involves comparing
multiple cities, considering factors like current weather
conditions, upcoming cultural or seasonal events, and
overall travel expenses. 

Your final answer must be a detailed
report on the chosen city, and everything you found out
about it, including the actual flight costs, weather 
forecast and attractions.
If you do your BEST WORK, I'll tip you $100!

Traveling from: {origin}
City Options: {cities}
Trip Date: {range}
Traveler Interests: {interests}""",
    expected_output='Detailed report on the chosen city including flight costs, weather forecast, and attractions',
    agent=cityselectionagent
)

gathertask = Task(
    description="""As a local expert on this city you must compile an 
in-depth guide for someone traveling there and wanting 
to have THE BEST trip ever!
Gather information about key attractions, local customs,
special events, and daily activity recommendations.
Find the best spots to go to, the kind of place only a
local would know.
This guide should provide a thorough overview of what 
the city has to offer, including hidden gems, cultural
hotspots, must-visit landmarks, weather forecasts, and
high level costs.

The final answer must be a comprehensive city guide, 
rich in cultural insights and practical tips, 
tailored to enhance the travel experience.
If you do your BEST WORK, I'll tip you $100!

Trip Date: {range}
Traveling from: {origin}
Traveler Interests: {interests}""",
    expected_output='Comprehensive city guide including hidden gems, cultural hotspots, and practical travel tips',
    agent=localexpertagent
)

plantask = Task(
    description="""Expand this guide into a full 7-day travel 
itinerary with detailed per-day plans, including 
weather forecasts, places to eat, packing suggestions, 
and a budget breakdown.

You MUST suggest actual places to visit, actual hotels 
to stay and actual restaurants to go to.

This itinerary should cover all aspects of the trip, 
from arrival to departure, integrating the city guide
information with practical travel logistics.

Your final answer MUST be a complete expanded travel plan,
formatted as markdown, encompassing a daily schedule,
anticipated weather conditions, recommended clothing and
items to pack, and a detailed budget, ensuring THE BEST
TRIP EVER. Be specific and give it a reason why you picked
each place, what makes them special! If you do your BEST WORK, I'll tip you $100!

Trip Date: {range}
Traveling from: {origin}
Traveler Interests: {interests}""",
    expected_output='Complete expanded travel plan with daily schedule, weather conditions, packing suggestions, and budget breakdown',
    agent=travelconciergeagent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[cityselectionagent, localexpertagent, travelconciergeagent],
        tasks=[identifytask, gathertask, plantask],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
