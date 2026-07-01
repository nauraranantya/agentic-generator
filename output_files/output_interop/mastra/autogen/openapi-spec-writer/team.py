
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


def tool_site_crawl_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_site_crawl

    Description:
    Crawl a website and extract the markdown content
    """
    return (
        "Tool 'tool_site_crawl' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_site_crawl = FunctionTool(
    tool_site_crawl_impl,
    description="""Crawl a website and extract the markdown content """
)


def tool_generate_spec_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_generate_spec

    Description:
    Generate a spec from a website
    """
    return (
        "Tool 'tool_generate_spec' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_generate_spec = FunctionTool(
    tool_generate_spec_impl,
    description="""Generate a spec from a website """
)


def tool_add_to_github_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    tool_add_to_github

    Description:
    Commit the spec to GitHub and create a PR
    """
    return (
        "Tool 'tool_add_to_github' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_add_to_github = FunctionTool(
    tool_add_to_github_impl,
    description="""Commit the spec to GitHub and create a PR """
)


# ==================================================
# Agents
# ==================================================


openapi_spec_gen_agent = AssistantAgent(
    name="openapi_spec_gen_agent",
    model_client=model_client,
    system_message="""
Role:
openapi-spec-writer

Goal:
openapi-spec-writer

Background:
You are a openapi-spec-writer.
""",
)



