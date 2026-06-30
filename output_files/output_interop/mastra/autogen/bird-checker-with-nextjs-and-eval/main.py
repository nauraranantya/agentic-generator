import asyncio

from team import (
    bird_agent,
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
        # Workflow Edge: get_random_image_task -> analyze_image_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: get_random_image_task")
        print("=" * 80)

        task_prompt = """Task to fetch a random image from Unsplash using a user-selected query option (wildlife, feathers, flying, birds)."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: analyze_image_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: analyze_image_task")
        print("=" * 80)

        task_prompt = """Task to analyze an image and determine whether it is a bird, the species scientific name, and a short location summary. Implemented via the birdAgent (agent.generate with an image and a text instruction)."""
        # Execute via the assigned agent: bird_agent
        result = await bird_agent.run(task=task_prompt)

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