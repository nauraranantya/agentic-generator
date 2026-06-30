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
        # Workflow Step: site_crawl_sync_step_task
        # Workflow Edge: site_crawl_sync_step_task -> generate_spec_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: site_crawl_sync_step_task")
        print("=" * 80)

        task_prompt = """Task executed by the workflow step site-crawl-sync-step. It runs the SiteCrawlTool (Firecrawl client) to extract markdown pages."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: generate_spec_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: generate_spec_task")
        print("=" * 80)

        task_prompt = """Task executed by the generate-spec step: this task iterates crawled pages, calls the agent to produce OpenAPI fragments, and then asks the agent to merge them."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: add_to_github_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: add_to_github_task")
        print("=" * 80)

        task_prompt = """Task executed by makePRToMastra workflow: formats YAML via agent and writes files to GitHub then creates a PR."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

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