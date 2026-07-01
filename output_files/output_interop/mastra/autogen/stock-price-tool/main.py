import asyncio

from team import (
    stock_agent,
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
        # Workflow Step: task_init
        # Workflow Edge: task_init -> task_query
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_init")
        print("=" * 80)

        task_prompt = """Initialize the Stock Agent before handling requests. """
        # Execute via the assigned agent: stock_agent
        result = await stock_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_query
        # Workflow Edge: task_query -> task_tool_call
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_query")
        print("=" * 80)

        task_prompt = """What is the current stock price of Apple (AAPL)? """
        # Execute via the assigned agent: stock_agent
        result = await stock_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tool_call
        # Workflow Edge: task_tool_call -> task_end
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tool_call")
        print("=" * 80)

        task_prompt = """Call the stockPrices tool with symbol 'AAPL' to fetch the latest closing price. """
        # Execute via the assigned agent: stock_agent
        result = await stock_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_end
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_end")
        print("=" * 80)

        task_prompt = """Return the formatted current price to the user. """
        # Execute via the assigned agent: stock_agent
        result = await stock_agent.run(task=task_prompt)

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