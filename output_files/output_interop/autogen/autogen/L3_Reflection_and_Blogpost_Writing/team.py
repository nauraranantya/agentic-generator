"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Goal: create a concise (within 100 words) blogpost about DeepLearning.AI and refine it via a reflection process with multiple reviewers.
Objectives:
  - : Objective: produce initial blogpost draft to be reviewed and refined.
Resources:
  - Blogpost Draft (resource): Expected output: concise engaging blogpost (with title) about DeepLearning.AI, within 100 words.
  - SEO Review (resource): JSON object with reviewer role and review text (as requested by summary prompt).
  - Legal Review (resource): JSON object with reviewer role and review text.
  - Ethics Review (resource): JSON object with reviewer role and review text.
  - Meta Reviewer Suggestion (resource): Aggregate review and final suggestion to improve the blogpost.
"""

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
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


# ==================================================
# Agents
# ==================================================


writer_1 = AssistantAgent(
    name="writer_1",
    model_client=model_client,
    system_message="""
Role:
Writer

Goal:
Writer

Background:
You are a Writer.
""",
)


critic_1 = AssistantAgent(
    name="critic_1",
    model_client=model_client,
    system_message="""
Role:
Critic

Goal:
Critic

Background:
You are a Critic.
""",
)


seo_reviewer_1 = AssistantAgent(
    name="seo_reviewer_1",
    model_client=model_client,
    system_message="""
Role:
SEO Reviewer

Goal:
SEO Reviewer

Background:
You are a SEO Reviewer.
""",
)


legal_reviewer_1 = AssistantAgent(
    name="legal_reviewer_1",
    model_client=model_client,
    system_message="""
Role:
Legal Reviewer

Goal:
Legal Reviewer

Background:
You are a Legal Reviewer.
""",
)


ethics_reviewer_1 = AssistantAgent(
    name="ethics_reviewer_1",
    model_client=model_client,
    system_message="""
Role:
Ethics Reviewer

Goal:
Ethics Reviewer

Background:
You are a Ethics Reviewer.
""",
)


meta_reviewer_1 = AssistantAgent(
    name="meta_reviewer_1",
    model_client=model_client,
    system_message="""
Role:
Meta Reviewer

Goal:
Meta Reviewer

Background:
You are a Meta Reviewer.
""",
)



