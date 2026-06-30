import asyncio

from team import (
    senior_engineer_agent,
    qa_engineer_agent,
    chief_qa_engineer_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "game":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: code_task
        # Workflow Edge: code_task -> review_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: code_task")
        print("=" * 80)

        task_prompt = """You will create a game using python, these are the instructions:

Instructions
# ------------
{game}"""
        # Execute via the assigned agent: senior_engineer_agent
        result = await senior_engineer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: review_task
        # Workflow Edge: review_task -> evaluate_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: review_task")
        print("=" * 80)

        task_prompt = """You will create a game using python, these are the instructions:

Instructions
# ------------
{game}

Using the code you got, check for errors. Check for logic errors,
syntax errors, missing imports, variable declarations, mismatched brackets,
and security vulnerabilities."""
        # Execute via the assigned agent: qa_engineer_agent
        result = await qa_engineer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: evaluate_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: evaluate_task")
        print("=" * 80)

        task_prompt = """You are helping create a game using python, these are the instructions:

Instructions
# ------------
{game}

You will look over the code to insure that it is complete and
does the job that it is supposed to do."""
        # Execute via the assigned agent: chief_qa_engineer_agent
        result = await chief_qa_engineer_agent.run(task=task_prompt)

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