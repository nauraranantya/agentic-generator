
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


def get_random_image_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    get_random_image_tool

    Description:
    Gets a random image from Unsplash based on selected query option. Random page selection and order_by ('relevant' or 'latest') logic is applied at runtime.
    """
    return (
        "Tool 'get_random_image_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_random_image_tool = FunctionTool(
    get_random_image_tool_impl,
    description="""Gets a random image from Unsplash based on selected query option. Random page selection and order_by ('relevant' or 'latest') logic is applied at runtime."""
)


# ==================================================
# Agents
# ==================================================


bird_checker = AssistantAgent(
    name="bird_checker",
    model_client=model_client,
    system_message="""
Role:
image-analyst

Goal:
image-analyst

Background:
You are a image-analyst.
""",
)



