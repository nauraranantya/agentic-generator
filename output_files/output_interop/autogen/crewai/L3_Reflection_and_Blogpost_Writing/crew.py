"""
Auto-generated CrewAI Crew: UnnamedProject

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Goal: create a concise (within 100 words) blogpost about DeepLearning.AI and refine it via a reflection process with multiple reviewers.
Objectives:
  - : Objective: produce initial blogpost draft to be reviewed and refined.
Resources:
  - Blogpost Draft (resource): Expected output: concise engaging blogpost (with title) about DeepLearning.AI, within 100 words.
  - SEO Review (resource): JSON object with reviewer role and review text (as requested by summary prompt).
  - Legal Review (resource): JSON object with reviewer role and review text.
  - Ethics Review (resource): JSON object with reviewer role and review text.
  - Meta Reviewer Suggestion (resource): Aggregate review and final suggestion to improve the blogpost.
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
    def writer_1(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_1'],
        )

    @agent
    def critic_1(self) -> Agent:
        return Agent(
            config=self.agents_config['critic_1'],
        )

    @agent
    def seo_reviewer_1(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_reviewer_1'],
        )

    @agent
    def legal_reviewer_1(self) -> Agent:
        return Agent(
            config=self.agents_config['legal_reviewer_1'],
        )

    @agent
    def ethics_reviewer_1(self) -> Agent:
        return Agent(
            config=self.agents_config['ethics_reviewer_1'],
        )

    @agent
    def meta_reviewer_1(self) -> Agent:
        return Agent(
            config=self.agents_config['meta_reviewer_1'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def seo_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_review_task'],
            agent=self.seo_reviewer_1(),
        )

    @task
    def legal_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['legal_review_task'],
            agent=self.legal_reviewer_1(),
        )

    @task
    def ethics_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['ethics_review_task'],
            agent=self.ethics_reviewer_1(),
        )

    @task
    def meta_aggregation_task(self) -> Task:
        return Task(
            config=self.tasks_config['meta_aggregation_task'],
            agent=self.meta_reviewer_1(),
        )

    @task
    def blogpost_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['blogpost_generation_task'],
            agent=self.writer_1(),
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
