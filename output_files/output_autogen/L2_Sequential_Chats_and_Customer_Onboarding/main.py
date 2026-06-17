import asyncio

from team import (
    team,
    TASK_PROMPT,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {

}


async def main():


    task = TASK_PROMPT


    print("\n" + "=" * 80)
    print("TASK")
    print("=" * 80)
    print(task)

    print("\n" + "=" * 80)
    print("STREAM")
    print("=" * 80)

    # Prevent infinite loops
    team._termination_condition = MaxMessageTermination(
        max_messages=20
    )

    try:

        async for msg in team.run_stream(
            task=task
        ):

            print("\n" + "-" * 60)
            print(type(msg).__name__)

            if hasattr(msg, "source"):
                print(f"SOURCE: {msg.source}")

            if hasattr(msg, "content"):
                print(msg.content)

            else:
                print(msg)

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