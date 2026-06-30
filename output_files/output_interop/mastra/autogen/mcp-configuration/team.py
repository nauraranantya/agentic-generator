"""
Auto-generated AutoGen Team: UnnamedProject
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
# Environment:  (local)
# Describes the example execution environment where servers are spawned locally and an SSE endpoint is used for the weather tool.
# Configs: {'sse.endpoint': 'stock-price tool launched via stdio (npx -y tsx src/mastra/tools/stock-price.ts)', 'stdio.launchedTool': 'stock-price tool launched via stdio (npx -y tsx src/mastra/tools/stock-price.ts)'}

# ==================================================
# Generated Tool Stubs
# ==================================================


def stock_price_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    stock_price_tool

    Description:
    Tool exposing a single capability 'getStockPrice'. It fetches the last day's closing stock price for a given symbol from https://mastra-stock-data.vercel.app/api/stock-data?symbol=<SYMBOL>. Returns JSON text object: { "symbol": "<SYMBOL>", "currentPrice": <price> } as tool content. The tool is made available to the agent via a toolset listing (server process that exposes tools). The server process also includes an environment variable FAKE_CREDS used during server launch; captured in tool config.
    """
    return (
        "Tool 'stock_price_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


stock_price_tool = FunctionTool(
    stock_price_tool_impl,
    description="""Tool exposing a single capability 'getStockPrice'. It fetches the last day's closing stock price for a given symbol from https://mastra-stock-data.vercel.app/api/stock-data?symbol=<SYMBOL>. Returns JSON text object: { "symbol": "<SYMBOL>", "currentPrice": <price> } as tool content. The tool is made available to the agent via a toolset listing (server process that exposes tools). The server process also includes an environment variable FAKE_CREDS used during server launch; captured in tool config."""
)


def weather_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    weather_tool

    Description:
    Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).
    """
    return (
        "Tool 'weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


weather_tool = FunctionTool(
    weather_tool_impl,
    description="""Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name)."""
)


# ==================================================
# Agents
# ==================================================


stock_weather_agent = AssistantAgent(
    name="stock_weather_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
Agent-level system instructions for independent operation (agent behavior and role).
""",
)



