import asyncio

from team import (
    cv_reader,
    matcher,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "path_to_cv":
        "",


    "path_to_jobs_csv":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: read_cv_task
        # Workflow Edge: read_cv_task -> match_cv_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: read_cv_task")
        print("=" * 80)

        task_prompt = """Task: extract structured summary from input CV file."""
        # Execute via the assigned agent: cv_reader
        result = await cv_reader.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: match_cv_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: match_cv_task")
        print("=" * 80)

        task_prompt = """Task: match structured CV summary against job opportunities CSV and produce ranked list."""
        # Execute via the assigned agent: matcher
        result = await matcher.run(task=task_prompt)

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