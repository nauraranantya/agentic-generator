"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Goal representing the desired final state: a composed answer to the user that includes both current weather for requested location and current stock price for requested symbol.
Objectives:
  - : Objective grouping the sub-tasks needed to respond to the user (get weather, get stock price, compose reply).
Environments:
  -  (local): Describes the example execution environment where servers are spawned locally and an SSE endpoint is used for the weather tool.
Capabilities:
  - : Capability to fetch the most recent closing stock price for a provided stock symbol (getStockPrice).
  - : Capability to get current weather for a specified location (getWeather). Performs geocoding, then queries a weather API, and returns a structured JSON response.
Resources:
  - : External HTTP endpoint used by the stock price tool: https://mastra-stock-data.vercel.app/api/stock-data?symbol=<SYMBOL>. Tool parses JSON and extracts 'prices["4. close"]' as the returned price.
  - : External weather API used to retrieve current weather values. The weather tool queries this API for fields: temperature_2m, apparent_temperature, relative_humidity_2m, wind_speed_10m, wind_gusts_10m, weather_code.
  - : Geocoding service used to map a location name to latitude/longitude: https://geocoding-api.open-meteo.com/v1/search?name=<location>&count=1
  - : Resource produced by getWeather: JSON object with fields:
- temperature: number
- feelsLike: number
- humidity: number
- windSpeed: number
- windGust: number
- conditions: string (derived from weather_code)
- location: string
This resource is produced by the getWeather tool and consumed by the agent for final response composition.
  - : Resource produced by getStockPrice: JSON object with fields:
- symbol: string
- currentPrice: number
This resource is produced by the getStockPrice tool and consumed by the agent for final response composition.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: stock_price_tool — unknown tool class "stockPriceTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("stockPriceTool")
def stock_price_tool(*args, **kwargs) -> str:
    """Tool exposing a single capability 'getStockPrice'. It fetches the last day's closing stock price for"""
    return "stock_price_tool result"

# TODO: weather_tool — unknown tool class "weatherTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("weatherTool")
def weather_tool(*args, **kwargs) -> str:
    """Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an exte"""
    return "weather_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def stock_weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_weather_agent'],
            tools=[stock_price_tool, weather_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def user_request_task(self) -> Task:
        return Task(
            config=self.tasks_config['user_request_task'],
        )

    @task
    def get_weather_task(self) -> Task:
        return Task(
            config=self.tasks_config['get_weather_task'],
        )

    @task
    def get_stock_price_task(self) -> Task:
        return Task(
            config=self.tasks_config['get_stock_price_task'],
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
