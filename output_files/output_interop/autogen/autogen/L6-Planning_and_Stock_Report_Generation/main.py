import asyncio

from team import (
    admin,
    planner,
    engineer,
    executor,
    writer,
    group_chat_manager,
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
        # Workflow Step: task_initiate_write_blog
        # Workflow Edge: task_initiate_write_blog -> task_planner_plan
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_initiate_write_blog")
        print("=" * 80)

        task_prompt = """Initial user task message used to start the groupchat planning and execution. """
        # Execute via the assigned agent: admin
        result = await admin.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_planner_plan
        # Workflow Edge: task_planner_plan -> task_engineer_write_code
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_planner_plan")
        print("=" * 80)

        task_prompt = """Planner's task to decompose the initial blogpost task into retrievable Python-code-based steps. """
        # Execute via the assigned agent: planner
        result = await planner.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_engineer_write_code
        # Workflow Edge: task_engineer_write_code -> task_executor_run_code
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_engineer_write_code")
        print("=" * 80)

        task_prompt = """Engineer tasked to implement code per the planner's steps. """
        # Execute via the assigned agent: engineer
        result = await engineer.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_executor_run_code
        # Workflow Edge: task_executor_run_code -> task_writer_produce_blog
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_executor_run_code")
        print("=" * 80)

        task_prompt = """Executor runs the engineer's code and reports outputs. """
        # Execute via the assigned agent: executor
        result = await executor.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_writer_produce_blog
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_writer_produce_blog")
        print("=" * 80)

        task_prompt = """Writer composes the final blogpost using execution outputs and admin feedback. """
        # Execute via the assigned agent: writer
        result = await writer.run(task=task_prompt)

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