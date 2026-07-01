import asyncio

from team import (
    bird_checker,
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
        # Workflow Step: get_random_image_task
        # Workflow Edge: get_random_image_task -> image_metadata_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_random_image_task")
        print("=" * 80)

        task_prompt = """Task that obtains an image (imageUrl, photographer info) from Unsplash based on a query. """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: image_metadata_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: image_metadata_task")
        print("=" * 80)

        task_prompt = """Task where the agent inspects an image and returns structured output indicating whether it is a bird, the species, and a short location summary. """
        # Execute via the assigned agent: bird_checker
        result = await bird_checker.run(task=task_prompt)

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