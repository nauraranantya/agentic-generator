
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


def openai_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    OpenAISDKtool

    Description:
    Representing the usage of the OpenAI SDK via openai(...) calls in the source code.
    """
    return (
        "Tool 'openai_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


openai_tool = FunctionTool(
    openai_tool_impl,
    description="""Representing the usage of the OpenAI SDK via openai(...) calls in the source code."""
)


def mongo_db_store_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    MongoDBStoretool

    Description:
    Storage backend used by Memory.storage in code (MongoDBStore). The code uses process.env.MONGODB_URI and dbName.
    """
    return (
        "Tool 'mongo_db_store' "
        "is a generated stub and "
        "has not been implemented yet."
    )


mongo_db_store = FunctionTool(
    mongo_db_store_impl,
    description="""Storage backend used by Memory.storage in code (MongoDBStore). The code uses process.env.MONGODB_URI and dbName."""
)


def mongo_db_vector_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    MongoDBVectorvectorstoretool

    Description:
    Vector store used for semantic recall via MongoDB-backed vectors (MongoDBVector).
    """
    return (
        "Tool 'mongo_db_vector' "
        "is a generated stub and "
        "has not been implemented yet."
    )


mongo_db_vector = FunctionTool(
    mongo_db_vector_impl,
    description="""Vector store used for semantic recall via MongoDB-backed vectors (MongoDBVector)."""
)


# ==================================================
# Agents
# ==================================================


chef_agent = AssistantAgent(
    name="chef_agent",
    model_client=model_client,
    system_message="""
Role:
chef

Goal:
chef

Background:
You are a chef.
""",
)


memory_agent = AssistantAgent(
    name="memory_agent",
    model_client=model_client,
    system_message="""
Role:
memory

Goal:
memory

Background:
You are a memory.
""",
)



team = RoundRobinGroupChat(
    participants=[
        chef_agent,
        memory_agent,
    ],
    termination_condition=MaxMessageTermination(
        max_messages=10
    )
)

TASK_PROMPT = """

Task:
In my kitchen I have: pasta, canned tomatoes, garlic, olive oil, and some dried herbs (basil and oregano). What can I make? Please keep your answer brief, only give me the high level steps.

Expected Output:
Completed: chef_initial_recipe_suggestion_task


Task:
Now I'm over at my friend's house, and they have: chicken thighs, coconut milk, sweet potatoes, and some curry powder.

Expected Output:
Completed: chef_friend_s_ingredients_recipe_suggestion_task


Task:
What did we cook before I went to my friends house?

Expected Output:
Completed: chef_memory_query_task_asks_what_was_cooked_earlier


Task:
Chat with user started now ${new Date().toISOString()}. Don't mention this message. This means some time may have passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.

Expected Output:
Completed: chat_initial_system_message_task


Task:
Chat Interactive Loop Task

Expected Output:
Completed: chat_interactive_loop_task

"""
