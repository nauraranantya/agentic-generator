"""
Auto-generated AutoGen Team: MeetingPreparationCrew
Goals:
  - Prepare meeting briefing and strategy: Prepare comprehensive research, industry analysis, strategic talking points, and a concise briefing document to support an upcoming meeting. This goal represents the overall purpose of the Meeting Preparation Crew created in main.py.
  - : Conduct thorough research on people and companies involved in the meeting
  - : Analyze the current industry trends, challenges, and opportunities relevant to the meeting context
  - : Develop talking points, questions, and strategic angles for the meeting
  - : Compile research, analysis, and strategy into a concise briefing document
Capabilities:
  - Exa.search: Search for webpages using a query and return top results (num_results=3).
  - Exa.find_similar: Find webpages similar to a given URL (num_results=3).
  - Exa.get_contents: Retrieve page contents for a list of ids. Handles JSON or Python literal lists input;
validates input is a list of string ids; returns extracted contents (first ~1000 chars per segment).
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


def exa_search_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ExaSearchTool

    Description:
    Tool wrapping Exa (exa_py) search capabilities used by agents.
Provides three main operations: search(query), find_similar(url), and get_contents(ids).
The tool requires an EXA_API_KEY configuration value to access Exa APIs.
    """
    return (
        "Tool 'exa_search_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


exa_search_tool = FunctionTool(
    exa_search_tool_impl,
    description="""Tool wrapping Exa (exa_py) search capabilities used by agents.
Provides three main operations: search(query), find_similar(url), and get_contents(ids).
The tool requires an EXA_API_KEY configuration value to access Exa APIs."""
)


# ==================================================
# Agents
# ==================================================


researcher_agent_1 = AssistantAgent(
    name="researcher_agent_1",
    model_client=model_client,
    system_message="""
Role:
Research Specialist

Goal:
Conduct thorough research on people and companies involved in the meeting

Background:
Role: Research Specialist; Goal: Conduct thorough research on people and companies involved in the meeting
""",
)


industry_analyst_agent_1 = AssistantAgent(
    name="industry_analyst_agent_1",
    model_client=model_client,
    system_message="""
Role:
Industry Analyst

Goal:
Analyze the current industry trends, challenges, and opportunities relevant to the meeting context

Background:
Role: Industry Analyst; Goal: Analyze industry trends and opportunities
""",
)


meeting_strategy_agent_1 = AssistantAgent(
    name="meeting_strategy_agent_1",
    model_client=model_client,
    system_message="""
Role:
Meeting Strategy Advisor

Goal:
Develop talking points, questions, and strategic angles for the meeting

Background:
Role: Meeting Strategy Advisor; Goal: Develop talking points and strategies
""",
)


briefing_coordinator_agent_1 = AssistantAgent(
    name="briefing_coordinator_agent_1",
    model_client=model_client,
    system_message="""
Role:
Briefing Coordinator

Goal:
Compile research, analysis, and strategy into a concise briefing document

Background:
Role: Briefing Coordinator; Goal: Compile information into briefing document
""",
)



