
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


def tool_draft_text_document_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_draft_text_document

    Description:
    Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document.
    """
    return (
        "Tool 'tool_draft_text_document' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_draft_text_document = FunctionTool(
    tool_draft_text_document_impl,
    description="""Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document. """
)


# ==================================================
# Agents
# ==================================================


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=model_client,
    system_message="""
Role:
writer

Goal:
writer

Background:
You are a writer.
""",
)



