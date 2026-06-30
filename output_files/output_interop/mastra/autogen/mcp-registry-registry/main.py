import asyncio

from team import (
    mcp_registry_agent,
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
        # Workflow Step: initialize_agent_task
        # Workflow Edge: initialize_agent_task -> search_mcp_registries_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: initialize_agent_task")
        print("=" * 80)

        task_prompt = """Initialization task where the MCP client is queried (listTools()) and the agent's tools collection is populated."""
        # Execute via the assigned agent: mcp_registry_agent
        result = await mcp_registry_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: search_mcp_registries_task
        # Workflow Edge: search_mcp_registries_task -> finalize_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: search_mcp_registries_task")
        print("=" * 80)

        task_prompt = """Task performed by the MCP Registry Agent: search for registries by ID, tag, or name. This task uses the agent prompt (instructions) and the MCP Registry Tool / MCP Client to obtain information about registries."""
        # Execute via the assigned agent: mcp_registry_agent
        result = await mcp_registry_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: finalize_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: finalize_task")
        print("=" * 80)

        task_prompt = """Task to finalize the search operation and present results (formatting, references)."""
        # Execute via the assigned agent: mcp_registry_agent
        result = await mcp_registry_agent.run(task=task_prompt)

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