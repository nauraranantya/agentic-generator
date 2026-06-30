"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Chef Agent Goal (Recipe Retrieval): Return a useful recipe given an ingredient and available tools/equipment.
Environments:
  - My Utility MCP Server (myMcpServerTwo) (): MCP server providing tools, agents, workflows, and weather resources.
  - My Calculation & Data MCP Server (myMcpServer) (): MCP server providing calculator and fetchWeather tools.
Capabilities:
  - Moderation Processor: ModerationProcessor configuration:
      - model: openai('gpt-4.1-nano')
      - categories: ['hate','harassment','violence']
      - threshold: 0.7
      - strategy: 'block'
      - purpose: detect and block inappropriate content
    Modeled as a Capability used by agents as input processor.
  - PII Detector: PII detection processor used to redact or mask PII; modeled as a capability.
  - Prompt Injection Detector: A prompt injection detector that can block malicious instructions (modeled as capability).
  - testScorer (scorer1): A scorer named scorer1 that returns a constant score 1 in the source. Used by Mastra as a scoring primitive.
  - Answer Relevancy Scorer: Prebuilt answer relevancy scorer (createAnswerRelevancyScorer) using openai('gpt-4o'). Used by evalAgent.
  - PII Detector (configured): Configured with openai('gpt-4o') in source and used as an input processor to redact PII.
  - Prompt Injection Detector (configured): Configured with google gemini model in source; blocks prompt injection.
Resources:
  - recipe-result: String output produced by recipe-maker workflow step (result: string).
  - weather://current: Real-time weather data for the current location (JSON). Example content includes location, temperature, humidity, windSpeed, updated timestamp.
  - weather://forecast: 5-day weather forecast (JSON array).
  - weather://historical: Historical metrics (averageHigh, averageLow, rainDays, sunnyDays, recordHigh, recordLow).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: cooking_tool — unknown tool class "cookingtool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("cookingtool")
def cooking_tool(*args, **kwargs) -> str:
    """Tool ID: cooking-tool     Description: Used to cook given an ingredient     Input schema (zod): { in"""
    return "cooking_tool result"

# TODO: weather_info_tool — unknown tool class "weatherinfo"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("weatherinfo")
def weather_info_tool(*args, **kwargs) -> str:
    """Tool ID: weather-info     Description: Fetches the current weather information for a given city.    """
    return "weather_info_tool result"

# TODO: calculator_tool — unknown tool class "calculator"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("calculator")
def calculator_tool(*args, **kwargs) -> str:
    """Tool ID: calculator     Description: Performs basic arithmetic operations (add, subtract).     Input"""
    return "calculator_tool result"

# TODO: fetch_weather_tool — unknown tool class "fetchWeather"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("fetchWeather")
def fetch_weather_tool(*args, **kwargs) -> str:
    """Tool ID: fetchWeather     Description: Simulated forecast for a city. Uses a simple mapping from cit"""
    return "fetch_weather_tool result"

# TODO: string_utils_tool — unknown tool class "stringUtils"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("stringUtils")
def string_utils_tool(*args, **kwargs) -> str:
    """Tool ID: stringUtils     Description: Performs utility operations on strings (uppercase, reverse).  """
    return "string_utils_tool result"

# TODO: greet_user_tool — unknown tool class "greetUser"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("greetUser")
def greet_user_tool(*args, **kwargs) -> str:
    """Tool ID: greetUser     Description: Generates a personalized greeting.     Input schema: { name: str"""
    return "greet_user_tool result"

# TODO: collect_contact_info_tool — unknown tool class "collectContactInfo"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("collectContactInfo")
def collect_contact_info_tool(*args, **kwargs) -> str:
    """Tool ID: collectContactInfo     Description: Collects user contact information through elicitation ("""
    return "collect_contact_info_tool result"




@CrewBase
class MastraSystem:
    """MastraSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def chef_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_agent'],
            tools=[cooking_tool, weather_info_tool],
        )

    @agent
    def chef_agent_responses(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_agent_responses'],
            tools=[cooking_tool, weather_info_tool],
        )

    @agent
    def chef_model_v2_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_model_v2_agent'],
            tools=[cooking_tool, weather_info_tool],
        )

    @agent
    def dynamic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['dynamic_agent'],
            tools=[cooking_tool],
        )

    @agent
    def agent_that_harasses_you(self) -> Agent:
        return Agent(
            config=self.agents_config['agent_that_harasses_you'],
        )

    @agent
    def error_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['error_agent'],
        )

    @agent
    def network_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['network_agent'],
            tools=[cooking_tool, weather_info_tool],
        )

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'],
            tools=[weather_info_tool],
        )

    @agent
    def eval_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['eval_agent'],
            tools=[weather_info_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_my_step(self) -> Task:
        return Task(
            config=self.tasks_config['task_my_step'],
            agent=self.chef_agent(),
        )

    @task
    def task_add_letter(self) -> Task:
        return Task(
            config=self.tasks_config['task_add_letter'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_step_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_one'],
            agent=self.dynamic_agent(),
        )

    @task
    def task_my_step_2(self) -> Task:
        return Task(
            config=self.tasks_config['task_my_step_2'],
            agent=self.chef_agent(),
        )

    @task
    def task_add_letter_b(self) -> Task:
        return Task(
            config=self.tasks_config['task_add_letter_b'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_step_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_two'],
            agent=self.dynamic_agent(),
        )

    @task
    def task_add_letter_c(self) -> Task:
        return Task(
            config=self.tasks_config['task_add_letter_c'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_step_three(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_three'],
            agent=self.dynamic_agent(),
        )

    @task
    def task_add_letter_with_count(self) -> Task:
        return Task(
            config=self.tasks_config['task_add_letter_with_count'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_step_four(self) -> Task:
        return Task(
            config=self.tasks_config['task_step_four'],
            agent=self.dynamic_agent(),
        )

    @task
    def task_suspend_resume(self) -> Task:
        return Task(
            config=self.tasks_config['task_suspend_resume'],
            agent=self.chef_agent(),
        )

    @task
    def task_short_text(self) -> Task:
        return Task(
            config=self.tasks_config['task_short_text'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_long_text(self) -> Task:
        return Task(
            config=self.tasks_config['task_long_text'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_nested_text_processor(self) -> Task:
        return Task(
            config=self.tasks_config['task_nested_text_processor'],
            agent=self.chef_model_v2_agent(),
        )

    @task
    def task_final_step(self) -> Task:
        return Task(
            config=self.tasks_config['task_final_step'],
            agent=self.chef_agent(),
        )

    @task
    def task_fetch_weather(self) -> Task:
        return Task(
            config=self.tasks_config['task_fetch_weather'],
        )

    @task
    def task_calculator(self) -> Task:
        return Task(
            config=self.tasks_config['task_calculator'],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MastraSystem"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
