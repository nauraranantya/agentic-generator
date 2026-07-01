"""
Auto-generated AutoGen Team: UnnamedProject
Human Agents:
  - customer_proxy_agent (customer_proxy)
Resources:
  - : Structured output expected from summary: JSON object of the form {'name': '', 'location': ''}.
"""

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.agents import UserProxyAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
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


# ==================================================
# Human Agents (UserProxy)
# ==================================================

customer_proxy_agent = UserProxyAgent(
    name="customer_proxy_agent",
    description="""customer_proxy """,
)

