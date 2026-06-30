"""
Auto-generated AutoGen Team: MastraSystem
Goals:
  - Generate OpenAPI spec from docs: Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.
Capabilities:
  - Convert markdown to OpenAPI spec: Extract endpoints, parameters, responses and models from markdown documentation and produce an OpenAPI fragment.
  - Merge OpenAPI fragments: Merge multiple OpenAPI fragments into a single valid OpenAPI spec (resolve conflicts, unify components).
  - Format spec as YAML: Produce a properly formatted YAML spec from textual content.
Resources:
  - Crawled data (markdown pages): Resource produced by site-crawl tool: an array of objects containing markdown text and metadata with sourceURL. Used as input for generate-spec tool.
  - Merged OpenAPI spec (yaml string): The merged OpenAPI specification produced by the generate-spec tool (string YAML). This resource is consumed by the add-to-github tool.
  - Pull Request URL / result: The PR created on GitHub as a result of add-to-github tool (pr_url if created).
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


def site_crawl_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SiteCrawl

    Description:
    Crawl a website and extract the markdown content
    """
    return (
        "Tool 'site_crawl_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


site_crawl_tool = FunctionTool(
    site_crawl_tool_impl,
    description="""Crawl a website and extract the markdown content"""
)


def firecrawl_integration_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    FirecrawlIntegration

    Description:
    Integration client used to crawl websites (Firecrawl API key supplied at runtime).
    """
    return (
        "Tool 'firecrawl_integration' "
        "is a generated stub and "
        "has not been implemented yet."
    )


firecrawl_integration = FunctionTool(
    firecrawl_integration_impl,
    description="""Integration client used to crawl websites (Firecrawl API key supplied at runtime)."""
)


def generate_spec_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    GenerateSpec

    Description:
    Generate an OpenAPI spec from crawled website markdown; uses the OpenAPI agent to convert pages and merge them.
    """
    return (
        "Tool 'generate_spec_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


generate_spec_tool = FunctionTool(
    generate_spec_tool_impl,
    description="""Generate an OpenAPI spec from crawled website markdown; uses the OpenAPI agent to convert pages and merge them."""
)


def add_to_git_hub_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    AddtoGit

    Description:
    Commit the spec to GitHub: formats YAML via the agent, creates branch, commits files and opens a pull request.
    """
    return (
        "Tool 'add_to_git_hub_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


add_to_git_hub_tool = FunctionTool(
    add_to_git_hub_tool_impl,
    description="""Commit the spec to GitHub: formats YAML via the agent, creates branch, commits files and opens a pull request."""
)


def git_hub_integration_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    GitHubIntegration

    Description:
    GitHub integration client that performs git ref, file write and pull request operations (requires PERSONAL_ACCESS_TOKEN).
    """
    return (
        "Tool 'git_hub_integration' "
        "is a generated stub and "
        "has not been implemented yet."
    )


git_hub_integration = FunctionTool(
    git_hub_integration_impl,
    description="""GitHub integration client that performs git ref, file write and pull request operations (requires PERSONAL_ACCESS_TOKEN)."""
)


# ==================================================
# Agents
# ==================================================


openapi_spec_gen_agent = AssistantAgent(
    name="openapi_spec_gen_agent",
    model_client=model_client,
    system_message="""
Role:
OpenAPI spec writer agent

Goal:
Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.

Background:
You are a OpenAPI spec writer agent.
""",
)



