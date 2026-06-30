"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : 
Objectives:
  - : 
Human Agents:
  - admin ()
Resources:
  - : Historic prices and metadata for Nvidia (NVDA) covering the past month. Intended to be retrieved via Python code. Source and retrieval instructions preserved in CodeArtifact description.
  - : Artifact produced by Engineer: Python scripts to retrieve NVDA historic prices, compute monthly performance metrics, and produce serialized outputs (csv, json, plots). Implementation details intentionally captured as a high-level description (no SDK-specific code insertion in ontology).
  - : Results produced by Executor after running CodeArtifact: computed performance metrics, figures, and any data files used by Writer to compose the blog.
  - : Draft blog post in markdown format produced by Writer based on execution results. Contains title, textual analysis of stock performance, and optionally code-derived figures. Writer instructed to use pseudo ```md``` code block for content.
  - : Blog draft refined by Writer after Admin (user_proxy) provides comments. Final deliverable of workflow.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: coding_environment_tool — unknown tool class "CodingEnvironmentTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("CodingEnvironmentTool")
def coding_environment_tool(*args, **kwargs) -> str:
    """Conceptual tool representing the environment used by Executor to run code. Config captured as key/va"""
    return "coding_environment_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planner_agent'],
        )

    @agent
    def engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['engineer_agent'],
        )

    @agent
    def executor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['executor_agent'],
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            tools=[coding_environment_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def main_task(self) -> Task:
        return Task(
            config=self.tasks_config['main_task'],
        )

    @task
    def plan_information_task(self) -> Task:
        return Task(
            config=self.tasks_config['plan_information_task'],
            agent=self.planner_agent(),
        )

    @task
    def write_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_code_task'],
            agent=self.engineer_agent(),
        )

    @task
    def execute_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['execute_code_task'],
            agent=self.executor_agent(),
            context=[self.write_code_task()],
        )

    @task
    def write_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_report_task'],
            agent=self.writer_agent(),
            context=[self.execute_code_task()],
        )

    @task
    def admin_feedback_task(self) -> Task:
        return Task(
            config=self.tasks_config['admin_feedback_task'],
            context=[self.write_report_task()],
            human_input=True,
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
