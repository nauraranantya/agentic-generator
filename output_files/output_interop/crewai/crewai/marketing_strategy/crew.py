"""
Auto-generated CrewAI Crew: MarketingPostsCrewTeam

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Marketing project goal: Boost awareness and adoption of CrewAI's services among enterprise clients. Create a comprehensive marketing campaign focusing on ease of use, scalability, and integration capabilities.
  - Lead Market Analyst personal goal: Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
  - Chief Marketing Strategist personal goal: Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
  - Creative Content Creator personal goal: Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact ad copies.
Objectives:
  - Produce campaign ideas: Objective: generate creative campaign ideas for the marketing project.
Capabilities:
  - web search capability: Capability to perform web searches and retrieve online information (used by SerperDevTool).
  - web scraping capability: Capability to scrape website content and extract structured information.
  - analyze market: Capability to research and analyze markets, competitors, and customers.
  - formulate strategy: Capability to synthesize analysis into strategic plans and marketing strategies.
  - create content: Capability to produce creative campaign ideas and marketing copy.
Resources:
  - Research Report (resource): Output of research_task: A complete report on the customer and their customers and competitors, including demographics, preferences, market positioning and audience engagement.
  - Project Summary (resource): Output of project_understanding_task: A detailed summary of the project and a profile of the target audience.
  - MarketStrategy (resource): Represents the MarketStrategy output (pydantic model):
Fields:
- name: str
- tatics: List[str]
- channels: List[str]
- KPIs: List[str]
From campaign: expected output: a detailed marketing strategy including name, tactics, channels, and KPIs.
  - CampaignIdea (resource): Represents campaign idea outputs (pydantic model):
Fields:
- name: str
- description: str
- audience: str
- channel: str
Expected: 5 campaign ideas with brief descriptions and expected impact.
  - Copy (resource): Represents copy outputs (pydantic model):
Fields:
- title: str
- body: str
Marketing copies for each campaign idea.
  - marketing_posts source: Original source code and configuration files (crew.py, main.py, config/agents.yaml, config/tasks.yaml) used to define the crew, agents, tasks, tools, and inputs. This ontology encodes semantic representation of that solution.
  - participation example: Example: lead_market_analyst_agent participated in research_task.
  - participation example: Example: chief_marketing_strategist_agent participated in marketing_strategy_task and project_understanding_task.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

# ===========================================================
# Tool Instances
# ===========================================================
serper_dev_tool = SerperDevTool(instantiated_in="crew.py: SerperDevTool()")
scrape_website_tool = ScrapeWebsiteTool(instantiated_in="crew.py: ScrapeWebsiteTool()")



@CrewBase
class MarketingPostsCrewTeam:
    """MarketingPostsCrewTeam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_market_analyst'],
            tools=[serper_dev_tool, scrape_website_tool],
            verbose=False,
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_marketing_strategist'],
            tools=[serper_dev_tool, scrape_website_tool],
            verbose=False,
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator'],
            verbose=False,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.lead_market_analyst(),
        )

    @task
    def project_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_understanding_task'],
            agent=self.chief_marketing_strategist(),
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_strategy_task'],
            agent=self.chief_marketing_strategist(),
            context=[self.research_task(), self.project_understanding_task()],
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['campaign_idea_task'],
            agent=self.creative_content_creator(),
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['copy_creation_task'],
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task(), self.campaign_idea_task()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MarketingPostsCrewTeam"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
