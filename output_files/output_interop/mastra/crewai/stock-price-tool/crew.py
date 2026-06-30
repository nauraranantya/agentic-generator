"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - Fetch stock price capability: Capability to retrieve a last-close stock price for a given ticker symbol.
Resources:
  - : External HTTP API endpoint used by the tool: https://mastra-stock-data.vercel.app/api/stock-data?symbol={symbol}. Modeled as a Resource the tool consumes.
  - : The ticker symbol used as input in the example query (AAPL). The task prompt contains promptInputData 'AAPL'.
  - : A numeric price value produced by executing the FetchStockPriceTask via the stockPrices tool. The tool returns a JSON object with key currentPrice mapped from the remote API (data.prices['4. close']). Value at runtime is not part of source code; this individual models the produced resource shape and label 'currentPrice'.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: stock_prices_tool — unknown tool class "GetStockPricestockPrices"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("GetStockPricestockPrices")
def stock_prices_tool(*args, **kwargs) -> str:
    """Fetches the last day's closing stock price for a given symbol. Source tool implementation uses an HT"""
    return "stock_prices_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def stock_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_agent'],
            tools=[stock_prices_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def fetch_stock_price_for_symbol_aapl_example(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_stock_price_for_symbol_aapl_example'],
            agent=self.stock_agent(),
        )

    @task
    def index_ts(self) -> Task:
        return Task(
            config=self.tasks_config['index_ts'],
            agent=self.stock_agent(),
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the UnnamedProject"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
