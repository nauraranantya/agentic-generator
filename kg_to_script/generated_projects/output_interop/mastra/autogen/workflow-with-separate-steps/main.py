import asyncio

from team import (
    mastra_agent,
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
        # Workflow Step: task_step_one
        # Workflow Edge: task_step_one -> task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_one")
        print("=" * 80)

        task_prompt = """Doubles triggerData.inputValue and returns an object with { doubledValue }. """
        # Execute via the assigned agent: mastra_agent
        result = await mastra_agent.run(task=task_prompt)

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

        task_prompt = """Triples triggerData.inputValue and returns an object with { tripledValue }. """
        # Execute via the assigned agent: mastra_agent
        result = await mastra_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_two
        # Workflow Edge: task_step_two -> task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_two")
        print("=" * 80)

        task_prompt = """Reads the payload from stepOne (doubledValue) and returns an object with { incrementedValue } which is doubledValue + 1. """
        # Execute via the assigned agent: mastra_agent
        result = await mastra_agent.run(task=task_prompt)

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

        task_prompt = """Reads the payload from stepThree (tripledValue) and returns an object with { isEven } indicating whether tripledValue is even. """
        # Execute via the assigned agent: mastra_agent
        result = await mastra_agent.run(task=task_prompt)

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