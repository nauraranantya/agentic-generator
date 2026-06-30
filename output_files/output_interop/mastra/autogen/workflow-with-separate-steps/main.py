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

        task_prompt = """Semantic algorithm (no code): 
- Read inputValue (numeric).
- Compute doubledValue = inputValue * 2.
- Compute isOriginalOdd = true if inputValue modulo 2 equals 1, otherwise false.
- Return an object containing doubledValue (number) and isOriginalOdd (boolean)."""
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

        task_prompt = """Semantic algorithm (no code):
- Receive doubledValue (numeric) and isOriginalOdd (boolean).
- If isOriginalOdd is true, set incrementedValue = doubledValue + 1; otherwise set incrementedValue = doubledValue.
- Return an object containing incrementedValue (number)."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_three
        # Workflow Edge: task_step_three -> task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_three")
        print("=" * 80)

        task_prompt = """Semantic algorithm (no code):
- Ensure that stepTwo produced a valid incrementedValue (numeric). If not available or invalid, the step should fail with an explanatory error.
- Compute tripledValue = incrementedValue * 3.
- Return an object containing tripledValue (number).
Note: This step semantically depends on stepTwo; in the implementation getStepResult(stepTwo) is used to access the prior output. The dependency is represented in the workflow as a relatedStep and nextStep (stepTwo -> stepThree)."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_four")
        print("=" * 80)

        task_prompt = """Semantic algorithm (no code):
- Ensure that stepThree produced a valid tripledValue (numeric). If not available or invalid, the step should fail with an explanatory error.
- Compute isEven = (tripledValue modulo 2 === 0).
- Return an object containing isEven (boolean).
Note: This step semantically depends on stepThree; the implementation accesses prior step results for validation. Represented in the workflow graph via relatedStep and nextStep relations."""
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