"""
Auto-generated AutoGen Team: UnnamedProject
Objectives:
  - : Objective representing the evaluation goal to measure the relevancy of ycAgent answers using an automatic scorer.
  - : Objective requiring the agent to answer questions about companies in the YC 2024 directory using only the dataset fields: name, longDescription, tags, industries, batch.
Capabilities:
  - : A scorer created by createAnswerRelevancyScorer used in tests: model 'openai/gpt-4o' with options scale:1 and uncertaintyWeight:0.3.
Resources:
  - : The Y Combinator Directory data used by the yc-directory tool (set in src/mastra/data/2024.ts). This dataset is an array of company objects; each object contains name, longDescription, tags, industries, batch fields. The original array is located in the project at src/mastra/data/2024.ts and contains many company entries for F24, S24, W24 batches and others. For fidelity, the dataset reference path is preserved here rather than embedding the entire array into the ontology file. Use the referenced file to obtain the full literal data when reconstructing the system.
  - : Single evaluation input used in tests: { input: 'Can you tell me what recent YC companies are working on AI Frameworks?' }
  - : Results produced by the evaluation runner when scoring the agent's output for the input question using the AnswerRelevancyScorer.
  - : References the key source files used to construct this ontology population: src/mastra/index.ts, src/mastra/agents/index.ts, src/mastra/tools/index.ts, src/mastra/data/2024.ts, src/mastra/tests/index.ts.
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


def yc_directory_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    yc_directory_tool

    Description:
    Tool that returns the Y Combinator 2024 directory data. Created in src/mastra/tools/index.ts. Exposes an execute action that returns the dataset.
    """
    return (
        "Tool 'yc_directory_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


yc_directory_tool = FunctionTool(
    yc_directory_tool_impl,
    description="""Tool that returns the Y Combinator 2024 directory data. Created in src/mastra/tools/index.ts. Exposes an execute action that returns the dataset."""
)


def mastra_evals_runner_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    mastra_evals_runner

    Description:
    Represents the runEvals invocation in src/mastra/tests/index.ts. Executes an evaluation run on a target agent using a set of scorer capabilities and data inputs.
    """
    return (
        "Tool 'mastra_evals_runner' "
        "is a generated stub and "
        "has not been implemented yet."
    )


mastra_evals_runner = FunctionTool(
    mastra_evals_runner_impl,
    description="""Represents the runEvals invocation in src/mastra/tests/index.ts. Executes an evaluation run on a target agent using a set of scorer capabilities and data inputs."""
)


# ==================================================
# Agents
# ==================================================


yc_directory_agent = AssistantAgent(
    name="yc_directory_agent",
    model_client=model_client,
    system_message="""
Role:
YC Directory Agent

Goal:
YC Directory Agent

Background:
Used as agent-level instructions for ycDirectoryAgent (src/mastra/agents/index.ts).
""",
)



