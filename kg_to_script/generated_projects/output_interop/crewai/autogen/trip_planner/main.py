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

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: task_identify_city
        # Workflow Edge: task_identify_city -> task_gather_city_info
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_identify_city")
        print("=" * 80)

        task_prompt = """Task to analyze and select the best city for the trip based on weather, seasonal events, and travel costs. """
        # Execute via the assigned agent: city_selection_agent
        result = await city_selection_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_gather_city_info
        # Workflow Edge: task_gather_city_info -> task_plan_itinerary
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_gather_city_info")
        print("=" * 80)

        task_prompt = """Task for local expert to compile an in-depth city guide including attractions, customs, events, and costs. """
        # Execute via the assigned agent: local_expert_agent
        result = await local_expert_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_plan_itinerary
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_plan_itinerary")
        print("=" * 80)

        task_prompt = """Task to expand the city guide into a full 7-day itinerary with daily plans, weather, packing suggestions, and budget. """
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