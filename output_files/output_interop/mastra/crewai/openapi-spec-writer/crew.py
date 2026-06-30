"""
Auto-generated CrewAI Crew: MastraSystem

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - Generate OpenAPI spec from docs: Produce a merged OpenAPI specification from website documentation and optionally open a PR with the spec in a repository.
Capabilities:
  - Convert markdown to OpenAPI spec: Extract endpoints, parameters, responses and models from markdown documentation and produce an OpenAPI fragment.
  - Merge OpenAPI fragments: Merge multiple OpenAPI fragments into a single valid OpenAPI spec (resolve conflicts, unify components).
  - Format spec as YAML: Produce a properly formatted YAML spec from textual content.
Resources:
  - Crawled data (markdown pages): Resource produced by site-crawl tool: an array of objects containing markdown text and metadata with sourceURL. Used as input for generate-spec tool.
  - Merged OpenAPI spec (yaml string): The merged OpenAPI specification produced by the generate-spec tool (string YAML). This resource is consumed by the add-to-github tool.
  - Pull Request URL / result: The PR created on GitHub as a result of add-to-github tool (pr_url if created).
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: site_crawl_tool — unknown tool class "SiteCrawl"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SiteCrawl")
def site_crawl_tool(*args, **kwargs) -> str:
    """Crawl a website and extract the markdown content"""
    return "site_crawl_tool result"

# TODO: firecrawl_integration — unknown tool class "FirecrawlIntegration"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("FirecrawlIntegration")
def firecrawl_integration(*args, **kwargs) -> str:
    """Integration client used to crawl websites (Firecrawl API key supplied at runtime)."""
    return "firecrawl_integration result"

# TODO: generate_spec_tool — unknown tool class "GenerateSpec"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("GenerateSpec")
def generate_spec_tool(*args, **kwargs) -> str:
    """Generate an OpenAPI spec from crawled website markdown; uses the OpenAPI agent to convert pages and """
    return "generate_spec_tool result"

# TODO: add_to_git_hub_tool — unknown tool class "AddtoGit"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("AddtoGit")
def add_to_git_hub_tool(*args, **kwargs) -> str:
    """Commit the spec to GitHub: formats YAML via the agent, creates branch, commits files and opens a pul"""
    return "add_to_git_hub_tool result"

# TODO: git_hub_integration — unknown tool class "GitHubIntegration"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("GitHubIntegration")
def git_hub_integration(*args, **kwargs) -> str:
    """GitHub integration client that performs git ref, file write and pull request operations (requires PE"""
    return "git_hub_integration result"




@CrewBase
class MastraSystem:
    """MastraSystem crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def openapi_spec_gen_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['openapi_spec_gen_agent'],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def site_crawl_sync_step_task(self) -> Task:
        return Task(
            config=self.tasks_config['site_crawl_sync_step_task'],
        )

    @task
    def generate_spec_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_spec_task'],
            context=[self.site_crawl_sync_step_task()],
        )

    @task
    def add_to_github_task(self) -> Task:
        return Task(
            config=self.tasks_config['add_to_github_task'],
            context=[self.generate_spec_task()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the MastraSystem"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
