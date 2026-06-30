import asyncio

from team import (
    personalized_activity_planner,
    restaurant_scout,
    itinerary_compiler,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "destination":
        "",


    "origin":
        "",


    "age":
        "",


    "hotel_location":
        "",


    "flight_information":
        "",


    "trip_duration":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: personalized_activity_planning_task
        # Workflow Edge: personalized_activity_planning_task -> restaurant_scenic_location_scout_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: personalized_activity_planning_task")
        print("=" * 80)

        task_prompt = """Research and find cool things to do at {destination}.
    Focus on activities and events that match the traveler's interests and age group.
    Utilize internet search tools and recommendation engines to gather the information.

    Traveler's information:

    - origin: {origin}
    - destination: {destination}
    - age of the traveler: {age}
    - hotel localtion: {hotel_location}
    - flight infromation: {flight_information}
    - how long is the trip: {trip_duration}"""
        # Execute via the assigned agent: personalized_activity_planner
        result = await personalized_activity_planner.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: restaurant_scenic_location_scout_task
        # Workflow Edge: restaurant_scenic_location_scout_task -> itinerary_compilation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: restaurant_scenic_location_scout_task")
        print("=" * 80)

        task_prompt = """Find highly-rated restaurants and dining experiences at {destination}.
    Recommend scenic locations and fun activities that align with the traveler's preferences.
    Use internet search tools, restaurant review sites, and travel guides.
    Make sure to find a variety of options to suit different tastes and budgets, and ratings for them.

    Traveler's information:
    - origin: {origin}
    - destination: {destination}
    - age of the traveler: {age}
    - hotel localtion: {hotel_location}
    - flight infromation: {flight_information}
    - how long is the trip: {trip_duration}"""
        # Execute via the assigned agent: restaurant_scout
        result = await restaurant_scout.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: itinerary_compilation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: itinerary_compilation_task")
        print("=" * 80)

        task_prompt = """Compile all researched information into a comprehensive day-by-day itinerary for the trip to {destination}.
    Ensure the itinerary integrates flights, hotel information, and all planned activities and dining experiences.
    Use text formatting and document creation tools to organize the information."""
        # Execute via the assigned agent: itinerary_compiler
        result = await itinerary_compiler.run(task=task_prompt)

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