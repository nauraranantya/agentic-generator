"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - Primary goal: Identify birds and contextual metadata: 
Objectives:
  - Acquire representative image for inspection: 
  - Identify bird presence/species and summarize location: 
Environments:
  - Web runtime environment (Next.js / browser + server (application) environment; uses Unsplash API via server-side call and LLM via configured model.): 
Capabilities:
  - detect bird: Determine whether an image contains a bird (boolean).
  - identify species (scientific name): Identify the bird species, ideally returning scientific name as a string.
  - summarize location: Summarize the location of the photographed scene in one or two simple sentences.
  - fetch random image: Capability to query Unsplash and return a representative image resource.
Resources:
  - Example Unsplash image instance (sample resource produced by fetch task): An image resource object with the fields used by the system: 
  alt_description: string,
  urls: { regular: string, raw: string },
  user: { first_name: string, links: { html: string } }.
  (This instance models the schema and an example image result; real images are produced at runtime.)
  - Example bird metadata instance (example resource produced by analyze task): Structured metadata returned by analysis:
  { "bird": boolean, "species": string, "location": string }.
  Example semantics: bird=true, species='Corvus corax' (scientific name), location='a coastal cliff near (region/city)'. The exact scientific name and summary are derived by the agent from the image.
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
# Environment Configuration
# ==================================================
# Environment: Web runtime environment (Next.js / browser + server (application) environment; uses Unsplash API via server-side call and LLM via configured model.)
# 
# Configs: {'NEXT_PUBLIC_UNSPLASH_ACCESS_KEY': 'REDACTED (provided at deployment time). The tool uses this key for Authorization: Client-ID <KEY> when calling Unsplash.'}

# ==================================================
# Generated Tool Stubs
# ==================================================


def get_random_image_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    GetarandomimagefromUnsplashtool

    Description:
    Tool that queries Unsplash and returns a single image object selected from search results. Implemented in the code using a GET to https://api.unsplash.com/search/photos with a query param and optional paging/randomization.
    """
    return (
        "Tool 'get_random_image_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_random_image_tool = FunctionTool(
    get_random_image_tool_impl,
    description="""Tool that queries Unsplash and returns a single image object selected from search results. Implemented in the code using a GET to https://api.unsplash.com/search/photos with a query param and optional paging/randomization."""
)


# ==================================================
# Agents
# ==================================================


bird_checker = AssistantAgent(
    name="bird_checker",
    model_client=model_client,
    system_message="""
Role:
image analyst / bird identifier

Goal:
image analyst / bird identifier

Background:
Agent instruction and purpose
""",
)



