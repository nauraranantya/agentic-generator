"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Objectives:
  - : Ensure tasks have an estimated duration to help with planning and prioritization.
  - : Guarantee that the user's todo list state is saved every interaction, per agent instruction.
Capabilities:
  - manage todo list: Ability to create, update, list, and complete todo items.
  - timebox tasks: Ability to ask the user for estimated durations and enforce timeboxing of tasks.
  - save memory every response: Requirement to persist working memory in every interaction to prevent forgetting between turns.
  - format and render list with emojis and subtasks: Ability to render todo lists with emojis, date fields, indexed titles, descriptions, statuses, and nested subtasks using boxed bullet lists.
Resources:
  - : External identifier passed to the agent as resourceId (represents the user-specific resource used for memory/session association in the source). Note: value originates in the code as the constant 'SOME_USER_ID'.
  - : Representative threadId used in the runtime example. Modeled as a resource instance to preserve the runtime identifier.
  - : The working memory representation that the agent is expected to produce and save in every response inside <working_memory> blocks. Initially seeded with the template below (exact string taken from source memory configuration):

# Todo List
## Active Items
- Example (Due: Feb 7 3028, Started: Feb 7 2025)
  - Description: This is an example task - replace with whatever the user needs

## Completed Items
- None yet
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task




@CrewBase
class UnnamedProject:
    """UnnamedProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def todo_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['todo_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def init_first_chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['init_first_chat_task'],
            agent=self.todo_agent(),
        )

    @task
    def init_return_chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['init_return_chat_task'],
            agent=self.todo_agent(),
        )

    @task
    def present_list_task(self) -> Task:
        return Task(
            config=self.tasks_config['present_list_task'],
            agent=self.todo_agent(),
        )

    @task
    def update_list_task(self) -> Task:
        return Task(
            config=self.tasks_config['update_list_task'],
            agent=self.todo_agent(),
        )

    @task
    def timebox_task(self) -> Task:
        return Task(
            config=self.tasks_config['timebox_task'],
            agent=self.todo_agent(),
        )

    @task
    def save_working_memory_task(self) -> Task:
        return Task(
            config=self.tasks_config['save_working_memory_task'],
            agent=self.todo_agent(),
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
