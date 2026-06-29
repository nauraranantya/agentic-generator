"""
Auto-generated CrewAI Crew: CopyCrew

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Marketing Campaign Objective: Overarching objective: produce Instagram post copy and photograph concepts that highlight the product, its unique selling points, and create a high-impact campaign.
Objectives:
  - Copy Crew Objective: Generate analysis-informed ad copy and campaign strategy to drive engagement.
  - Image Crew Objective: Create photograph concepts aligned with ad copy and campaign to produce visuals for Instagram.
Capabilities:
  - web scraping: Capability to scrape and summarize website content.
  - internet search: Capability to search the internet and summarize results.
  - instagram search: Capability to search Instagram posts (site:instagram.com queries).
  - strategy planning: Capability to synthesize analysis into marketing strategies.
  - copywriting: Capability to craft punchy Instagram ad copy.
  - photography review: Capability to evaluate and revise photograph concepts.
  - review & approval: Capability to review outputs, approve, and delegate follow-ups.
Resources:
  - Product Analysis Report: Textual report produced by product_analysis task: detailed product features, market appeal, recommendations.
  - Competitor Analysis Report: Textual competitor analysis with top-3 competitor comparisons produced by competitor_analysis task.
  - Campaign Strategy & Ideas: Marketing strategy and creative content ideas produced by campaign_development task. Used by creative and photography agents.
  - Ad Copy Options (3 variations): Three Instagram ad copy options produced by instagram_ad_copy task.
  - Photograph Descriptions (3 options): Three photograph concept descriptions produced by take_photograph_task.
  - Approved Photograph Descriptions: Reviewed and approved (or delegated) photograph descriptions produced by review_photo task.
  - tasks.py (semantic summary): Contains prompt texts (task descriptions) for product_analysis, competitor_analysis, campaign_development, instagram_ad_copy, take_photograph_task, review_photo. Task prompts preserved as Prompt individuals and Task dct:description values.
  - agents.py (semantic summary): Defines agents (roles, goals, backstories), their tool sets, and association to the Ollama language model. Represented as LLMAgent individuals with agent prompts and useLanguageModel links.
  - main.py (semantic summary): Orchestrates two Crews (Copy Crew and Image Crew). Copy Crew runs tasks: product_analysis, competitor_analysis, campaign_development, instagram_ad_copy. Image Crew runs tasks: take_photograph_task, review_photo. Crew orchestration and kickoff semantics not directly modeled; outputs represented as produced Resources.
"""

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: tool_browser_tools_scrape_and_summarize — unknown tool class "BrowserToolsscrapeandsummarizewebsite"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("BrowserToolsscrapeandsummarizewebsite")
def tool_browser_tools_scrape_and_summarize(*args, **kwargs) -> str:
    """Semantic purpose: Scrape a website and produce a long summary of its content or content chunks. Inpu"""
    return "tool_browser_tools_scrape_and_summarize result"

# TODO: tool_search_tools_search_internet — unknown tool class "SearchToolssearchinternet"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchToolssearchinternet")
def tool_search_tools_search_internet(*args, **kwargs) -> str:
    """Semantic purpose: Search the Internet (generic web search) and return top organic results, title, li"""
    return "tool_search_tools_search_internet result"

# TODO: tool_search_tools_search_instagram — unknown tool class "SearchToolssearchinstagram"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchToolssearchinstagram")
def tool_search_tools_search_instagram(*args, **kwargs) -> str:
    """Semantic purpose: Search Instagram via site-limited search (site:instagram.com) to find relevant pos"""
    return "tool_search_tools_search_instagram result"


# ===========================================================
# Custom LLM
# ===========================================================
product_competitor_agent_llm = LLM(model="ollama/local")
strategy_planner_agent_llm = LLM(model="ollama/local")
creative_content_creator_agent_llm = LLM(model="ollama/local")
senior_photographer_agent_llm = LLM(model="ollama/local")
chief_creative_director_agent_llm = LLM(model="ollama/local")


@CrewBase
class CopyCrew:
    """CopyCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def product_competitor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['product_competitor_agent'],
            llm=product_competitor_agent_llm,
        )

    @agent
    def strategy_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['strategy_planner_agent'],
            llm=strategy_planner_agent_llm,
        )

    @agent
    def creative_content_creator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_content_creator_agent'],
            llm=creative_content_creator_agent_llm,
        )

    @agent
    def senior_photographer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_photographer_agent'],
            llm=senior_photographer_agent_llm,
        )

    @agent
    def chief_creative_director_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_creative_director_agent'],
            llm=chief_creative_director_agent_llm,
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def task_product_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['task_product_analysis'],
            agent=self.product_competitor_agent(),
        )

    @task
    def task_competitor_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['task_competitor_analysis'],
            agent=self.product_competitor_agent(),
        )

    @task
    def task_campaign_development(self) -> Task:
        return Task(
            config=self.tasks_config['task_campaign_development'],
            agent=self.strategy_planner_agent(),
            context=[self.task_product_analysis(), self.task_competitor_analysis()],
        )

    @task
    def task_instagram_ad_copy(self) -> Task:
        return Task(
            config=self.tasks_config['task_instagram_ad_copy'],
            agent=self.creative_content_creator_agent(),
            context=[self.task_campaign_development()],
        )

    @task
    def task_take_photograph(self) -> Task:
        return Task(
            config=self.tasks_config['task_take_photograph'],
            agent=self.senior_photographer_agent(),
            context=[self.task_instagram_ad_copy(), self.task_product_analysis()],
        )

    @task
    def task_review_photo(self) -> Task:
        return Task(
            config=self.tasks_config['task_review_photo'],
            agent=self.chief_creative_director_agent(),
            context=[self.task_take_photograph(), self.task_product_analysis()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the CopyCrew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
