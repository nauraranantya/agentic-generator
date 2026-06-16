from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-3.5-turbo"
)

# ==================================================
# Generated Tool Stubs
# ==================================================


# ==================================================
# Agents
# ==================================================


onboarding_personal_information_agent = AssistantAgent(
    name="onboarding_personal_information_agent",
    model_client=model_client,
    system_message="""
Role:
personal_information_collector

Goal:
personal_information_collector

Background:
You are a personal_information_collector.
""",
)


onboarding_topic_preference_agent = AssistantAgent(
    name="onboarding_topic_preference_agent",
    model_client=model_client,
    system_message="""
Role:
topic_preference_collector

Goal:
topic_preference_collector

Background:
You are a topic_preference_collector.
""",
)


customer_engagement_agent = AssistantAgent(
    name="customer_engagement_agent",
    model_client=model_client,
    system_message="""
Role:
engagement_generator

Goal:
engagement_generator

Background:
You are a engagement_generator.
""",
)


team = RoundRobinGroupChat(
    participants=[
        onboarding_personal_information_agent,
        onboarding_topic_preference_agent,
        customer_engagement_agent,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
sender: onboarding_personal_information_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; summary_args: { 'summary_prompt': "Return the customer information into as JSON object only: {'name': '', 'location': ''}" }; max_turns: 2; clear_history: True

Expected Output:
JSON object with keys 'name' and 'location'


Task:
sender: onboarding_personal_information_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; summary_args: { 'summary_prompt': "Return the customer information into as JSON object only: {'name': '', 'location': ''}" }; max_turns: 2; clear_history: True

Expected Output:
JSON object with keys 'name' and 'location'


Task:
sender: onboarding_topic_preference_agent; recipient: customer_proxy_agent; summary_method: reflection_with_llm; max_turns: 1; clear_history: False

Expected Output:
Completed: task_collect_topic_preferences


Task:
sender: customer_proxy_agent; recipient: customer_engagement_agent; message: "Let's find something fun to read."; summary_method: reflection_with_llm; max_turns: 1

Expected Output:
Completed: task_customer_proxy_to_engagement


Task:
sender: customer_proxy_agent; recipient: customer_engagement_agent; message: "Let's find something fun to read."; summary_method: reflection_with_llm; max_turns: 1

Expected Output:
Completed: task_customer_proxy_to_engagement

"""