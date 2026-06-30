import asyncio

from team import (
    pizza_orderer_v1,
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
        # Workflow Step: find_pizza_shop_task
        # Workflow Edge: find_pizza_shop_task -> place_pizza_order_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_pizza_shop_task")
        print("=" * 80)

        task_prompt = """Source semantics captured from node 'findStore':
- Uses a structured model output with schema 'find_pizza_shop' to extract:
  { location: string, pizza_company?: string }
- System instruction: 'You are a helpful AI assistant, tasked with extracting information from the conversation between you, and the user, in order to find a pizza shop for them.'
- After model invocation, a ToolMessage is created with content:
  'I've found a pizza shop at 1119 19th St, San Francisco, CA 94107. The phone number for the shop is 415-555-1234.'
- The code includes an artificial delay (sleep) following the model call."""
        # Execute via the assigned agent: pizza_orderer_v1
        result = await pizza_orderer_v1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: place_pizza_order_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: place_pizza_order_task")
        print("=" * 80)

        task_prompt = """Source semantics captured from node 'orderPizza':
- Uses a structured model output with schema 'place_pizza_order' to extract:
  { address: string, phone_number: string, order: string }
- System instruction: 'You are a helpful AI assistant, tasked with placing an order for a pizza for the user.'
- After model invocation, a ToolMessage is created with content:
  'Pizza order successfully placed.'
- The code includes an artificial delay (sleep) prior to execution."""
        # Execute via the assigned agent: pizza_orderer_v1
        result = await pizza_orderer_v1.run(task=task_prompt)

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