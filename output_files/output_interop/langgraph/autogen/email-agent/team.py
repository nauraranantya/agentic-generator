"""
Auto-generated AutoGen Team: UnnamedProject
Human Agents:
  - user_human ()
Capabilities:
  - Compose Email: Generate a draft email (subject, body, to) from conversation history.
  - Rewrite Email: Rewrite email content given user's response/instructions; should only change requested fields.
  - Send Email: Finalize and send the composed email (in this implementation it yields a confirmation message indicating successful send).
  - Handle Human Interrupt: Present the email to a human for review and accept/edit/ignore/response and handle the resulting input accordingly.
Resources:
  - Conversation History: Sequence of messages between user and agent used as input to generate the email. In implementation substituted into the prompt via {CONVERSATION}.
  - Draft Email: Structured email artifact with fields:
- subject: string
- body: string
- to: string

This is the primary data produced by the writing and rewriting tasks. The implementation expects these exact fields.
  - Sent Email Record: A record/artifact representing that the email was sent. In implementation returned as an AI message: 'Successfully sent email.' (represented as an artifact here).
  - Human Response (interrupt result): Represents the human-interaction result from the interrupt UI. Possible response types recorded in implementation: 'ignore', 'response', 'accept', or 'edit' (with args carrying edited email fields). This ontology stores allowed values in the interrupt config and records that user participated in interrupt interactions.
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


def write_email_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    writeemailtoolschemabound

    Description:
    Tool binding used by the LLM to produce structured email objects. Description: "Write an email based on the conversation history".
    """
    return (
        "Tool 'write_email_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


write_email_tool = FunctionTool(
    write_email_tool_impl,
    description="""Tool binding used by the LLM to produce structured email objects. Description: "Write an email based on the conversation history"."""
)


# ==================================================
# Agents
# ==================================================


email_assistant_agent = AssistantAgent(
    name="email_assistant_agent",
    model_client=model_client,
    system_message="""
Role:
email_assistant

Goal:
email_assistant

Background:
You are a email_assistant.
""",
)


# ==================================================
# Human Agents (UserProxy)
# ==================================================

user_human = UserProxyAgent(
    name="user_human",
    description="""""",
)

