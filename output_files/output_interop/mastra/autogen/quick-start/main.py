import asyncio

from team import (
    cat_one,
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
        # Workflow Step: task_log_cat_name
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_log_cat_name")
        print("=" * 80)

        task_prompt = """Task that takes { name: string } as input, performs logging 'Hello, <name> 🐈' and returns { rawText: string } containing the greeting. Implemented in source as createStep with id 'logCatName' and executed by the workflow runtime/console."""
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