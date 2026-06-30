import asyncio

from team import (
    lead_market_analyst,
    chief_marketing_strategist,
    creative_content_creator,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "customer_domain":
        "",


    "project_description":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: research_task
        # Workflow Edge: research_task -> project_understanding_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: research_task")
        print("=" * 80)

        task_prompt = """Conduct a thorough research about the customer and competitors in the context of {customer_domain}.
Make sure you find any interesting and relevant information given the current year is 2024.
We are working with them on the following project: {project_description}."""
        # Execute via the assigned agent: lead_market_analyst
        result = await lead_market_analyst.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: project_understanding_task
        # Workflow Edge: project_understanding_task -> marketing_strategy_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: project_understanding_task")
        print("=" * 80)

        task_prompt = """Understand the project details and the target audience for
{project_description}.
Review any provided materials and gather additional information as needed."""
        # Execute via the assigned agent: chief_marketing_strategist
        result = await chief_marketing_strategist.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: marketing_strategy_task
        # Workflow Edge: marketing_strategy_task -> campaign_idea_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: marketing_strategy_task")
        print("=" * 80)

        task_prompt = """Formulate a comprehensive marketing strategy for the project
{project_description} of the customer {customer_domain}.
Use the insights from the research task and the project understanding task to create a high-quality strategy."""
        # Execute via the assigned agent: chief_marketing_strategist
        result = await chief_marketing_strategist.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: campaign_idea_task
        # Workflow Edge: campaign_idea_task -> copy_creation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: campaign_idea_task")
        print("=" * 80)

        task_prompt = """Develop creative marketing campaign ideas for {project_description}.
Ensure the ideas are innovative, engaging, and aligned with the overall marketing strategy."""
        # Execute via the assigned agent: creative_content_creator
        result = await creative_content_creator.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: copy_creation_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: copy_creation_task")
        print("=" * 80)

        task_prompt = """Create marketing copies based on the approved campaign ideas for {project_description}.
Ensure the copies are compelling, clear, and tailored to the target audience."""
        # Execute via the assigned agent: creative_content_creator
        result = await creative_content_creator.run(task=task_prompt)

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