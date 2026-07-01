import asyncio

from team import (
    langgraph_anthropic_agent,
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
        # Workflow Step: find_store_task
        # Workflow Edge: find_store_task -> order_pizza_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: find_store_task")
        print("=" * 80)

        task_prompt = """You are a helpful AI assistant, tasked with extracting information from the conversation between you, and the user, in order to find a pizza shop for them. """
        # Execute via the assigned agent: langgraph_anthropic_agent
        result = await langgraph_anthropic_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: order_pizza_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: order_pizza_task")
        print("=" * 80)

        task_prompt = """You are a helpful AI assistant, tasked with placing an order for a pizza for the user. """
        # Execute via the assigned agent: langgraph_anthropic_agent
        result = await langgraph_anthropic_agent.run(task=task_prompt)

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