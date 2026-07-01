import asyncio

from team import (
    crypto_agent,
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
        # Workflow Step: search_crypto_coins_task
        # Workflow Edge: search_crypto_coins_task -> get_crypto_price_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: search_crypto_coins_task")
        print("=" * 80)

        task_prompt = """Semantic task corresponding to the searchCryptoCoins tool."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: get_crypto_price_task
        # Workflow Edge: get_crypto_price_task -> get_historical_crypto_prices_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_crypto_price_task")
        print("=" * 80)

        task_prompt = """Semantic task corresponding to the getCryptoPrice tool."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: get_historical_crypto_prices_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_historical_crypto_prices_task")
        print("=" * 80)

        task_prompt = """Semantic task corresponding to the getHistoricalCryptoPrices tool."""
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