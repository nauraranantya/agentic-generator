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
        # Workflow Step: task_fetch_random_image
        # Workflow Edge: task_fetch_random_image -> task_analyze_image
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_fetch_random_image")
        print("=" * 80)

        task_prompt = """Task that selects a random image from Unsplash using the getRandomImage tool with a query parameter drawn from an enum of options."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_analyze_image
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_analyze_image")
        print("=" * 80)

        task_prompt = """Task that sends an image and an instruction prompt to the LLM agent to determine whether the image is a bird, the species (scientific name) and a short summary of the picture location."""
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