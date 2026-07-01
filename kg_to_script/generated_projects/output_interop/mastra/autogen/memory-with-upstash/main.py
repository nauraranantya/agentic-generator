import asyncio

from team import (
    chef_agent,
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
        # Workflow Step: set_up_session_and_thread
        # Workflow Edge: set_up_session_and_thread -> suggest_recipes_from_user_s_listed_ingredients
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: set_up_session_and_thread")
        print("=" * 80)

        task_prompt = """Represents creating a thread/session id for streaming interactions. In source a randomUUID() is used for threadId; resourceId is set to 'SOME_USER_ID'."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: suggest_recipes_from_user_s_listed_ingredients
        # Workflow Edge: suggest_recipes_from_user_s_listed_ingredients -> suggest_recipes_from_friend_s_ingredients
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: suggest_recipes_from_user_s_listed_ingredients")
        print("=" * 80)

        task_prompt = """User asks the agent: 'In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.' This exact string is captured in Prompt_InitialIngredients and used as input to the ChefAgent."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: suggest_recipes_from_friend_s_ingredients
        # Workflow Edge: suggest_recipes_from_friend_s_ingredients -> recall_what_was_cooked_previously
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: suggest_recipes_from_friend_s_ingredients")
        print("=" * 80)

        task_prompt = """User asks: 'Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.' Captured exactly in Prompt_FriendIngredients."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: recall_what_was_cooked_previously
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: recall_what_was_cooked_previously")
        print("=" * 80)

        task_prompt = """User asks: 'What did we cook before I went to my friends house?' In source, this call is made with memoryOptions: { lastMessages: 3 } to override recall settings for that call. That override is captured in Task_MemoryOverride_Config."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

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