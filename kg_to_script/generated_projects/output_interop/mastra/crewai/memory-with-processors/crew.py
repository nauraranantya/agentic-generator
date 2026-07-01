"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Goal to illustrate that TokenLimiter ensures conversation memory stays within token limits while preserving recent context.
  - : Goal to show custom memory processors can filter or redact content based on keywords or types (e.g., tool calls).
  - : Goal to validate that the support agent can use tools, recall recent context, and that TokenLimiter prunes older content when exceeding token limits.
Resources:
  - : Represents the large textual content that the read-file tool returns (truncated to 20K chars or generated mock content).
  - : Represents textual results returned by web-search tool (simulated search output).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: read_file_tool — unknown tool class "readfiletool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("readfiletool")
def read_file_tool(*args, **kwargs) -> str:
    """Read a large file to test token limits; attempts several file system locations and otherwise generat"""
    return "read_file_tool result"

# TODO: search_tool — unknown tool class "searchtool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("searchtool")
def search_tool(*args, **kwargs) -> str:
    """Search the web for information. Input schema expects a 'query' string."""
    return "search_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def token_test_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['token_test_agent'],
            tools=[read_file_tool],
        )

    @agent
    def technical_support(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_support'],
            tools=[search_tool],
        )

    @agent
    def technical_support_repo(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_support_repo'],
            tools=[search_tool],
        )

    @agent
    def forgetful_job_interviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['forgetful_job_interviewer'],
        )

    @agent
    def forgetful_job_interviewer_repo(self) -> Agent:
        return Agent(
            config=self.agents_config['forgetful_job_interviewer_repo'],
            tools=[search_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_token_limiter_demo(self) -> Task:
        return Task(
            config=self.tasks_config['task_token_limiter_demo'],
        )

    @task
    def task_forgetful_interviewer_demo(self) -> Task:
        return Task(
            config=self.tasks_config['task_forgetful_interviewer_demo'],
        )

    @task
    def task_technical_support_demo(self) -> Task:
        return Task(
            config=self.tasks_config['task_technical_support_demo'],
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
