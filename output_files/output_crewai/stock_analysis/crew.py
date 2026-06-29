"""
Auto-generated CrewAI Crew: StockAnalysisCrew

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
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

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool

from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool, TXTSearchTool

# ===========================================================
# Tool Instances
# ===========================================================
# TODO: tool_calculator — unknown tool class "CalculatorTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("CalculatorTool")
def tool_calculator(*args, **kwargs) -> str:
    """Calculator tool (from src/stock_analysis/tools/calculator_tool.py).     Purpose: perform mathematica"""
    return "tool_calculator result"

tool_scrape_website = ScrapeWebsiteTool()
tool_website_search = WebsiteSearchTool()
tool_txt_search = TXTSearchTool()
# TODO: sec10_k_tool_generic — unknown tool class "SEC10KToolgeneric"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SEC10KToolgeneric")
def sec10_k_tool_generic(*args, **kwargs) -> str:
    """A RAG-style tool for semantic search in 10-K filings (class src/stock_analysis/tools/sec_tools.py). """
    return "sec10_k_tool_generic result"

# TODO: sec10_k_tool_amzn — unknown tool class "SEC10KToolAMZN"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SEC10KToolAMZN")
def sec10_k_tool_amzn(*args, **kwargs) -> str:
    """Instance of SEC10KTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's late"""
    return "sec10_k_tool_amzn result"

# TODO: sec10_q_tool_generic — unknown tool class "SEC10QToolgeneric"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SEC10QToolgeneric")
def sec10_q_tool_generic(*args, **kwargs) -> str:
    """A RAG-style tool for semantic search in 10-Q filings (class src/stock_analysis/tools/sec_tools.py). """
    return "sec10_q_tool_generic result"

# TODO: sec10_q_tool_amzn — unknown tool class "SEC10QToolAMZN"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SEC10QToolAMZN")
def sec10_q_tool_amzn(*args, **kwargs) -> str:
    """Instance of SEC10QTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's late"""
    return "sec10_q_tool_amzn result"


# ===========================================================
# Custom LLM
# ===========================================================
financial_agent_llm = LLM(model="ollama/llama3.1")
financial_analyst_agent_llm = LLM(model="ollama/llama3.1")
research_analyst_agent_llm = LLM(model="ollama/llama3.1")
investment_advisor_agent_llm = LLM(model="ollama/llama3.1")


@CrewBase
class StockAnalysisCrew:
    """StockAnalysisCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def financial_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_agent'],
            tools=[tool_calculator, tool_scrape_website, tool_website_search, sec10_k_tool_amzn, sec10_q_tool_amzn],
            llm=financial_agent_llm,
        )

    @agent
    def financial_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst_agent'],
            tools=[tool_calculator, tool_scrape_website, tool_website_search, sec10_k_tool_generic, sec10_q_tool_generic],
            llm=financial_analyst_agent_llm,
        )

    @agent
    def research_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst_agent'],
            tools=[tool_scrape_website, sec10_k_tool_amzn, sec10_q_tool_amzn],
            llm=research_analyst_agent_llm,
        )

    @agent
    def investment_advisor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['investment_advisor_agent'],
            tools=[tool_calculator, tool_scrape_website, tool_website_search],
            llm=investment_advisor_agent_llm,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research'],
            agent=self.research_analyst_agent(),
        )

    @task
    def filings_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['filings_analysis'],
            agent=self.financial_analyst_agent(),
        )

    @task
    def financial_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analysis'],
            agent=self.financial_analyst_agent(),
        )

    @task
    def recommend(self) -> Task:
        return Task(
            config=self.tasks_config['recommend'],
            agent=self.investment_advisor_agent(),
            context=[self.financial_analysis(), self.research(), self.filings_analysis()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the StockAnalysisCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
