import asyncio

from team import (
    weather_agent,
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
        # Workflow Step: network_supervisor_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: network_supervisor_task")
        print("=" * 80)

        task_prompt = """You are a helpful supervisor agent that can help users with a variety of tasks."""
        # Execute via the assigned agent: weather_agent
        result = await weather_agent.run(task=task_prompt)

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