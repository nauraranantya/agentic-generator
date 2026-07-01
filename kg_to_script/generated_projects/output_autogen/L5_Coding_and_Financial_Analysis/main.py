import asyncio

from team import (
    code_writer_agent,
    code_executor_agent,
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
        # Workflow Step: task_plot_ytd_v1
        # Workflow Edge: task_plot_ytd_v1 -> task_plot_ytd_v2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_plot_ytd_v1")
        print("=" * 80)

        task_prompt = """Initiated by code_executor_agent to request code from code_writer_agent (Chinese message). """
        # Execute via the assigned agent: code_executor_agent
        result = await code_executor_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_plot_ytd_v2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_plot_ytd_v2")
        print("=" * 80)

        task_prompt = """Initiated by code_executor_agent to request code from code_writer_agent (English message about downloading and plotting YTD stock prices). """
        # Execute via the assigned agent: code_executor_agent
        result = await code_executor_agent.run(task=task_prompt)

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