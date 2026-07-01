"""
Auto-generated AutoGen Team: UnnamedProject
Objectives:
  - : Ensure tasks have an estimated duration to help with planning and prioritization.
  - : Guarantee that the user's todo list state is saved every interaction, per agent instruction.
Capabilities:
  - manage todo list: Ability to create, update, list, and complete todo items.
  - timebox tasks: Ability to ask the user for estimated durations and enforce timeboxing of tasks.
  - save memory every response: Requirement to persist working memory in every interaction to prevent forgetting between turns.
  - format and render list with emojis and subtasks: Ability to render todo lists with emojis, date fields, indexed titles, descriptions, statuses, and nested subtasks using boxed bullet lists.
Resources:
  - : External identifier passed to the agent as resourceId (represents the user-specific resource used for memory/session association in the source). Note: value originates in the code as the constant 'SOME_USER_ID'.
  - : Representative threadId used in the runtime example. Modeled as a resource instance to preserve the runtime identifier.
  - : The working memory representation that the agent is expected to produce and save in every response inside <working_memory> blocks. Initially seeded with the template below (exact string taken from source memory configuration):

# Todo List
## Active Items
- Example (Due: Feb 7 3028, Started: Feb 7 2025)
  - Description: This is an example task - replace with whatever the user needs

## Completed Items
- None yet
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


# ==================================================
# Agents
# ==================================================


todo_agent = AssistantAgent(
    name="todo_agent",
    model_client=model_client,
    system_message="""
Role:
todolist manager

Goal:
todolist manager

Background:
You are a todolist manager.
""",
)



