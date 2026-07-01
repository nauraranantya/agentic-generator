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

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: task_code
        # Workflow Edge: task_code -> task_review
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_code")
        print("=" * 80)

        task_prompt = """code_task from config/tasks.yaml """
        # Execute via the assigned agent: senior_engineer_agent
        result = await senior_engineer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_review
        # Workflow Edge: task_review -> task_evaluate
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_review")
        print("=" * 80)

        task_prompt = """review_task from config/tasks.yaml """
        # Execute via the assigned agent: qa_engineer_agent
        result = await qa_engineer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_evaluate
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_evaluate")
        print("=" * 80)

        task_prompt = """evaluate_task from config/tasks.yaml """
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