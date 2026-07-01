import asyncio

from team import (
    openapi_spec_gen_agent,
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
        # Workflow Step: task_site_crawl_sync
        # Workflow Edge: task_site_crawl_sync -> task_generate_spec
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_site_crawl_sync")
        print("=" * 80)

        task_prompt = """Crawl a website and extract the markdown content and sync it to the database. """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_generate_spec
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_generate_spec")
        print("=" * 80)

        task_prompt = """For each crawled markdown page, ask the agent to turn it into an OpenAPI spec fragment; then ask the agent to merge fragments into a single spec. """
        # Execute via the assigned agent: openapi_spec_gen_agent
        result = await openapi_spec_gen_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_add_to_github
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_add_to_github")
        print("=" * 80)

        task_prompt = """Take a YAML blob, ask the agent to format it, then create branch, commit files and open a PR via the GitHub client. """
        # Execute via the assigned agent: openapi_spec_gen_agent
        result = await openapi_spec_gen_agent.run(task=task_prompt)

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