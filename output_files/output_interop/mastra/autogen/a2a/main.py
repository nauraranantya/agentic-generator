import asyncio

from team import (
    my_agent,
    content_creator_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "researchResult":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: research_task
        # Workflow Edge: research_task -> content_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: research_task")
        print("=" * 80)

        task_prompt = """Task where the first agent gathers information. In code: researchTaskId = `research-${Date.now()}` and a message with the researchQuery is sent via a2aClient.sendMessage. The task returns a message/status object and the resulting textual research output is stored in the ResearchResult resource."""
        # Execute via the assigned agent: my_agent
        result = await my_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: content_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: content_task")
        print("=" * 80)

        task_prompt = """Task where the content-creator agent receives research output and transforms it into an engaging blog post introduction. In the code the prompt is constructed by embedding researchResult into a template and sending via secondA2aClient.sendMessage."""
        # Execute via the assigned agent: content_creator_agent
        result = await content_creator_agent.run(task=task_prompt)

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