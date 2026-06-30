import asyncio

from team import (
    chef_agent,
    memory_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "ISO_TIMESTAMP":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: task_recipe_suggest_initial_query
        # Workflow Edge: task_recipe_suggest_initial_query -> task_recipe_suggest_friends_house_query
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_recipe_suggest_initial_query")
        print("=" * 80)

        task_prompt = """Agent.stream called with Prompt_Index_WhatCanIMake; ChefAgent produces short high-level steps. The call includes threadId and resourceId parameters to enable memory association."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_recipe_suggest_friends_house_query
        # Workflow Edge: task_recipe_suggest_friends_house_query -> task_recipe_suggest_recall_previous
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_recipe_suggest_friends_house_query")
        print("=" * 80)

        task_prompt = """Agent.stream called with Prompt_Index_FriendsHouse to produce alternative recipes. Uses same threadId and resourceId as previous to keep memory context."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_recipe_suggest_recall_previous
        # Workflow Edge: task_recipe_suggest_recall_previous -> task_recipe_suggest_recall_previous
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_recipe_suggest_recall_previous")
        print("=" * 80)

        task_prompt = """Agent.stream called with Prompt_Index_RecallPrevious requesting recall using memoryOptions.lastMessages = 3."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_chat_start_conversation
        # Workflow Edge: task_chat_start_conversation -> task_chat_interactive_message
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_chat_start_conversation")
        print("=" * 80)

        task_prompt = """On startup a system message (Prompt_Chat_SystemStart) is sent to the memory agent. This is used to re-engage a returning user and may include a dynamic timestamp."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_chat_interactive_message
        # Workflow Edge: task_chat_interactive_message -> task_chat_interactive_message
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_chat_interactive_message")
        print("=" * 80)

        task_prompt = """Loop of receiving a user message and calling memoryAgent.stream(prompt, { memory: { thread, resource } }). The user message is forwarded as Prompt_Chat_UserMessage_Template at runtime with concrete content."""
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