import asyncio

from team import (
    city_selection_agent,
    local_expert_agent,
    travel_concierge_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "origin":
        "",


    "cities":
        "",


    "range":
        "",


    "interests":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: identify_task
        # Workflow Edge: identify_task -> gather_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: identify_task")
        print("=" * 80)

        task_prompt = """Analyze and select the best city for the trip 
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
Traveler Interests: {interests}"""
        # Execute via the assigned agent: city_selection_agent
        result = await city_selection_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: gather_task
        # Workflow Edge: gather_task -> plan_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: gather_task")
        print("=" * 80)

        task_prompt = """As a local expert on this city you must compile an 
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
Traveler Interests: {interests}"""
        # Execute via the assigned agent: local_expert_agent
        result = await local_expert_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: plan_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: plan_task")
        print("=" * 80)

        task_prompt = """Expand this guide into a full 7-day travel 
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
Traveler Interests: {interests}"""
        # Execute via the assigned agent: travel_concierge_agent
        result = await travel_concierge_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        print("\n" + "=" * 80)
        print("DONE")
        print("=" * 80)

    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR")
        print("=" * 80)
        print(type(e).__name__)
        print(str(e))



if __name__ == "__main__":
    asyncio.run(main())