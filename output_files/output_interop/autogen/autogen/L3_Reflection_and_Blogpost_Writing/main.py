import asyncio

from team import (
    writer_1,
    critic_1,
    seo_reviewer_1,
    legal_reviewer_1,
    ethics_reviewer_1,
    meta_reviewer_1,
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
        # Workflow Step: blogpost_generation_task
        # Workflow Edge: blogpost_generation_task -> ethics_review_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: blogpost_generation_task")
        print("=" * 80)

        task_prompt = """Task instructs the Writer to produce a concise but engaging blogpost about DeepLearning.AI within 100 words."""
        # Execute via the assigned agent: writer_1
        result = await writer_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: ethics_review_task
        # Workflow Edge: ethics_review_task -> meta_aggregation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: ethics_review_task")
        print("=" * 80)

        task_prompt = """Review the following content. Return review into as JSON object only: {'reviewer': '', 'review': ''}."""
        # Execute via the assigned agent: ethics_reviewer_1
        result = await ethics_reviewer_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: meta_aggregation_task
        # Workflow Edge: meta_aggregation_task -> blogpost_generation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: meta_aggregation_task")
        print("=" * 80)

        task_prompt = """This task consumes JSON outputs from SEO, Legal, and Ethics reviewers and produces a consolidated suggestion object (the notebook orchestrates this via the Critic.register_nested_chats and nested chat flow)."""
        # Execute via the assigned agent: meta_reviewer_1
        result = await meta_reviewer_1.run(task=task_prompt)

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