import asyncio

from team import (
    stockbroker_01,
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
        # Workflow Step: call_tools
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: call_tools")
        print("=" * 80)

        task_prompt = """Task executed by the Stockbroker agent to call the language model with bound tools and to route resulting tool calls to tool-specific handlers. Uses the system prompt and conversation messages as input to the LLM."""
        # Execute via the assigned agent: stockbroker_01
        result = await stockbroker_01.run(task=task_prompt)

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