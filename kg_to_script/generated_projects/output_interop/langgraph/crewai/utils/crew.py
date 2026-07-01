"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Capabilities:
  - : Capability to capitalize the first letter of each word in a sentence-like string.
  - : Capability to capitalize the first character of a string.
  - : Capability to serialize an array of message objects into a single formatted string preserving role and index, and stringifying non-string content with JSON semantics.
Resources:
  - : A plain string provided as input to capitalization tasks. Examples: 'hello world', 'apple'.
  - : Resulting string from capitalization tasks. Example outputs: 'Hello World', 'Apple'.
  - : An ordered collection of message-like objects (BaseMessage[]). Each element is expected to expose a getType() result describing its role (e.g., 'user', 'assistant') and a content field which may be a string or a serializable object.
  - : A single string produced by serializing a MessageArrayResource per the FormatMessagesTask. Example structure (conceptual): '<user index="0'>\nHello\n</user>\n<assistant index="1">\n{"reply":"ok"}\n</assistant>'.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: capitalize_tool — unknown tool class "CapitalizeTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("CapitalizeTool")
def capitalize_tool(*args, **kwargs) -> str:
    """Tool grouping for two capitalization utilities. Implements two conceptual capabilities: (1) capitali"""
    return "capitalize_tool result"

# TODO: format_messages_tool — unknown tool class "FormatMessagesTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("FormatMessagesTool")
def format_messages_tool(*args, **kwargs) -> str:
    """Tool that serializes an ordered collection of messages into a formatted string. Conceptual behavior:"""
    return "format_messages_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    # ── Tasks ───────────────────────────────────────────

    @task
    def capitalize_sentence_task(self) -> Task:
        return Task(
            config=self.tasks_config['capitalize_sentence_task'],
        )

    @task
    def capitalize_task(self) -> Task:
        return Task(
            config=self.tasks_config['capitalize_task'],
        )

    @task
    def format_messages_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_messages_task'],
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
