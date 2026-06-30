import asyncio

from team import (
    stock_weather_agent,
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
        # Workflow Step: user_request_task
        # Workflow Edge: user_request_task -> get_weather_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: user_request_task")
        print("=" * 80)

        task_prompt = """High-level task representing the incoming user prompt that asks for weather in Seattle and the current stock price of Apple (AAPL). This task triggers a workflow that coordinates tool calls to fetch weather and stock data."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: get_weather_task
        # Workflow Edge: get_weather_task -> get_stock_price_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_weather_task")
        print("=" * 80)

        task_prompt = """Task representing the action to obtain current weather for a location. Executed by the Weather Tool which returns a structured JSON-like result with temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: get_stock_price_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_stock_price_task")
        print("=" * 80)

        task_prompt = """Task representing the action to obtain the most recent stock close price for a given symbol. Executed by the Stock Price Tool which returns a JSON-like result with symbol and currentPrice."""
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