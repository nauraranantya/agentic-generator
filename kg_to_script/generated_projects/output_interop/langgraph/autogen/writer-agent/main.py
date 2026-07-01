import asyncio

from team import (
    writer_agent,
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
        # Workflow Step: task_prepare
        # Workflow Edge: task_prepare -> task_writer
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_prepare")
        print("=" * 80)

        task_prompt = """Create an initial draft of the document by invoking the bound tool and streaming response to the UI. """
        # Execute via the assigned agent: writer_agent
        result = await writer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_writer
        # Workflow Edge: task_writer -> task_suggestions
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_writer")
        print("=" * 80)

        task_prompt = """Generate the full document content based on the user's request and earlier messages; stream to UI, then finalise. """
        # Execute via the assigned agent: writer_agent
        result = await writer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_suggestions
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_suggestions")
        print("=" * 80)

        task_prompt = """Call the model to produce a finishing/suggestions message based on collected messages and tool call completions. """
        # Execute via the assigned agent: writer_agent
        result = await writer_agent.run(task=task_prompt)

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