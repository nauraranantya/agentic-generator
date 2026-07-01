import asyncio

from team import (
    unnamed,
    unnamed,
    unnamed,
    unnamed,
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
        # Workflow Step: task_write_blog
        # Workflow Edge: task_write_blog -> task_critic_initiate_1
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_write_blog")
        print("=" * 80)

        task_prompt = """Writer generates a concise blogpost about DeepLearning.AI. """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_critic_initiate_1
        # Workflow Edge: task_critic_initiate_1 -> task_nested_seo_review
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_critic_initiate_1")
        print("=" * 80)

        task_prompt = """Critic initiates chat with Writer (first initiate_chat call, max_turns=3). """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_nested_seo_review
        # Workflow Edge: task_nested_seo_review -> task_nested_legal_review
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_nested_seo_review")
        print("=" * 80)

        task_prompt = """SEO reviewer performs one-turn review using reflection_with_llm summary_prompt. """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_nested_legal_review
        # Workflow Edge: task_nested_legal_review -> task_nested_ethics_review
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_nested_legal_review")
        print("=" * 80)

        task_prompt = """Legal reviewer performs one-turn review using reflection_with_llm summary_prompt. """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_nested_ethics_review
        # Workflow Edge: task_nested_ethics_review -> task_meta_aggregate
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_nested_ethics_review")
        print("=" * 80)

        task_prompt = """Ethics reviewer performs one-turn review using reflection_with_llm summary_prompt. """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_meta_aggregate
        # Workflow Edge: task_meta_aggregate -> task_critic_initiate_2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_meta_aggregate")
        print("=" * 80)

        task_prompt = """Meta reviewer aggregates feedback and provides final suggestion. """
        # Execute via the assigned agent: unnamed
        result = await unnamed.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_critic_initiate_2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_critic_initiate_2")
        print("=" * 80)

        task_prompt = """Critic initiates chat with Writer (second initiate_chat call, max_turns=2) which triggers nested reviews. """
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