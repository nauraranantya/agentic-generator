import asyncio

from team import (
    product_competitor_agent,
    strategy_planner_agent,
    creative_content_creator_agent,
    senior_photographer_agent,
    chief_creative_diretor_agent,
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
        # Workflow Step: task_product_analysis
        # Workflow Edge: task_product_analysis -> task_competitor_analysis
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_product_analysis")
        print("=" * 80)

        task_prompt = """Analyze the given product website, identify unique features, benefits, narrative, and recommendations. """
        # Execute via the assigned agent: product_competitor_agent
        result = await product_competitor_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_competitor_analysis
        # Workflow Edge: task_competitor_analysis -> task_campaign_development
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_competitor_analysis")
        print("=" * 80)

        task_prompt = """Identify top competitors and analyze their strategies and positioning relative to the product. """
        # Execute via the assigned agent: product_competitor_agent
        result = await product_competitor_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_campaign_development
        # Workflow Edge: task_campaign_development -> task_instagram_ad_copy
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_campaign_development")
        print("=" * 80)

        task_prompt = """Create a targeted marketing campaign strategy and creative ideas. """
        # Execute via the assigned agent: strategy_planner_agent
        result = await strategy_planner_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_instagram_ad_copy
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_instagram_ad_copy")
        print("=" * 80)

        task_prompt = """Craft engaging Instagram post copy aligned with marketing strategy. """
        # Execute via the assigned agent: creative_content_creator_agent
        result = await creative_content_creator_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_take_photograph
        # Workflow Edge: task_take_photograph -> task_review_photo
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_take_photograph")
        print("=" * 80)

        task_prompt = """Imagine and describe three photograph concepts for the Instagram post based on provided copy and product context. """
        # Execute via the assigned agent: senior_photographer_agent
        result = await senior_photographer_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_review_photo
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_review_photo")
        print("=" * 80)

        task_prompt = """Review photography drafts, approve or request clarifications or delegations; ensure alignment with product goals. """
        # Execute via the assigned agent: chief_creative_diretor_agent
        result = await chief_creative_diretor_agent.run(task=task_prompt)

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