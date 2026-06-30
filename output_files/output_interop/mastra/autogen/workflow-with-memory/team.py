
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
# Environment:  ()
# 
# Configs: {'logger.level': 'debug'}

# ==================================================
# Generated Tool Stubs
# ==================================================


def cat_fact_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    cat_fact_tool

    Description:
    
    """
    return (
        "Tool 'cat_fact_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


cat_fact_tool = FunctionTool(
    cat_fact_tool_impl,
    description=""""""
)


# ==================================================
# Agents
# ==================================================


cat_one = AssistantAgent(
    name="cat_one",
    model_client=model_client,
    system_message="""
Role:
feline expert

Goal:
feline expert

Background:
Agent role and long-form instructions provided in Agent instantiation (instructions in source code).
""",
)



