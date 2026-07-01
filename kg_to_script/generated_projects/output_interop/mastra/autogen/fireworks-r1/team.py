
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


example_agent = AssistantAgent(
    name="example_agent",
    model_client=model_client,
    system_message="""
Role:
assistant

Goal:
assistant

Background:
System-level instruction (agent 'instructions' argument)
""",
)



team = RoundRobinGroupChat(
    participants=[
        example_agent,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
Template representing an interactive chat turn processed in the main loop (in chat.ts). For each user input, the code calls agent.stream(answer, { threadId, resourceId }) and consumes the returned textStream. The streaming output is masked and decorated for display (think tags and spinner). This Task is performed by the ExampleAgent and consumes a UserInput resource and produces a TextResponse resource.

Expected Output:
Completed: chat_interaction_task

"""
