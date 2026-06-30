import asyncio

from team import (
    planner_agent,
    engineer_agent,
    executor_agent,
    writer_agent,
    admin,
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
        # Workflow Step: main_task
        # Workflow Edge: main_task -> plan_information_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: main_task")
        print("=" * 80)

        task_prompt = """Top-level task given by Admin that initiates the workflow. Text preserved in MainTaskPrompt."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: plan_information_task
        # Workflow Edge: plan_information_task -> write_code_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: plan_information_task")
        print("=" * 80)

        task_prompt = """Planner determines which information (stock prices, date range, sources, computation methods) is needed and specifies steps for retrieving it using Python code."""
        # Execute via the assigned agent: planner_agent
        result = await planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: write_code_task
        # Workflow Edge: write_code_task -> execute_code_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: write_code_task")
        print("=" * 80)

        task_prompt = """Engineer implements Python code to retrieve stock data, compute required metrics, and produce artifacts for the writer. Code artifact contains instructions like 'retrieve historic prices, compute performance over last month, format data for report'."""
        # Execute via the assigned agent: engineer_agent
        result = await engineer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: execute_code_task
        # Workflow Edge: execute_code_task -> write_report_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: execute_code_task")
        print("=" * 80)

        task_prompt = """Executor runs the code produced by the Engineer in a specified working directory and returns execution outputs (e.g., numerical results, csv, figures). Execution config preserved on ExecutorConfig_Execution."""
        # Execute via the assigned agent: executor_agent
        result = await executor_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: write_report_task
        # Workflow Edge: write_report_task -> admin_feedback_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: write_report_task")
        print("=" * 80)

        task_prompt = """Writer composes the blog post using execution results; writes in markdown format with relevant titles and places content inside a pseudo ```md``` code block. The writer should accept feedback from Admin and refine the blog."""
        # Execute via the assigned agent: writer_agent
        result = await writer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: admin_feedback_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: admin_feedback_task")
        print("=" * 80)

        task_prompt = """Admin (user_proxy) reviews the blog draft and provides feedback; the Writer will refine the blog accordingly. Modeled as a Task performed by a HumanAgent."""
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