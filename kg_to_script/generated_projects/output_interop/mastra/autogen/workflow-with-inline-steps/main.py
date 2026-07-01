import asyncio

from team import (
    mastra_default_agent,
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
        # Workflow Step: task_step_one
        # Workflow Edge: task_step_one -> task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_one")
        print("=" * 80)

        task_prompt = """Compute doubledValue from triggerData.inputValue. """
        # Execute via the assigned agent: mastra_default_agent
        result = await mastra_default_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_two")
        print("=" * 80)

        task_prompt = """If stepOne succeeded, compute incrementedValue = doubledValue + 1; else return 0. """
        # Execute via the assigned agent: mastra_default_agent
        result = await mastra_default_agent.run(task=task_prompt)

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