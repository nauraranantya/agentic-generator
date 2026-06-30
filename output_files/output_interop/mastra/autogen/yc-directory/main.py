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
        # Workflow Step: run_evals_task
        # Workflow Edge: run_evals_task -> fetch_yc_data_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: run_evals_task")
        print("=" * 80)

        task_prompt = """Task representing the tests/runEvals invocation that evaluates ycAgent using the AnswerRelevancyScorer with a small input dataset."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: fetch_yc_data_task
        # Workflow Edge: fetch_yc_data_task -> answer_yc_directory_query
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_yc_data_task")
        print("=" * 80)

        task_prompt = """Task that represents the operation of the yc-directory tool's execute function returning YC data."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: answer_yc_directory_query
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: answer_yc_directory_query")
        print("=" * 80)

        task_prompt = """Primary task the ycDirectoryAgent performs: accept a natural language query about the YC 2024 directory and produce an answer exclusively using the yc-directory tool's dataset. Must include batch numbers when referencing companies and must not hallucinate beyond the available fields."""
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