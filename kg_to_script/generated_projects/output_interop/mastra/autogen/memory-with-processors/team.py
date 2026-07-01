"""
Auto-generated AutoGen Team: UnnamedProject
Goals:
  - : Goal to illustrate that TokenLimiter ensures conversation memory stays within token limits while preserving recent context.
  - : Goal to show custom memory processors can filter or redact content based on keywords or types (e.g., tool calls).
  - : Goal to validate that the support agent can use tools, recall recent context, and that TokenLimiter prunes older content when exceeding token limits.
Resources:
  - : Represents the large textual content that the read-file tool returns (truncated to 20K chars or generated mock content).
  - : Represents textual results returned by web-search tool (simulated search output).
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


def read_file_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    read_file_tool

    Description:
    Read a large file to test token limits; attempts several file system locations and otherwise generates a large mock file, returning a truncated 20K-character string.
    """
    return (
        "Tool 'read_file_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


read_file_tool = FunctionTool(
    read_file_tool_impl,
    description="""Read a large file to test token limits; attempts several file system locations and otherwise generates a large mock file, returning a truncated 20K-character string."""
)


def search_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    search_tool

    Description:
    Search the web for information. Input schema expects a 'query' string.
    """
    return (
        "Tool 'search_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_tool = FunctionTool(
    search_tool_impl,
    description="""Search the web for information. Input schema expects a 'query' string."""
)


# ==================================================
# Agents
# ==================================================


token_test_agent = AssistantAgent(
    name="token_test_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
Used as agent instructions to guide agent behavior in the Token Limiter demonstration.
""",
)


technical_support = AssistantAgent(
    name="technical_support",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
Agent system instructions controlling behavior and style (support-agent.ts).
""",
)


technical_support_repo = AssistantAgent(
    name="technical_support_repo",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


forgetful_job_interviewer = AssistantAgent(
    name="forgetful_job_interviewer",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
System instructions used during the interactive interviewer demo.
""",
)


forgetful_job_interviewer_repo = AssistantAgent(
    name="forgetful_job_interviewer_repo",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
System instructions used in repository example (mastra/agents).
""",
)



team = RoundRobinGroupChat(
    participants=[
        token_test_agent,
        technical_support,
        technical_support_repo,
        forgetful_job_interviewer,
        forgetful_job_interviewer_repo,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Demonstrate TokenLimiter by having agent call read-file tool to produce a large response, then query the agent to show forgetting/pruning behavior.

Expected Output:
Completed: task_token_limiter_demo


Task:
Interactive interviewer scenario where the agent may forget information that contains configured keywords (e.g., 'name').

Expected Output:
Completed: task_forgetful_interviewer_demo


Task:
Support dialogue where user describes laptop overheating and agent uses web-search tool; memory TokenLimiter demonstrates retention/pruning.

Expected Output:
Completed: task_technical_support_demo

"""
