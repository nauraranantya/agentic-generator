"""
Auto-generated AutoGen Team: MarkDownValidatorCrew
Goals:
  - Markdown validation crew goal: Provide a detailed list of the markdown linting results. Give a summary with actionable tasks to address the validation results. Write your response as if you were handing it to a developer to fix the issues. DO NOT provide examples of how to fix the issues or recommend other tools to use.
  - Requirements Manager goal: Provide a detailed list of the markdown linting results. Give a summary with actionable tasks to address the validation results. Write your response as if you were handing it to a developer to fix the issues. DO NOT provide examples of how to fix the issues or recommend other tools to use.
Resources:
  - Markdown validation report (tool output): Formatted string of validation results returned by markdown_validation_tool. Example output forms: 'No markdown validation issues found.' or a newline-separated list of detected rule violations with file, line, rule id, rule name and description.
  - PyMarkdownApi: The PyMarkdownApi library instance invoked by the tool implementation. The tool calls PyMarkdownApi().scan_path(file_path) to perform the scan and returns a formatted summary.
  - Input markdown file (CLI filename): The file path provided via command-line to the CLI (sys.argv[1] when running). The task expects only the file path string (filename) to be passed to the markdown_validation_tool.
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


def markdown_validation_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    markdownvalidationtool

    Description:
    Tool definition (from src/markdown_validator/tools/markdownTools.py):
- Tool name registered as 'markdown_validation_tool'
- Signature (conceptual): input: file_path (string) -> output: validation_results (string)
- Behavior:
    * Checks whether file_path exists on filesystem; returns error string if not found.
    * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.
    * Uses format_scan_result to transform the scan result to a formatted string.
    * On PyMarkdownApiException returns 'API Exception: <exception message>'.
- Output format:
    * If no failures: 'No markdown validation issues found.'
    * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description
- Constraints and usage note:
    * The tool expects only the path (filename) as input.
    * The task instructs the agent to pass only the filename to this tool.
    """
    return (
        "Tool 'markdown_validation_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


markdown_validation_tool = FunctionTool(
    markdown_validation_tool_impl,
    description="""Tool definition (from src/markdown_validator/tools/markdownTools.py):
- Tool name registered as 'markdown_validation_tool'
- Signature (conceptual): input: file_path (string) -> output: validation_results (string)
- Behavior:
    * Checks whether file_path exists on filesystem; returns error string if not found.
    * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.
    * Uses format_scan_result to transform the scan result to a formatted string.
    * On PyMarkdownApiException returns 'API Exception: <exception message>'.
- Output format:
    * If no failures: 'No markdown validation issues found.'
    * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description
- Constraints and usage note:
    * The tool expects only the path (filename) as input.
    * The task instructs the agent to pass only the filename to this tool."""
)


# ==================================================
# Agents
# ==================================================


requirements_manager = AssistantAgent(
    name="requirements_manager",
    model_client=model_client,
    system_message="""
Role:
Requirements Manager

Goal:
Provide a detailed list of the markdown linting results. Give a summary with actionable tasks to address the validation results. Write your response as if you were handing it to a developer to fix the issues. DO NOT provide examples of how to fix the issues or recommend other tools to use.

Background:
Agent backstory: expert business analyst and software QA specialist.
""",
)



