import asyncio

from team import (
    trade_agent,
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
        # Workflow Step: open_buy_ui_task
        # Workflow Edge: open_buy_ui_task -> execute_purchase_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: open_buy_ui_task")
        print("=" * 80)

        task_prompt = """Prepare and present the buy stock UI to the user. """
        # Execute via the assigned agent: trade_agent
        result = await trade_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: execute_purchase_task
        # Workflow Edge: execute_purchase_task -> confirm_purchase_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: execute_purchase_task")
        print("=" * 80)

        task_prompt = """Execute the purchase by invoking the buy-stock tool with purchaseDetails. """
        # Execute via the assigned agent: trade_agent
        result = await trade_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: confirm_purchase_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: confirm_purchase_task")
        print("=" * 80)

        task_prompt = """Display purchase confirmation to the user including executed quantity and price. """
        # Execute via the assigned agent: trade_agent
        result = await trade_agent.run(task=task_prompt)

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