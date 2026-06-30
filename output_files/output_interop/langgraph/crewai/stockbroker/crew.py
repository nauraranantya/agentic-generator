"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Get stock information and perform trades: Goal: Provide stock price information to the user, show portfolio details on request, and facilitate buy orders when requested by user.
Environments:
  - Trading Environment (virtual): Operational environment context for the Stockbroker agent (uses external financial datasets API).
Capabilities:
  - Get stock prices: Capability to query historical and recent market prices for a given ticker.
  - Get portfolio: Capability to retrieve the user's portfolio details.
  - Buy stock: Capability to initiate a purchase action for a given stock and quantity.
Resources:
  - FINANCIAL_DATASETS_API_KEY (env var): Environment variable required by the agent to access the financial datasets API (FINANCIAL_DATASETS_API_KEY).
  - LLM message: The assistant message returned by the LLM invocation. May include content, and tool_calls array with each tool call having an id, name, and args object. This resource is pushed to the UI along with UI items representing tool outputs.
  - UI items: A list of UI items produced by the agent to present results (e.g., chart for prices, portfolio view, buy confirmation). Modeled here as a resource produced by the CallToolsTask.
  - oneDayPrices: Array of Price entries for a single day. Retrieved from https://api.financialdatasets.ai/prices with interval=minute and interval_multiplier=5, start_date=end_date=today, limit=5000.
  - thirtyDayPrices: Array of Price entries covering up to 30 days. Retrieved from https://api.financialdatasets.ai/prices with interval=minute and interval_multiplier=30; may require pagination following next_page_url to collect additional pages.
  - snapshot: Snapshot object returned by https://api.financialdatasets.ai/prices/snapshot for a requested ticker. Used by the buy-stock UI item to present price at purchase time.
  - portfolio UI: UI representation of the user's portfolio produced when the portfolio tool is invoked.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: tool_stock_price — unknown tool class "stockprice"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("stockprice")
def tool_stock_price(*args, **kwargs) -> str:
    """A tool to get the stock price of a company. Invoked with argument { ticker: string }. When called, t"""
    return "tool_stock_price result"

# TODO: tool_portfolio — unknown tool class "portfolio"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("portfolio")
def tool_portfolio(*args, **kwargs) -> str:
    """A tool to get the user's portfolio details. Only called when the user explicitly requests portfolio """
    return "tool_portfolio result"

# TODO: tool_buy_stock — unknown tool class "buystock"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("buystock")
def tool_buy_stock(*args, **kwargs) -> str:
    """A tool to buy a stock. Invoked with arguments { ticker: string, quantity: number }. When called, the"""
    return "tool_buy_stock result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def stockbroker_01(self) -> Agent:
        return Agent(
            config=self.agents_config['stockbroker_01'],
            tools=[tool_stock_price, tool_portfolio, tool_buy_stock],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def call_tools(self) -> Task:
        return Task(
            config=self.tasks_config['call_tools'],
            agent=self.stockbroker_01(),
        )

    @task
    def get_prices_for_ticker(self) -> Task:
        return Task(
            config=self.tasks_config['get_prices_for_ticker'],
        )

    @task
    def get_price_snapshot_for_ticker(self) -> Task:
        return Task(
            config=self.tasks_config['get_price_snapshot_for_ticker'],
        )

    @task
    def get_portfolio(self) -> Task:
        return Task(
            config=self.tasks_config['get_portfolio'],
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
