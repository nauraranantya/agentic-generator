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
        # Workflow Step: task_initial_ingredients_query
        # Workflow Edge: task_initial_ingredients_query -> task_ingredients_at_friend_s_house
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_initial_ingredients_query")
        print("=" * 80)

        task_prompt = """User asks: 'In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.' This is passed as input to chefAgent.stream with threadId and resourceId context."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_ingredients_at_friend_s_house
        # Workflow Edge: task_ingredients_at_friend_s_house -> task_ask_what_we_cooked_before
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_ingredients_at_friend_s_house")
        print("=" * 80)

        task_prompt = """User asks: 'Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.' This is passed to chefAgent.stream with same threadId/resourceId to append to conversation memory."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_ask_what_we_cooked_before
        # Workflow Edge: task_ask_what_we_cooked_before -> task_memory_agent_recall_operation
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_ask_what_we_cooked_before")
        print("=" * 80)

        task_prompt = """User asks: 'What did we cook before I went to my friends house?' This demonstrates memory recall options with memoryOptions: lastMessages=false and semanticRecall configured."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_memory_agent_recall_operation
        # Workflow Edge: task_memory_agent_recall_operation -> exit
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_memory_agent_recall_operation")
        print("=" * 80)

        task_prompt = """Memory agent performs semantic recall according to configured memory options and may ask for user identification when missing."""
        # Execute via the assigned agent: memory_agent
        result = await memory_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: exit
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: exit")
        print("=" * 80)

        task_prompt = """Represents termination of the script after example interactions (process.exit in index.ts). Modeled as a conceptual task reflecting end of workflow."""
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