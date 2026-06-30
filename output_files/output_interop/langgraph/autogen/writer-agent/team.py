
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


def draft_text_document_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    drafttextdocument

    Description:
    Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document.
    """
    return (
        "Tool 'draft_text_document_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


draft_text_document_tool = FunctionTool(
    draft_text_document_tool_impl,
    description="""Prepare a text document for the user with a short title and short description for browsing purposes. Can be also used when creating a new version of the document."""
)


# ==================================================
# Agents
# ==================================================


writer_annotation_agent_uuid_1 = AssistantAgent(
    name="writer_annotation_agent_uuid_1",
    model_client=model_client,
    system_message="""
Role:
annotation-driven writer

Goal:
annotation-driven writer

Background:
You are a annotation-driven writer.
""",
)



