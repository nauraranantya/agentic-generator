"""
Auto-generated AutoGen Team: MastraSystem
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
# Environment: My Utility MCP Server (myMcpServerTwo) ()
# MCP server providing tools, agents, workflows, and weather resources.
# Environment: My Calculation & Data MCP Server (myMcpServer) ()
# MCP server providing calculator and fetchWeather tools.

# ==================================================
# Generated Tool Stubs
# ==================================================


def cooking_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    cookingtool

    Description:
    Tool ID: cooking-tool
    Description: Used to cook given an ingredient
    Input schema (zod): { ingredient: string }
    Behavior: Simulated long-running operation (sleep ~5000ms). Logs the ingredient and returns 'My tool result'.
    Note: When available, context.agent.toolCallId is logged by the tool for tracing.
    """
    return (
        "Tool 'cooking_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


cooking_tool = FunctionTool(
    cooking_tool_impl,
    description="""Tool ID: cooking-tool
    Description: Used to cook given an ingredient
    Input schema (zod): { ingredient: string }
    Behavior: Simulated long-running operation (sleep ~5000ms). Logs the ingredient and returns 'My tool result'.
    Note: When available, context.agent.toolCallId is logged by the tool for tracing."""
)


def weather_info_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    weatherinfo

    Description:
    Tool ID: weather-info
    Description: Fetches the current weather information for a given city.
    Input schema: { city: string }
    Returns: an object with city, weather, temperature_celsius, temperature_fahrenheit, humidity, wind.
    """
    return (
        "Tool 'weather_info_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


weather_info_tool = FunctionTool(
    weather_info_tool_impl,
    description="""Tool ID: weather-info
    Description: Fetches the current weather information for a given city.
    Input schema: { city: string }
    Returns: an object with city, weather, temperature_celsius, temperature_fahrenheit, humidity, wind."""
)


def calculator_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    calculator

    Description:
    Tool ID: calculator
    Description: Performs basic arithmetic operations (add, subtract).
    Input schema: { num1: number, num2: number, operation: 'add'|'subtract' }
    Output: numeric result.
    """
    return (
        "Tool 'calculator_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


calculator_tool = FunctionTool(
    calculator_tool_impl,
    description="""Tool ID: calculator
    Description: Performs basic arithmetic operations (add, subtract).
    Input schema: { num1: number, num2: number, operation: 'add'|'subtract' }
    Output: numeric result."""
)


def fetch_weather_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    fetchWeather

    Description:
    Tool ID: fetchWeather
    Description: Simulated forecast for a city. Uses a simple mapping from city to temperature string.
    Input schema: { city: string }
    Output: string describing weather (e.g., 'The weather in X is 20°C and sunny.').
    """
    return (
        "Tool 'fetch_weather_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


fetch_weather_tool = FunctionTool(
    fetch_weather_tool_impl,
    description="""Tool ID: fetchWeather
    Description: Simulated forecast for a city. Uses a simple mapping from city to temperature string.
    Input schema: { city: string }
    Output: string describing weather (e.g., 'The weather in X is 20°C and sunny.')."""
)


def string_utils_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    stringUtils

    Description:
    Tool ID: stringUtils
    Description: Performs utility operations on strings (uppercase, reverse).
    Input schema: { text: string, action: 'uppercase'|'reverse' }
    Output: transformed text.
    Note: Source code had a small bug (used inputData variable in execute); semantic behavior preserved here.
    """
    return (
        "Tool 'string_utils_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


string_utils_tool = FunctionTool(
    string_utils_tool_impl,
    description="""Tool ID: stringUtils
    Description: Performs utility operations on strings (uppercase, reverse).
    Input schema: { text: string, action: 'uppercase'|'reverse' }
    Output: transformed text.
    Note: Source code had a small bug (used inputData variable in execute); semantic behavior preserved here."""
)


def greet_user_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    greetUser

    Description:
    Tool ID: greetUser
    Description: Generates a personalized greeting.
    Input schema: { name: string }
    Output: greeting string 'Hello, {name}! Welcome to the MCP server.'
    """
    return (
        "Tool 'greet_user_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


greet_user_tool = FunctionTool(
    greet_user_tool_impl,
    description="""Tool ID: greetUser
    Description: Generates a personalized greeting.
    Input schema: { name: string }
    Output: greeting string 'Hello, {name}! Welcome to the MCP server.'"""
)


def collect_contact_info_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    collectContactInfo

    Description:
    Tool ID: collectContactInfo
    Description: Collects user contact information through elicitation (interactive).
    Input schema: { reason?: string }
    Behavior:
      - Calls MCP elicitation session to send a request with JSON schema (name, email, phone).
      - Waits for user response via an elicitation handler. Interprets actions: accept/reject/cancel.
      - Returns a string summarizing collection outcome or an error.
    Elicitation requestedSchema (JSON):
      {
        type: 'object',
        properties: {
          name: { type: 'string', title: 'Full Name', description: 'Your full name' },
          email: { type: 'string', title: 'Email Address', description: 'Your email address', format: 'email' },
          phone: { type: 'string', title: 'Phone Number', description: 'Your phone number (optional)' }
        },
        required: ['name','email']
      }
    """
    return (
        "Tool 'collect_contact_info_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


collect_contact_info_tool = FunctionTool(
    collect_contact_info_tool_impl,
    description="""Tool ID: collectContactInfo
    Description: Collects user contact information through elicitation (interactive).
    Input schema: { reason?: string }
    Behavior:
      - Calls MCP elicitation session to send a request with JSON schema (name, email, phone).
      - Waits for user response via an elicitation handler. Interprets actions: accept/reject/cancel.
      - Returns a string summarizing collection outcome or an error.
    Elicitation requestedSchema (JSON):
      {
        type: 'object',
        properties: {
          name: { type: 'string', title: 'Full Name', description: 'Your full name' },
          email: { type: 'string', title: 'Email Address', description: 'Your email address', format: 'email' },
          phone: { type: 'string', title: 'Phone Number', description: 'Your phone number (optional)' }
        },
        required: ['name','email']
      }"""
)


# ==================================================
# Agents
# ==================================================


chef_agent = AssistantAgent(
    name="chef_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
Return a useful recipe given an ingredient and available tools/equipment.

Background:
You are a LLM Agent.
""",
)


chef_agent_responses = AssistantAgent(
    name="chef_agent_responses",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


chef_model_v2_agent = AssistantAgent(
    name="chef_model_v2_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


dynamic_agent = AssistantAgent(
    name="dynamic_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


agent_that_harasses_you = AssistantAgent(
    name="agent_that_harasses_you",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


error_agent = AssistantAgent(
    name="error_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


network_agent = AssistantAgent(
    name="network_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


weather_agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)


eval_agent = AssistantAgent(
    name="eval_agent",
    model_client=model_client,
    system_message="""
Role:
LLM Agent

Goal:
LLM Agent

Background:
You are a LLM Agent.
""",
)



