import asyncio


from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: invoke_nested_data_processing_workflow
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: invoke_nested_data_processing_workflow")
        print("=" * 80)

        task_prompt = """Invokes nested workflow 'data-processing' with input schema { inputValue: number } and expects output { isEven: boolean }."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_one_task_double_input
        # Workflow Edge: step_one_task_double_input -> resume_increment
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_one_task_double_input")
        print("=" * 80)

        task_prompt = """Execution logic: await delay(10000); doubledValue = inputData.inputValue * 2; return { doubledValue }."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: resume_increment
        # Workflow Edge: resume_increment -> step_three_task_triple_incremented_value
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: resume_increment")
        print("=" * 80)

        task_prompt = """Execution logic: if (!resumeData?.extraNumber) { await suspend({}); return { incrementedValue: 0 }; } else { incrementedValue = inputData.doubledValue + 1 + resumeData.extraNumber; return { incrementedValue }; }"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_three_task_triple_incremented_value
        # Workflow Edge: step_three_task_triple_incremented_value -> step_four_task_is_even_check
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_three_task_triple_incremented_value")
        print("=" * 80)

        task_prompt = """Execution logic: tripledValue = inputData.incrementedValue * 3; return { tripledValue }."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: step_four_task_is_even_check
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: step_four_task_is_even_check")
        print("=" * 80)

        task_prompt = """Execution logic: isEven = (inputData.tripledValue % 2 === 0); return { isEven }."""
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