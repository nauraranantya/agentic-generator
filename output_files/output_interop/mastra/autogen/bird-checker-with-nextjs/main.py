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
        # Workflow Step: fetch_random_image_task
        # Workflow Edge: fetch_random_image_task -> analyze_image_and_produce_bird_metadata
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: fetch_random_image_task")
        print("=" * 80)

        task_prompt = """Get a random image from Unsplash using a selected query option"""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: analyze_image_and_produce_bird_metadata
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: analyze_image_and_produce_bird_metadata")
        print("=" * 80)

        task_prompt = """view this image and let me know if it's a bird or not, and the scientific name of the bird without any explanation. Also summarize the location for this picture in one or two short sentences understandable by a high school student"""
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