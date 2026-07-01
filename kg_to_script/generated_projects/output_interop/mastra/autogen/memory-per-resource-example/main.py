import asyncio

from team import (
    personal_assistant,
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
        # Workflow Step: task_start_conversation
        # Workflow Edge: task_start_conversation -> task_update_memory
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_start_conversation")
        print("=" * 80)

        task_prompt = """Start a new conversation thread. System message template (in source):
`New conversation thread started at ${new Date().toISOString()}. 
This may be a returning user - check your working memory to see if you know them already.
If this is a new user, introduce yourself and learn about them.
If this is a returning user, greet them warmly and reference what you remember!` 
This message is generated at runtime with a timestamp; represented here as a template."""
        # Execute via the assigned agent: personal_assistant
        result = await personal_assistant.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_update_memory
        # Workflow Edge: task_update_memory -> task_interactive_chat
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_update_memory")
        print("=" * 80)

        task_prompt = """Inspect conversation content and persist updates to per-resource working memory. Source code expects the agent to output updates wrapped with <working_memory> tags; updates are masked in the stream and persisted to LibSQL. UI uses a spinner during persistence but streaming semantics are an implementation detail (not modeled)."""
        # Execute via the assigned agent: personal_assistant
        result = await personal_assistant.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_interactive_chat
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_interactive_chat")
        print("=" * 80)

        task_prompt = """Receive user messages, call the agent with memory context (resource + thread), stream responses to the user. The loop terminates when the user types 'exit' or 'quit'. The code obtains user input via Readline; runtime specifics are not modeled. The agent should use stored working memory where relevant."""
        # Execute via the assigned agent: personal_assistant
        result = await personal_assistant.run(task=task_prompt)

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