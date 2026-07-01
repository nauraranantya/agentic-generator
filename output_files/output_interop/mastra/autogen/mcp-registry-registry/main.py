import asyncio

from team import (
    registry_registry_server,
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
        # Workflow Step: task_fetch_servers_from_registry
        # Workflow Edge: task_fetch_servers_from_registry -> task_post_process_servers
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_fetch_servers_from_registry")
        print("=" * 80)

        task_prompt = """Locate registry entry, validate servers_url, fetch raw registry data, and hand off to post-processor. """
        # Execute via the assigned agent: registry_registry_server
        result = await registry_registry_server.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_post_process_servers
        # Workflow Edge: task_post_process_servers -> task_filter_servers
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_post_process_servers")
        print("=" * 80)

        task_prompt = """Apply registry-specific post-processing function (e.g., processApifyServers, processDockerServers) to normalize server entries into standard ServerEntry shape. """
        # Execute via the assigned agent: registry_registry_server
        result = await registry_registry_server.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_filter_servers
        # Workflow Edge: task_filter_servers -> task_get_servers_from_registry
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_filter_servers")
        print("=" * 80)

        task_prompt = """Filter ServerEntry results by search term or tag (if implemented), returning matched servers. """
        # Execute via the assigned agent: registry_registry_server
        result = await registry_registry_server.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_get_servers_from_registry
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_get_servers_from_registry")
        print("=" * 80)

        task_prompt = """High-level function orchestrating fetchServersFromRegistry and filterServers, providing the external API used by tools and tests. """
        # Execute via the assigned agent: registry_registry_server
        result = await registry_registry_server.run(task=task_prompt)

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