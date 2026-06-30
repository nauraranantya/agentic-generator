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
        # Workflow Step: capitalize_sentence_task
        # Workflow Edge: capitalize_sentence_task -> capitalize_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: capitalize_sentence_task")
        print("=" * 80)

        task_prompt = """Task: Capitalize the first letter of each word in a provided sentence-like string. Conceptual behavior: split input string on space characters, for each token convert the first character to uppercase and append the rest of the token unchanged, then join tokens using a single space to produce the output string."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: capitalize_task
        # Workflow Edge: capitalize_task -> format_messages_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: capitalize_task")
        print("=" * 80)

        task_prompt = """Task: Capitalize the first letter of a string (typically a single word). Conceptual behavior: take the string, replace its first character with its uppercase equivalent, and append the remaining substring unchanged."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: format_messages_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: format_messages_task")
        print("=" * 80)

        task_prompt = """Task: Serialize an array of BaseMessage objects into a single formatted string. Behavior summary: for each message in the array, determine its role by calling the message's getType() operation, obtain the message content; if content is a string, use it directly, otherwise serialize the content with JSON.stringify; then wrap the content in an XML-like tag using the role as the tag name and an index attribute, concatenating all formatted message blocks separated by newlines."""
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