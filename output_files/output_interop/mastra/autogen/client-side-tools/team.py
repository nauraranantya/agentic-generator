"""
Auto-generated AutoGen Team: ClientApplicationViteReactTeam
Goals:
  - Interactive browser UI driven by agent: Goal for the client app: enable an interactive UI where the language model/agent can instruct the browser to perform UI changes and stream text responses.
  - Provide interactive user experience: Higher-level goal: deliver a streaming conversational experience with dynamic UI updates triggered by model-invoked tool calls.
Objectives:
  - Enable user-agent interactive messaging: Objective to allow a human user to send free-text messages to the agent and receive streaming responses.
  - Handle streaming responses and events: Objective to properly process streaming data, including tool call events, tool results, deltas, and text parts.
  - Apply UI updates requested via tool calls: Objective to apply client-side state changes (color, logo size, posts) as requested by tool calls from the agent.
Human Agents:
  - human_user ()
Capabilities:
  - Change background color: Capability to change the UI color state (expects a single string property 'color').
  - Change logo size: Capability to change the UI logo size. Expects 'height' and 'width' string properties.
  - Add a new post: Capability to append a new post entry containing 'color' and 'name' to the posts collection in the client.
Resources:
  - background color state: Abstract representation of the application background color state (corresponds to React state 'color' in src/App.tsx).
  - logo size state: Abstract representation of the logo size state (corresponds to React state 'logoSize' with keys 'height' and 'width').
  - posts list state: Abstract representation of the posts array in client state (React state 'posts'). Items are objects with properties 'name' and 'color'.
  - response text stream: Cumulative response text displayed in the UI (state 'responseText' appended by streaming onTextPart handler).
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


def tool_change_color_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    changeColor

    Description:
    Client-side tool that changes the application background color. Declared in clientSideToolCallsMap in src/App.tsx.
    """
    return (
        "Tool 'tool_change_color' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_change_color = FunctionTool(
    tool_change_color_impl,
    description="""Client-side tool that changes the application background color. Declared in clientSideToolCallsMap in src/App.tsx."""
)


def tool_change_logo_size_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    changeLogoSize

    Description:
    Client-side tool that changes the size of the logo. Declared in clientSideToolCallsMap in src/App.tsx.
    """
    return (
        "Tool 'tool_change_logo_size' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_change_logo_size = FunctionTool(
    tool_change_logo_size_impl,
    description="""Client-side tool that changes the size of the logo. Declared in clientSideToolCallsMap in src/App.tsx."""
)


def tool_add_post_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    addPost

    Description:
    Client-side tool that adds a new post to the 'posts' state array. Declared in clientSideToolCallsMap in src/App.tsx.
    """
    return (
        "Tool 'tool_add_post' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_add_post = FunctionTool(
    tool_add_post_impl,
    description="""Client-side tool that adds a new post to the 'posts' state array. Declared in clientSideToolCallsMap in src/App.tsx."""
)


# ==================================================
# Agents
# ==================================================


agent = AssistantAgent(
    name="agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
Goal for the client app: enable an interactive UI where the language model/agent can instruct the browser to perform UI changes and stream text responses.

Background:
System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts).
""",
)


test_agent = AssistantAgent(
    name="test_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
Goal for the client app: enable an interactive UI where the language model/agent can instruct the browser to perform UI changes and stream text responses.

Background:
System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts).
""",
)


# ==================================================
# Human Agents (UserProxy)
# ==================================================

human_user = UserProxyAgent(
    name="human_user",
    description="""""",
)

