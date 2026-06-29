"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Top-level goal: identify and rank job opportunities for a given CV.
Objectives:
  - : Objective for producing a structured summary of the given CV.
  - : Objective for producing a ranked list of job matches for the candidate.
Resources:
  - : CV markdown file provided as input
  - : CSV file listing job opportunities
  - : Structured summary of the CV produced by read_cv_task; includes Professional Summary, Technical Skills, Work History, Education, Key Achievements.
  - : A ranked list of job opportunities that best match the CV, produced by match_cv_task; includes Job Title, Match Score, Key Matching Points.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool

from crewai_tools import FileReadTool, CSVSearchTool

# ===========================================================
# Tool Instances
# ===========================================================
file_read_tool = FileReadTool(description="Reads and returns file contents given a path. Used to access CV and any file-based resources.")
csv_search_tool = CSVSearchTool(description="Searches CSV files and extracts rows matching criteria. Used to parse the jobs CSV.")
# TODO: my_custom_tool — unknown tool class "MyCustomTool"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("MyCustomTool")
def my_custom_tool(*args, **kwargs) -> str:
    """Custom tool implemented at src/match_to_proposal/tools/job_db_connect.py. Placeholder for an externa"""
    return "my_custom_tool result"




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def cv_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_reader'],
            tools=[file_read_tool],
            allow_delegation=False,
            verbose=False,
        )

    @agent
    def matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['matcher'],
            tools=[file_read_tool, csv_search_tool],
            allow_delegation=False,
            verbose=False,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def read_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_cv_task'],
            agent=self.cv_reader(),
        )

    @task
    def match_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_cv_task'],
            agent=self.matcher(),
            context=[self.read_cv_task()],
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
