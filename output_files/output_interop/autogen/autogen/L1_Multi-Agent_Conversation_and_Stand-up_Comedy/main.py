import asyncio

from team import (
    chatbot,
    unnamed,
    unnamed,
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
        # Workflow Step: task_guodegang_initiate_chat_1
        # Workflow Edge: task_guodegang_initiate_chat_1 -> task_guodegang_initiate_chat_2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_guodegang_initiate_chat_1")
        print("=" * 80)

        task_prompt = """message="我是郭德纲，于谦呀，我们给观众讲一段相声怎么样？"; recipient=于谦; max_turns=6 """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_guodegang_initiate_chat_2
        # Workflow Edge: task_guodegang_initiate_chat_2 -> task_guodegang_send_followup
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_guodegang_initiate_chat_2")
        print("=" * 80)

        task_prompt = """message="我是郭德纲，于谦呀，我们给观众讲一段相声怎么样？"; summary_method="reflection_with_llm"; summary_prompt="简洁的总结下这场相声表演。" """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_guodegang_send_followup
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_guodegang_send_followup")
        print("=" * 80)

        task_prompt = """message='我们刚才的相声在讲什么?'; recipient=于谦 """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

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