import asyncio

from team import (
    product_competitor_agent,
    strategy_planner_agent,
    creative_content_creator_agent,
    senior_photographer_agent,
    chief_creative_director_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "product_website":
        "",


    "product_details":
        "",


    "copy":
        "",

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

        task_prompt = """Analyze the given product website: {product_website}.
Extra details provided by the customer: {product_details}.

Focus on identifying unique features, benefits,
and the overall narrative presented.

Your final report should clearly articulate the
product's key selling points, its market appeal,
and suggestions for enhancement or positioning.
Emphasize the aspects that make the product stand out.

Keep in mind, attention to detail is crucial for
a comprehensive analysis. It's currenlty 2024."""
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

        task_prompt = """Explore competitor of: {product_website}.
Extra details provided by the customer: {product_details}.

Identify the top 3 competitors and analyze their
strategies, market positioning, and customer perception.

Your final report MUST include BOTH all context about {product_website}
and a detailed comparison to whatever competitor they have competitors."""
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

        task_prompt = """You're creating a targeted marketing campaign for: {product_website}.
Extra details provided by the customer: {product_details}.

To start this campaing we will need a strategy and creative content ideas.
It should be meticulously designed to captivate and engage
the product's target audience.

Based on your ideas your co-workers will create the content for the campaign.

Your final answer MUST be ideas that will resonate with the audience and
also include ALL context you have about the product and the customer."""
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

        task_prompt = """Craft an engaging Instagram post copy.
The copy should be punchy, captivating, concise,
and aligned with the product marketing strategy.

Focus on creating a message that resonates with
the target audience and highlights the product's
unique selling points.

Your ad copy must be attention-grabbing and should
encourage viewers to take action, whether it's
visiting the website, making a purchase, or learning
more about the product.

Your final answer MUST be 3 options for an ad copy for instagram that
not only informs but also excites and persuades the audience."""
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

        task_prompt = """You are working on a new campaign for a super important customer,
and you MUST take the most amazing photo ever for an instagram post
regarding the product, you have the following copy:
{copy}

This is the product you are working with: {product_website}.
Extra details provided by the customer: {product_details}.

Imagine what the photo you wanna take describe it in a paragraph.
Here are some examples for you follow:
- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

Think creatively and focus on how the image can capture the audience's
attention. Don't show the actual product on the photo.

Your final answer must be 3 options of photographs, each with 1 paragraph
describing the photograph exactly like the examples provided above."""
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

        task_prompt = """Review the photos you got from the senior photographer.
Make sure it's the best possible and aligned with the product's goals,
review, approve, ask clarifying question or delegate follow up work if
necessary to make decisions. When delegating work send the full draft
as part of the information.

This is the product you are working with: {product_website}.
Extra details provided by the customer: {product_details}.

Here are some examples on how the final photographs should look like:
- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

Your final answer must be 3 reviewed options of photographs,
each with 1 paragraph description following the examples provided above."""
        # Execute via the assigned agent: chief_creative_director_agent
        result = await chief_creative_director_agent.run(task=task_prompt)

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