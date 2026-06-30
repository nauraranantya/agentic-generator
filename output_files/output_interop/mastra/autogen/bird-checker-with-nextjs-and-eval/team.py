"""
Auto-generated AutoGen Team: MastraDeploymentBirdChecker
Goals:
  - Identify birds and species from images: Primary goal: determine whether images contain birds, identify species when present, and summarize the location.
Objectives:
  - Accuracy evaluation objective: Objective to measure whether the agent identifies birds and species correctly (used by evaluation).
Environments:
  - Web UI Environment (nextjs + browser UI (visualization of images, interactive tags)): Operational environment of the Bird Checker (user selects tags in UI which trigger image retrieval and agent analysis).
Capabilities:
  - analyze image (detect bird, species, location): Capability assigned to birdAgent: view image, determine if a bird is present, return species scientific name and a short human-readable location summary.
  - fetch random image from Unsplash: Tool capability: call Unsplash search API for a random image matching provided query and return a selected image object.
Resources:
  - Unsplash API (external resource): External API used by GetRandomImageTool: https://api.unsplash.com/search/photos
  - Image resource (unsplash result): A resource that represents an image object returned by Unsplash. Contains URLs and photographer attribution in the runtime system; structurally represented here as a generic resource.
  - BirdResponse (structured agent output): Structured output format expected from the agent: { bird: boolean, species: string, location: string }.
  - IMAGES.isBird image (sample): Sample image expected to be a bird (IMAGES.isBird in src/lib/evals/data.ts).
  - IMAGES.notBird image (sample): Sample image expected to NOT be a bird (IMAGES.notBird in src/lib/evals/data.ts).
  - Evaluation results (bird detection): Contains scoring results for the evaluation (containsScorer: checks bird boolean and that species string contains expected scientific name). Represented as a resource literal in the system.
  - tag:wildlife: Tag option presented in UI: 'wildlife'.
  - tag:feathers: Tag option presented in UI: 'feathers'.
  - tag:flying: Tag option presented in UI: 'flying'.
  - tag:birds: Tag option presented in UI: 'birds'.
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
# Environment: Web UI Environment (nextjs + browser UI (visualization of images, interactive tags))
# Operational environment of the Bird Checker (user selects tags in UI which trigger image retrieval and agent analysis).

# ==================================================
# Generated Tool Stubs
# ==================================================


def get_random_image_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Getarandomimagefromunsplash

    Description:
    Gets a random image from Unsplash based on the selected option (query enum). Declared as a tool in src/mastra/tools.
    """
    return (
        "Tool 'get_random_image_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


get_random_image_tool = FunctionTool(
    get_random_image_tool_impl,
    description="""Gets a random image from Unsplash based on the selected option (query enum). Declared as a tool in src/mastra/tools."""
)


# ==================================================
# Agents
# ==================================================


bird_agent = AssistantAgent(
    name="bird_agent",
    model_client=model_client,
    system_message="""
Role:
analyze images to detect birds, identify species and location

Goal:
Primary goal: determine whether images contain birds, identify species when present, and summarize the location.

Background:
agent instructions (default context for agent)
""",
)



