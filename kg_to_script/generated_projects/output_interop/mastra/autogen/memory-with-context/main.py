import asyncio

from team import (
    memory_agent,
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
        # Workflow Step: task_initial_system_message
        # Workflow Edge: task_initial_system_message -> task_receive_user_input
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_initial_system_message")
        print("=" * 80)

        task_prompt = """On session start the program sends a system-role message; uses prompt_system_firstChat if isFirstChat, otherwise prompt_system_returningChat. The timestamp is inserted at runtime."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_receive_user_input
        # Workflow Edge: task_receive_user_input -> task_agent_stream_response
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_receive_user_input")
        print("=" * 80)

        task_prompt = """A blocking read from a human input channel; in code this is achieved by Readline and awaiting user's input, then the input is forwarded to the agent.stream call."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_agent_stream_response
        # Workflow Edge: task_agent_stream_response -> task_receive_user_input
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_agent_stream_response")
        print("=" * 80)

        task_prompt = """Agent processes the user's message, streams text output. During streaming the implementation masks two tag sections: 'think' (internal chain-of-thought-like output) and 'working_memory' (memory saving operations). Spinners (status indicators) are displayed while sections stream; upon end spinners succeed and input reading resumes. The stream also interacts with the Memory component for saving/retrieving conversation context."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

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