"""
Auto-generated AutoGen Team: MarketingPostsCrewTeam
Goals:
  - Marketing project goal: Boost awareness and adoption of CrewAI's services among enterprise clients. Create a comprehensive marketing campaign focusing on ease of use, scalability, and integration capabilities.
  - Lead Market Analyst personal goal: Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
  - Chief Marketing Strategist personal goal: Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
  - Creative Content Creator personal goal: Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.
Objectives:
  - Produce campaign ideas: Objective: generate creative campaign ideas for the marketing project.
Capabilities:
  - web search capability: Capability to perform web searches and retrieve online information (used by SerperDevTool).
  - web scraping capability: Capability to scrape website content and extract structured information.
  - analyze market: Capability to research and analyze markets, competitors, and customers.
  - formulate strategy: Capability to synthesize analysis into strategic plans and marketing strategies.
  - create content: Capability to produce creative campaign ideas and marketing copy.
Resources:
  - Research Report (resource): Output of research_task: A complete report on the customer and their customers and competitors, including demographics, preferences, market positioning and audience engagement.
  - Project Summary (resource): Output of project_understanding_task: A detailed summary of the project and a profile of the target audience.
  - MarketStrategy (resource): Represents the MarketStrategy output (pydantic model):
Fields:
- name: str
- tatics: List[str]
- channels: List[str]
- KPIs: List[str]
From campaign: expected output: a detailed marketing strategy including name, tactics, channels, and KPIs.
  - CampaignIdea (resource): Represents campaign idea outputs (pydantic model):
Fields:
- name: str
- description: str
- audience: str
- channel: str
Expected: 5 campaign ideas with brief descriptions and expected impact.
  - Copy (resource): Represents copy outputs (pydantic model):
Fields:
- title: str
- body: str
Marketing copies for each campaign idea.
  - marketing_posts source: Original source code and configuration files (crew.py, main.py, config/agents.yaml, config/tasks.yaml) used to define the crew, agents, tasks, tools, and inputs. This ontology encodes semantic representation of that solution.
  - participation example: Example: lead_market_analyst_agent participated in research_task.
  - participation example: Example: chief_marketing_strategist_agent participated in marketing_strategy_task and project_understanding_task.
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


def serper_dev_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SerperDevTool

    Description:
    Third-party web search / SERP tool used by agents for lookups. Instantiated in code as SerperDevTool().
    """
    return (
        "Tool 'serper_dev_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


serper_dev_tool = FunctionTool(
    serper_dev_tool_impl,
    description="""Third-party web search / SERP tool used by agents for lookups. Instantiated in code as SerperDevTool()."""
)


def scrape_website_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ScrapeWebsiteTool

    Description:
    Tool for scraping website contents; used by agents to gather site-specific information. Instantiated in code as ScrapeWebsiteTool().
    """
    return (
        "Tool 'scrape_website_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


scrape_website_tool = FunctionTool(
    scrape_website_tool_impl,
    description="""Tool for scraping website contents; used by agents to gather site-specific information. Instantiated in code as ScrapeWebsiteTool()."""
)


# ==================================================
# Agents
# ==================================================


lead_market_analyst = AssistantAgent(
    name="lead_market_analyst",
    model_client=model_client,
    system_message="""
Role:
Lead Market Analyst

Goal:
Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.

Background:
Role and backstory for agent
""",
)


chief_marketing_strategist = AssistantAgent(
    name="chief_marketing_strategist",
    model_client=model_client,
    system_message="""
Role:
Chief Marketing Strategist

Goal:
Synthesize amazing insights from product analysis to formulate incredible marketing strategies.

Background:
Role and backstory for agent
""",
)


creative_content_creator = AssistantAgent(
    name="creative_content_creator",
    model_client=model_client,
    system_message="""
Role:
Creative Content Creator

Goal:
Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.

Background:
Role and backstory for agent
""",
)



