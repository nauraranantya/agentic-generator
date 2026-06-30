import asyncio

from team import (
    cat_one,
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
        # Workflow Step: step_one_task
        # Workflow Edge: step_one_task -> step_two_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_one_task")
        print("=" * 80)

        task_prompt = """Step One Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_two_task
        # Workflow Edge: step_two_task -> step_three_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_two_task")
        print("=" * 80)

        task_prompt = """Step Two Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_three_task
        # Workflow Edge: step_three_task -> step_four_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_three_task")
        print("=" * 80)

        task_prompt = """Step Three Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_four_task
        # Workflow Edge: step_four_task -> step_five_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_four_task")
        print("=" * 80)

        task_prompt = """Step Four Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_five_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_five_task")
        print("=" * 80)

        task_prompt = """Step Five Task"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_six_task
        # Workflow Edge: step_six_task -> step_two_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_six_task")
        print("=" * 80)

        task_prompt = """Step Six Task"""
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