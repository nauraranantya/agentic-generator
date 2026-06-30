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
        # Workflow Step: task_extraction
        # Workflow Edge: task_extraction -> task_call_tools
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_extraction")
        print("=" * 80)

        task_prompt = """Extraction task: given the entire conversation history, call a tool named "extract" with the following schema:
- location: string (required) - "The location to plan the trip for. Can be a city, state, or country."
- startDate: string (optional) - "YYYY-MM-DD"
- endDate: string (optional) - "YYYY-MM-DD"
- numberOfGuests: number (optional) - defaults to 2 if not provided

Behavior notes:
- Do NOT guess or make up information. If location missing, produce a single-sentence clarification request: "Please specify the location for the trip you want to go on".
- After extraction: apply date defaulting logic (see TripDetails resource description)."""
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_classify
        # Workflow Edge: task_classify -> task_extraction
        # Workflow Edge: task_classify -> task_call_tools
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_classify")
        print("=" * 80)

        task_prompt = """Classification task: use a tool named "classify" with schema { isRelevant: boolean } to determine if previously extracted tripDetails remain relevant to the user's most recent message.
- If isRelevant == false -> the agent will clear tripDetails (tripDetails becomes undefined) and routing will proceed to extraction.
- If isRelevant == true -> proceed to callTools."""
        # Execute via the assigned agent: trip_planner_agent
        result = await trip_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_call_tools
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_call_tools")
        print("=" * 80)

        task_prompt = """CallTools task: binds ACCOMMODATIONS_TOOLS (list-accommodations and list-restaurants), invokes the language model to decide which tool(s) to call, and pushes UI items for results. The LLM receives the system message:
"You are an AI assistant who helps users book trips. Use the user's most recent message(s) to contextually generate a response."
The task expects state.tripDetails to be defined and produces resources:
- Accommodations list resource
- Restaurants list resource
- UI items (represented here as produced resources)"""
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