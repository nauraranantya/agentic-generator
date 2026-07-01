import asyncio

from team import (
    yc_directory_agent,
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
        # Workflow Step: fetch_yc_directory_task
        # Workflow Edge: fetch_yc_directory_task -> process_yc_data_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_yc_directory_task")
        print("=" * 80)

        task_prompt = """Task to retrieve the YC directory dataset using the yc-directory tool. """
        # Execute via the assigned agent: yc_directory_agent
        result = await yc_directory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: process_yc_data_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: process_yc_data_task")
        print("=" * 80)

        task_prompt = """Task to process/format the YC directory data for consumption by downstream callers (e.g., filtering, adding batch metadata). """
        # Execute via the assigned agent: yc_directory_agent
        result = await yc_directory_agent.run(task=task_prompt)

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