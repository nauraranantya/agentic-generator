import asyncio

from team import (
    weather_agent,
    weather_explainer_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "location":
        "",


    "JSON":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: fetch_weather_task
        # Workflow Edge: fetch_weather_task -> plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_weather_task")
        print("=" * 80)

        task_prompt = """Fetches weather forecast for a given city and produces forecast array resource. Semantics: take city -> produce daily forecast array with fields date, maxTemp, minTemp, precipitationChance, condition, location."""
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

        task_prompt = """Suggests activities based on weather conditions. Input: forecast array (or forecast object). The step constructs a prompt 'Based on the following weather forecast for {location}, suggest appropriate activities: {JSON}' and streams agent response. Produces an activities text resource."""
        # Execute via the assigned agent: weather_agent
        result = await weather_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: weather_tool_call_task
        # Workflow Edge: weather_tool_call_task -> map_forecast_to_prompt_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: weather_tool_call_task")
        print("=" * 80)

        task_prompt = """Task that calls the get-weather tool. Input: { location: string }. Output: simplified current weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location)."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: map_forecast_to_prompt_task
        # Workflow Edge: map_forecast_to_prompt_task -> explain_weather_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: map_forecast_to_prompt_task")
        print("=" * 80)

        task_prompt = """Takes the tool output and formats a short prompt string for the agent. Produces a single string resource."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: explain_weather_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: explain_weather_task")
        print("=" * 80)

        task_prompt = """Agent task that receives a prompt string and produces an explanatory text and activity suggestions. Uses the agent instruction template that enforces a specific output formatting (emoji sections, weather summary, activities, indoor alternatives, special considerations)."""
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