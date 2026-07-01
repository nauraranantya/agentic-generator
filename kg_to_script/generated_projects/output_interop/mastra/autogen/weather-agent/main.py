import asyncio

from team import (
    weather_agent,
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
        # Workflow Step: task_fetch_weather
        # Workflow Edge: task_fetch_weather -> task_plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_fetch_weather")
        print("=" * 80)

        task_prompt = """Fetches weather forecast for a given city """
        # Execute via the assigned agent: weather_agent
        result = await weather_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_plan_activities")
        print("=" * 80)

        task_prompt = """Suggests activities based on weather conditions """
        # Execute via the assigned agent: weather_agent
        result = await weather_agent.run(task=task_prompt)

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