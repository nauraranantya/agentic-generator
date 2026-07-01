import asyncio

from team import (
    trip_planner_agent,
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
        # Workflow Step: view_accommodations_task
        # Workflow Edge: view_accommodations_task -> select_accommodation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: view_accommodations_task")
        print("=" * 80)

        task_prompt = """Display available accommodations or restaurants to the user and allow selection. """
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: select_accommodation_task
        # Workflow Edge: select_accommodation_task -> confirm_booking_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: select_accommodation_task")
        print("=" * 80)

        task_prompt = """Handle user selection of an accommodation and present detailed view including price breakdown and booking option. """
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: confirm_booking_task
        # Workflow Edge: confirm_booking_task -> booked_confirmation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: confirm_booking_task")
        print("=" * 80)

        task_prompt = """Prepare order details and invoke the booking tool using the 'book-accommodation' tool call. """
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: booked_confirmation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: booked_confirmation_task")
        print("=" * 80)

        task_prompt = """Display booking confirmation details returned by the booking tool or show success message if no details returned. """
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

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