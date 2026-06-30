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
        # Workflow Step: fetch_stock_price_for_symbol_aapl_example
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_stock_price_for_symbol_aapl_example")
        print("=" * 80)

        task_prompt = """Task representing the user's invocation in src/index.ts where the agent is asked: 'What is the current stock price of Apple (AAPL)?'. The agent handles the query using its model and invokes the stockPrices tool to fetch the numeric price."""
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