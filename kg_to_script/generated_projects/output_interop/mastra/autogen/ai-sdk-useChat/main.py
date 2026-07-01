import asyncio

from team import (
    weather_agent,
    planning_agent,
    developer_fajar_ekaputra,
    developer_kabul_kurniawan,
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
        # Workflow Step: fetch_weather
        # Workflow Edge: fetch_weather -> plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_weather")
        print("=" * 80)

        task_prompt = """Fetches weather forecast for a given city by resolving the city name to coordinates and retrieving daily forecast data. Produces an array of forecast objects { date, maxTemp, minTemp, precipitationChance, condition, location }."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: plan_activities")
        print("=" * 80)

        task_prompt = """Suggests activities based on the weather forecast. Calls an LLM agent (planningAgent) with the forecast data; receives a streaming text response which is concatenated into the final activities output."""
        # Execute via the assigned agent: planning_agent
        result = await planning_agent.run(task=task_prompt)

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