"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - fetch-current-weather: Capability to obtain current weather information for a specified location by calling geocoding and weather APIs and mapping the response to a structured output.
Resources:
  - open-meteo geocoding API: Used to translate a location name into coordinates (latitude, longitude) and normalized name.
  - open-meteo forecast API: Used to fetch current weather metrics including temperature_2m, apparent_temperature, relative_humidity_2m, wind_speed_10m, wind_gusts_10m, weather_code.
  - WeatherData: Structured weather data produced by the 'Fetch current weather' task/tool. Fields:
- temperature: number (°C) from temperature_2m
- feelsLike: number (°C) from apparent_temperature
- humidity: number (%) from relative_humidity_2m
- windSpeed: number (m/s) from wind_speed_10m
- windGust: number (m/s) from wind_gusts_10m
- conditions: string (mapped from weather_code)
- location: string (normalized place name from geocoding result)
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: get_weather_tool — unknown tool class "getweather"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("getweather")
def get_weather_tool(*args, **kwargs) -> str:
    """Get current weather for a location"""
    return "get_weather_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[get_weather_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def fetch_current_weather(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_current_weather'],
            agent=self.weather_agent(),
        )

    @task
    def weather_agent_participation_placeholder(self) -> Task:
        return Task(
            config=self.tasks_config['weather_agent_participation_placeholder'],
            agent=self.weather_agent(),
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
