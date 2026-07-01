import asyncio

from team import (
    onboarding_personal_information_agent,
    onboarding_topic_preference_agent,
    customer_engagement_agent,
    customer_proxy_agent,
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
        # Workflow Step: task_collect_personal_info
        # Workflow Edge: task_collect_personal_info -> task_collect_topic_preferences
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_collect_personal_info")
        print("=" * 80)

        task_prompt = """sender: onboarding_personal_information_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; summary_args: { 'summary_prompt': "Return the customer information into as JSON object only: {'name': '', 'location': ''}" }; max_turns: 2; clear_history: True """
        # Execute via the assigned agent: onboarding_personal_information_agent
        result = await onboarding_personal_information_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_collect_topic_preferences
        # Workflow Edge: task_collect_topic_preferences -> task_customer_proxy_to_engagement
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_collect_topic_preferences")
        print("=" * 80)

        task_prompt = """sender: onboarding_topic_preference_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; max_turns: 1; clear_history: False """
        # Execute via the assigned agent: onboarding_topic_preference_agent
        result = await onboarding_topic_preference_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_customer_proxy_to_engagement
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_customer_proxy_to_engagement")
        print("=" * 80)

        task_prompt = """sender: customer_proxy_agent; recipient: customer_engagement_agent; message: "Let's find something fun to read."; summary_method: reflection_with_llm; max_turns: 1 """
        # Execute via the assigned agent: customer_proxy_agent
        result = await customer_proxy_agent.run(task=task_prompt)

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