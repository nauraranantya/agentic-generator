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



team = RoundRobinGroupChat(
    participants=[
        writer_1,
        critic_1,
        seo_reviewer_1,
        legal_reviewer_1,
        ethics_reviewer_1,
        meta_reviewer_1,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Task instructs the Writer to produce a concise but engaging blogpost about DeepLearning.AI within 100 words.

Expected Output:
A concise blogpost (with title) within 100 words.


Task:
Review the following content. Return review into as JSON object only: {'reviewer': '', 'review': ''}.

Expected Output:
JSON object only. Fields: reviewer, review.


Task:
This task consumes JSON outputs from SEO, Legal, and Ethics reviewers and produces a consolidated suggestion object (the notebook orchestrates this via the Critic.register_nested_chats and nested chat flow).

Expected Output:
Consolidated suggestions and a final recommendation for the Writer.


Task:
Review the following content. Return review into as JSON object only: {'Reviewer': '', 'Review': ''}. Here Reviewer should be your role.

Expected Output:
JSON object only. Fields: Reviewer, Review.


Task:
Review the following content. Return review into as JSON object only: {'Reviewer': '', 'Review': ''}.

Expected Output:
JSON object only. Fields: Reviewer, Review.

"""