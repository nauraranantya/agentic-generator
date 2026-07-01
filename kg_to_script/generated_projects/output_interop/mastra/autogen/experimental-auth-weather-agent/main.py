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
        # Workflow Step: fetch_weather
        # Workflow Edge: fetch_weather -> plan_activities
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_weather")
        print("=" * 80)

        task_prompt = """Fetches weather forecast for a given city.

Implementation summary preserved semantically:
- Input: { city: string }
- Process:
  * Call geocoding API to get latitude, longitude, canonical name.
  * Call weather API with current & hourly parameters.
  * Compute forecast object:
    { date: now, maxTemp: max(hourly.temperature_2m), minTemp: min(hourly.temperature_2m),
      condition: map(weathercode), precipitationChance: max(hourly.precipitation_probability), location: <city name> }
- Output: forecast object (see weather-forecast resource)."""
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

        task_prompt = """Suggests activities based on the normalized weather forecast.

Semantic summary:
- Input: forecast object (weather-forecast-resource)
- Behavior:
  * Construct a user prompt by interpolating the forecast JSON into a template prompt (planActivities_user_prompt).
  * Submit prompts to the planner agent which has a strict system prompt (weather-agent-instructions-planner).
  * Receive a streamed text response and aggregate into a single activities string.
- Output: activities-text-resource (string).
Constraints:
- Output must follow the planner system prompt format (emoji sections, headers, specific fields)."""
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