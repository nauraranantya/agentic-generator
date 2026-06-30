import asyncio

from team import (
    biomed_agent_1,
    healthcare_agent_1,
    financial_agent_1,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "weaviate_feature":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: biomedical_agent_task_research_a_weaviate_feature
        # Workflow Edge: biomedical_agent_task_research_a_weaviate_feature -> healthcare_agent_task_research_a_weaviate_feature
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: biomedical_agent_task_research_a_weaviate_feature")
        print("=" * 80)

        task_prompt = """Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs."""
        # Execute via the assigned agent: biomed_agent_1
        result = await biomed_agent_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: healthcare_agent_task_research_a_weaviate_feature
        # Workflow Edge: healthcare_agent_task_research_a_weaviate_feature -> financial_agent_task_research_a_weaviate_feature
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: healthcare_agent_task_research_a_weaviate_feature")
        print("=" * 80)

        task_prompt = """Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs."""
        # Execute via the assigned agent: healthcare_agent_1
        result = await healthcare_agent_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: financial_agent_task_research_a_weaviate_feature
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: financial_agent_task_research_a_weaviate_feature")
        print("=" * 80)

        task_prompt = """Conduct a thorough research about {weaviate_feature}
Make sure you find any interesting and relevant information using the web and Weaviate blogs."""
        # Execute via the assigned agent: financial_agent_1
        result = await financial_agent_1.run(task=task_prompt)

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