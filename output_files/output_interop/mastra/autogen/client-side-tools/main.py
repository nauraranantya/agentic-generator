import asyncio

from team import (
    agent,
    test_agent,
    human_user,
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
        # Workflow Step: user_submits_message
        # Workflow Edge: user_submits_message -> stream_message_to_agent
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: user_submits_message")
        print("=" * 80)

        task_prompt = """User types text into the UI textarea and clicks Send; triggers setting isStreaming flag, clears previous responseText, and calls streamIt with prompt equal to the message."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: stream_message_to_agent
        # Workflow Edge: stream_message_to_agent -> process_streamed_events_tool_calls_tool_results_deltas_text_parts
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: stream_message_to_agent")
        print("=" * 80)

        task_prompt = """The agent.stream call is invoked with { messages: prompt, clientTools: clientSideToolCallsMap }. This initiates a streaming response from the language model which may include tool call events and text parts."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: process_streamed_events_tool_calls_tool_results_deltas_text_parts
        # Workflow Edge: process_streamed_events_tool_calls_tool_results_deltas_text_parts -> execute_add_post_tool
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: process_streamed_events_tool_calls_tool_results_deltas_text_parts")
        print("=" * 80)

        task_prompt = """The client processes the streaming response using response.processDataStream callbacks: onToolCallPart, onToolResultPart, onToolCallDeltaPart, onTextPart. onTextPart appends string parts to responseText. onToolCallPart executes matching client tool by name and args."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: execute_add_post_tool
        # Workflow Edge: execute_add_post_tool -> append_text_parts_to_the_response_text_state
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: execute_add_post_tool")
        print("=" * 80)

        task_prompt = """Tool call for 'addPost' triggers execute with args { color, name } and appends a post object to the posts array."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: append_text_parts_to_the_response_text_state
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: append_text_parts_to_the_response_text_state")
        print("=" * 80)

        task_prompt = """Each onTextPart callback appends the delivered text fragment to responseText. This task is repeated as streaming text parts arrive and results in updating the UI display region."""
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