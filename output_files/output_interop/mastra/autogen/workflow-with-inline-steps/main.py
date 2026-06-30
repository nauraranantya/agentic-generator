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
        # Workflow Step: task_step_one
        # Workflow Edge: task_step_one -> task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_one")
        print("=" * 80)

        task_prompt = """Execution logic (preserved from source):
    doubledValue = context?.workflow?.state?.triggerData.inputValue * 2

    Notes:
    - The task reads the workflow trigger value at path workflow.state.triggerData.inputValue and outputs doubledValue.
    - Input schema (declared in code): { value: number } (this is the step input schema)
    - Output schema (declared in code): { doubledValue: number }"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_two
        # Workflow Edge: task_step_two -> task_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_two")
        print("=" * 80)

        task_prompt = """Execution logic (preserved from source):
    incrementedValue = inputData.valueToIncrement + 1

    Notes:
    - stepTwo's declared input schema: { valueToIncrement: number }
    - stepTwo's declared output schema: { incrementedValue: number }
    - Typical dataflow in this workflow: stepOne produces 'doubledValue'. The code's input name is 'valueToIncrement'; implementers should map stepOne.doubledValue -> stepTwo.valueToIncrement at runtime."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_three")
        print("=" * 80)

        task_prompt = """Execution logic (preserved from source):
    if (context?.workflow?.resumeData?.confirm !== 'true') {
      return context?.workflow?.suspend({
        message: 'Do you accept?',
      });
    }

    return {
      message: 'Thank you for accepting',
    };

    Notes:
    - This task implements a suspend/resume pattern: when resumeData.confirm !== 'true', it suspends and requests confirmation with message 'Do you accept?'.
    - On resume with confirm === 'true' the task returns a message 'Thank you for accepting'.
    - The ontology cannot represent runtime suspend/resume mechanics formally; this behavior is captured here as descriptive metadata."""
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