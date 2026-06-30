import asyncio

from team import (
    chat_agent_1,
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
        # Workflow Step: chat_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: chat_task")
        print("=" * 80)

        task_prompt = """Task logic (semantic summary extracted from source code):
    - Build an array of messages to send to the language model by making the first message a system role: 'You are a helpful assistant.' and then appending the runtime state.messages array.
    - Invoke the language model with that messages array.
    - Return the model response as the task output (messages).
    Implementation detail: The source uses a ChatOpenAI client with { model: 'gpt-4o-mini' } and calls model.invoke([...])."""
        # Execute via the assigned agent: chat_agent_1
        result = await chat_agent_1.run(task=task_prompt)

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