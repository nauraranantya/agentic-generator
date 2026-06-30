import asyncio

from team import (
    travel_agent,
    travel_analyzer,
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
        # Workflow Step: find_outbound_flight
        # Workflow Edge: find_outbound_flight -> find_return_flight
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_outbound_flight")
        print("=" * 80)

        task_prompt = """Select 1 outbound flight for the given departureLocation -> arrivalLocation and date range. Return entire flight object including legs and timestamps. Consider flightPriority to trade off price vs convenience."""
        # Execute via the assigned agent: travel_agent
        result = await travel_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: find_return_flight
        # Workflow Edge: find_return_flight -> find_accommodation_hotel_or_airbnb
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_return_flight")
        print("=" * 80)

        task_prompt = """Select 1 return flight for the given arrivalLocation -> departureLocation and date range. Return entire flight object including legs and timestamps."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: find_accommodation_hotel_or_airbnb
        # Workflow Edge: find_accommodation_hotel_or_airbnb -> find_attractions
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_accommodation_hotel_or_airbnb")
        print("=" * 80)

        task_prompt = """If accommodationType is 'hotel' call Search Hotels tool using arrivalCityId. If accommodationType is 'airbnb', first call Search Airbnb Location tool to get place id and then call Search Airbnb tool using that id, typeOfPlace, startDate, endDate. Do NOT call Airbnb tools if accommodationType is hotel. Do NOT call searchHotels if accommodationType is airbnb."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: find_attractions
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_attractions")
        print("=" * 80)

        task_prompt = """Find three activities and attractions for the customer based on interests and arrivalAttractionId; return id, name, description, rating, price, imageUrl, location."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: sync_csv_data_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: sync_csv_data_task")
        print("=" * 80)

        task_prompt = """Sync Csv Data Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

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