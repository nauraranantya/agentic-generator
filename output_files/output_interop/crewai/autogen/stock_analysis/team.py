"""
Auto-generated AutoGen Team: StockAnalysisCrew
Goals:
  - Stock analysis overall goal: Conduct stock and filings analysis pipeline that collects news, analyzes EDGAR filings, computes key financial metrics and produces investment recommendations.
Capabilities:
  - web scraping: Capability to fetch and extract textual content from web pages.
  - website search: Capability to search web content and return links or content snippets (site-level search).
  - mathematical calculation: Numeric computation capability (safe evaluation of arithmetic expressions).
  - SEC 10-K semantic search: Semantic search over the latest 10-K filing content for a specified company ticker.
  - SEC 10-Q semantic search: Semantic search over the latest 10-Q filing content for a specified company ticker.
Resources:
  - News summary resource: Resource representing aggregated news, press releases and market analysis text collected by the Research task using web search and scraping tools.
  - Financial analysis report resource: Resource representing the final financial analysis report produced by financial_analysis task. Expected to include metrics and narrative assessment.
  - Filings analysis report resource: Report summarizing important findings from EDGAR filings (10-K, 10-Q) including flagged items and extracted metrics.
  - Investment recommendation report: Final recommendation report produced by recommend task, combining financial, news and filings analyses.
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


def tool_calculator_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    CalculatorTool

    Description:
    Calculator tool (from src/stock_analysis/tools/calculator_tool.py).
    Purpose: perform mathematical calculations expressed as arithmetic expressions (examples: '200*7', '5000/2*10').
    Implementation notes summarized: safe AST evaluation allowing operators + - * / ** % and unary +/-. Filters allowed characters using regex '^[0-9+\-*/().% ]+$'. Raises ValueError on invalid input or errors (syntax, division by zero, unsupported nodes).
    """
    return (
        "Tool 'tool_calculator' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_calculator = FunctionTool(
    tool_calculator_impl,
    description="""Calculator tool (from src/stock_analysis/tools/calculator_tool.py).
    Purpose: perform mathematical calculations expressed as arithmetic expressions (examples: '200*7', '5000/2*10').
    Implementation notes summarized: safe AST evaluation allowing operators + - * / ** % and unary +/-. Filters allowed characters using regex '^[0-9+\-*/().% ]+$'. Raises ValueError on invalid input or errors (syntax, division by zero, unsupported nodes)."""
)


def tool_scrape_website_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ScrapeWebsiteTool

    Description:
    Tool used to fetch and convert HTML pages into text for downstream processing. Referenced from crewai_tools usage in the crew.
    """
    return (
        "Tool 'tool_scrape_website' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_scrape_website = FunctionTool(
    tool_scrape_website_impl,
    description="""Tool used to fetch and convert HTML pages into text for downstream processing. Referenced from crewai_tools usage in the crew."""
)


def tool_website_search_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    WebsiteSearchTool

    Description:
    Tool used for general website search (referenced from crewai_tools in the crew).
    """
    return (
        "Tool 'tool_website_search' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_website_search = FunctionTool(
    tool_website_search_impl,
    description="""Tool used for general website search (referenced from crewai_tools in the crew)."""
)


def tool_txt_search_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    TXTSearchTool

    Description:
    Tool used for searching plaintext resources (referenced from crewai_tools in the crew).
    """
    return (
        "Tool 'tool_txt_search' "
        "is a generated stub and "
        "has not been implemented yet."
    )


tool_txt_search = FunctionTool(
    tool_txt_search_impl,
    description="""Tool used for searching plaintext resources (referenced from crewai_tools in the crew)."""
)


def sec10_k_tool_generic_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SEC10KToolgeneric

    Description:
    A RAG-style tool for semantic search in 10-K filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-K filing via the SEC API (sec_api.QueryApi using environment variable SEC_API_API_KEY), requests the filing details URL, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\s\n]' and adds resulting text to its internal RAG index (DataType.TEXT).
    """
    return (
        "Tool 'sec10_k_tool_generic' "
        "is a generated stub and "
        "has not been implemented yet."
    )


sec10_k_tool_generic = FunctionTool(
    sec10_k_tool_generic_impl,
    description="""A RAG-style tool for semantic search in 10-K filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-K filing via the SEC API (sec_api.QueryApi using environment variable SEC_API_API_KEY), requests the filing details URL, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\s\n]' and adds resulting text to its internal RAG index (DataType.TEXT)."""
)


def sec10_k_tool_amzn_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SEC10KToolAMZN

    Description:
    Instance of SEC10KTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-K, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10KToolSchema (only search_query required subsequently).
    """
    return (
        "Tool 'sec10_k_tool_amzn' "
        "is a generated stub and "
        "has not been implemented yet."
    )


sec10_k_tool_amzn = FunctionTool(
    sec10_k_tool_amzn_impl,
    description="""Instance of SEC10KTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-K, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10KToolSchema (only search_query required subsequently)."""
)


def sec10_q_tool_generic_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SEC10QToolgeneric

    Description:
    A RAG-style tool for semantic search in 10-Q filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-Q filing via the SEC API, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\s\n]' and adds resulting text to its internal index (DataType.TEXT).
    """
    return (
        "Tool 'sec10_q_tool_generic' "
        "is a generated stub and "
        "has not been implemented yet."
    )


sec10_q_tool_generic = FunctionTool(
    sec10_q_tool_generic_impl,
    description="""A RAG-style tool for semantic search in 10-Q filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-Q filing via the SEC API, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\s\n]' and adds resulting text to its internal index (DataType.TEXT)."""
)


def sec10_q_tool_amzn_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SEC10QToolAMZN

    Description:
    Instance of SEC10QTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-Q, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10QToolSchema (only search_query required subsequently).
    """
    return (
        "Tool 'sec10_q_tool_amzn' "
        "is a generated stub and "
        "has not been implemented yet."
    )


sec10_q_tool_amzn = FunctionTool(
    sec10_q_tool_amzn_impl,
    description="""Instance of SEC10QTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-Q, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10QToolSchema (only search_query required subsequently)."""
)


# ==================================================
# Agents
# ==================================================


financial_agent = AssistantAgent(
    name="financial_agent",
    model_client=model_client,
    system_message="""
Role:
The Best Financial Analyst

Goal:
The Best Financial Analyst

Background:
This prompt is used as the agent/system instruction for the financial agent to guide independent behaviour.
""",
)


financial_analyst_agent = AssistantAgent(
    name="financial_analyst_agent",
    model_client=model_client,
    system_message="""
Role:
The Best Financial Analyst

Goal:
The Best Financial Analyst

Background:
This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration).
""",
)


research_analyst_agent = AssistantAgent(
    name="research_analyst_agent",
    model_client=model_client,
    system_message="""
Role:
Staff Research Analyst

Goal:
Staff Research Analyst

Background:
System prompt for the research analyst agent.
""",
)


investment_advisor_agent = AssistantAgent(
    name="investment_advisor_agent",
    model_client=model_client,
    system_message="""
Role:
Private Investment Advisor

Goal:
Private Investment Advisor

Background:
System prompt for the investment advisor agent.
""",
)



