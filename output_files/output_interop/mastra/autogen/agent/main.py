import asyncio

from team import (
    chef_agent,
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
        # Workflow Step: task_query_pantry
        # Workflow Edge: task_query_pantry -> task_generate_text
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_query_pantry")
        print("=" * 80)

        task_prompt = """User asks what they can make given pantry ingredients (pasta, canned tomatoes, garlic, olive oil, dried herbs). """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_generate_text
        # Workflow Edge: task_generate_text -> task_text_stream
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_generate_text")
        print("=" * 80)

        task_prompt = """Alternate/duplicate generate usage with same pantry query. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_text_stream
        # Workflow Edge: task_text_stream -> task_generate_stream
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_text_stream")
        print("=" * 80)

        task_prompt = """Streamed response for chicken/coconut/sweet potatoes/curry powder scenario. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_generate_stream
        # Workflow Edge: task_generate_stream -> task_text_object
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_generate_stream")
        print("=" * 80)

        task_prompt = """Streaming variant with array input; yields streamed recipe. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_text_object
        # Workflow Edge: task_text_object -> task_text_object_jsonschema
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_text_object")
        print("=" * 80)

        task_prompt = """Generate a lasagna recipe structured as an object with ingredients and steps. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_text_object_jsonschema
        # Workflow Edge: task_text_object_jsonschema -> task_generate_object
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_text_object_jsonschema")
        print("=" * 80)

        task_prompt = """Generate lasagna recipe constrained by provided JSON Schema. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_generate_object
        # Workflow Edge: task_generate_object -> task_stream_object
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_generate_object")
        print("=" * 80)

        task_prompt = """Generate lasagna recipe with structured output (array input variant). """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_stream_object
        # Workflow Edge: task_stream_object -> task_generate_stream_object
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_stream_object")
        print("=" * 80)

        task_prompt = """Streamed generation of a lasagna recipe as structured object. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_generate_stream_object
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_generate_stream_object")
        print("=" * 80)

        task_prompt = """Final streaming structured generation variant. """
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

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