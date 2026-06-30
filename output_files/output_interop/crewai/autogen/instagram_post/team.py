"""
Auto-generated AutoGen Team: CopyCrew
Goals:
  - Marketing Campaign Objective: Overarching objective: produce Instagram post copy and photograph concepts that highlight the product, its unique selling points, and create a high-impact campaign.
Objectives:
  - Copy Crew Objective: Generate analysis-informed ad copy and campaign strategy to drive engagement.
  - Image Crew Objective: Create photograph concepts aligned with ad copy and campaign to produce visuals for Instagram.
Capabilities:
  - web scraping: Capability to scrape and summarize website content.
  - internet search: Capability to search the internet and summarize results.
  - instagram search: Capability to search Instagram posts (site:instagram.com queries).
  - strategy planning: Capability to synthesize analysis into marketing strategies.
  - copywriting: Capability to craft punchy Instagram ad copy.
  - photography review: Capability to evaluate and revise photograph concepts.
  - review & approval: Capability to review outputs, approve, and delegate follow-ups.
Resources:
  - Product Analysis Report: Textual report produced by product_analysis task: detailed product features, market appeal, recommendations.
  - Competitor Analysis Report: Textual competitor analysis with top-3 competitor comparisons produced by competitor_analysis task.
  - Campaign Strategy & Ideas: Marketing strategy and creative content ideas produced by campaign_development task. Used by creative and photography agents.
  - Ad Copy Options (3 variations): Three Instagram ad copy options produced by instagram_ad_copy task.
  - Photograph Descriptions (3 options): Three photograph concept descriptions produced by take_photograph_task.
  - Approved Photograph Descriptions: Reviewed and approved (or delegated) photograph descriptions produced by review_photo task.
  - tasks.py (semantic summary): Contains prompt texts (task descriptions) for product_analysis, competitor_analysis, campaign_development, instagram_ad_copy, take_photograph_task, review_photo. Task prompts preserved as Prompt individuals and Task dct:description values.
  - agents.py (semantic summary): Defines agents (roles, goals, backstories), their tool sets, and association to the Ollama language model. Represented as LLMAgent individuals with agent prompts and useLanguageModel links.
  - main.py (semantic summary): Orchestrates two Crews (Copy Crew and Image Crew). Copy Crew runs tasks: product_analysis, competitor_analysis, campaign_development, instagram_ad_copy. Image Crew runs tasks: take_photograph_task, review_photo. Crew orchestration and kickoff semantics not directly modeled; outputs represented as produced Resources.
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


def tool_browser_tools_scrape_and_summarize_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    BrowserToolsscrapeandsummarizewebsite

    Description:
    Semantic purpose: Scrape a website and produce a long summary of its content or content chunks.
Input: full URL string (e.g., https://example.com).
Outputs: textual scrapped content and summaries (used as context for agents/tasks).
Configuration: requires a Browserless API key (SERPER/BROWSERLESS keys are present in Config entries).
Note: Implementation uses HTML partitioning into chunks and summary generation per chunk; we capture purpose and required config here.
    """
    return (
        "Tool 'tool_browser_tools_scrape_and_summarize' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_browser_tools_scrape_and_summarize = FunctionTool(
    tool_browser_tools_scrape_and_summarize_impl,
    description="""Semantic purpose: Scrape a website and produce a long summary of its content or content chunks.
Input: full URL string (e.g., https://example.com).
Outputs: textual scrapped content and summaries (used as context for agents/tasks).
Configuration: requires a Browserless API key (SERPER/BROWSERLESS keys are present in Config entries).
Note: Implementation uses HTML partitioning into chunks and summary generation per chunk; we capture purpose and required config here."""
)


def tool_search_tools_search_internet_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchToolssearchinternet

    Description:
    Semantic purpose: Search the Internet (generic web search) and return top organic results, title, link, snippet.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key.
    """
    return (
        "Tool 'tool_search_tools_search_internet' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_tools_search_internet = FunctionTool(
    tool_search_tools_search_internet_impl,
    description="""Semantic purpose: Search the Internet (generic web search) and return top organic results, title, link, snippet.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key."""
)


def tool_search_tools_search_instagram_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchToolssearchinstagram

    Description:
    Semantic purpose: Search Instagram via site-limited search (site:instagram.com) to find relevant posts.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key.
    """
    return (
        "Tool 'tool_search_tools_search_instagram' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_search_tools_search_instagram = FunctionTool(
    tool_search_tools_search_instagram_impl,
    description="""Semantic purpose: Search Instagram via site-limited search (site:instagram.com) to find relevant posts.
Input: query string.
Configuration: uses SERPER_API_KEY (search service) as an API key."""
)


# ==================================================
# Agents
# ==================================================


product_competitor_agent = AssistantAgent(
    name="product_competitor_agent",
    model_client=model_client,
    system_message="""
Role:
Lead Market Analyst

Goal:
Lead Market Analyst

Background:
Agent backstory and role description for Lead Market Analyst
""",
)


strategy_planner_agent = AssistantAgent(
    name="strategy_planner_agent",
    model_client=model_client,
    system_message="""
Role:
Chief Marketing Strategist

Goal:
Chief Marketing Strategist

Background:
Agent backstory and role description for Chief Marketing Strategist
""",
)


creative_content_creator_agent = AssistantAgent(
    name="creative_content_creator_agent",
    model_client=model_client,
    system_message="""
Role:
Creative Content Creator

Goal:
Creative Content Creator

Background:
Agent backstory and role description for Creative Content Creator
""",
)


senior_photographer_agent = AssistantAgent(
    name="senior_photographer_agent",
    model_client=model_client,
    system_message="""
Role:
Senior Photographer

Goal:
Senior Photographer

Background:
Agent backstory and role description for Senior Photographer
""",
)


chief_creative_director_agent = AssistantAgent(
    name="chief_creative_director_agent",
    model_client=model_client,
    system_message="""
Role:
Chief Creative Director

Goal:
Chief Creative Director

Background:
Agent backstory and role description for Chief Creative Director
""",
)



