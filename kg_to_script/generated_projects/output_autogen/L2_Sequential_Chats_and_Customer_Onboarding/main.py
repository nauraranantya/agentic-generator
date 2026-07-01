import asyncio

from team import (
    onboarding_personal_information_agent,
    onboarding_topic_preference_agent,
    customer_engagement_agent,
    agent_customer_proxy_agent,
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
        # Workflow Step: task_onboarding_personal_info
        # Workflow Edge: task_onboarding_personal_info -> task_onboarding_topic_preference
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_onboarding_personal_info")
        print("=" * 80)

        task_prompt = """Hello, I'm here to help you get started with our product. Could you tell me your name and location? """
        # Execute via the assigned agent: onboarding_personal_information_agent
        result = await onboarding_personal_information_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_onboarding_topic_preference
        # Workflow Edge: task_onboarding_topic_preference -> task_customer_engagement_request
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_onboarding_topic_preference")
        print("=" * 80)

        task_prompt = """Great! Could you tell me what topics you are interested in reading about? """
        # Execute via the assigned agent: onboarding_topic_preference_agent
        result = await onboarding_topic_preference_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_customer_engagement_request
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_customer_engagement_request")
        print("=" * 80)

        task_prompt = """Let's find something fun to read. """
        # Execute via the assigned agent: customer_engagement_agent
        result = await customer_engagement_agent.run(task=task_prompt)

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