"""
Auto-generated CrewAI Crew: ExpandIdeaCrewteam

Source  : AgentO Knowledge Graph → SPARQL → Pydantic → Jinja2
Pipeline: 3-Layer Conversion Pipeline
Goals:
  - : Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.
  - : Provide WHY, HOW, WHAT messaging and core message for the idea.
  - : Select a Tailwind template that fits the idea and copy it into the working folder; then update components.
  - : Produce content for components, update components, and QA them according to rules.
Capabilities:
  - web search: Capability to search internet and return snippets.
  - web scraping and summarization: Capability to scrape a website and summarize content.
  - file write: Capability to write content safely to files in workdir.
  - learn templates listing: Capability to read templates configuration and list template options.
  - copy template folder: Capability to copy template folders into project workspace.
  - read file: Capability to read file content from the workspace.
  - list directory: Capability to list directories in the workspace.
Resources:
  - templates/ (folder of Tailwind templates): Local templates base folder. The code expects user to place individual template folders here. Referenced by TemplateTools.copy_landing_page_template_to_project_folder.
  - workdir.zip (final packaged project archive): At the end of execution the system compresses ./workdir into a zip and returns it to the user.
  - Expanded idea report (text): Output of expand_idea_task. The code uses this expanded idea as input to the next crews.
  - Refined idea report (text): Output of refine_idea_task. Used by other tasks to craft landing page content.
  - Copied template folder in workdir: Result of copying a template folder into ./workdir. The copy is executed by TemplateTools.copy_landing_page_template_to_project_folder.
  - List of component paths used in main page.jsx: Produced by update_page_task: the set of component file paths that will be used on the final single page.
  - Component text suggestions (structured text): Produced by component_content_task and used by update_component_task.
  - Updated React component files (on disk): Files written to ./workdir by update_component_task using WriteFileTool. Filenames correspond to the components list.
  - QA confirmation / corrections applied: Confirmation that updated components pass QA rules. If not, corrected files are written to disk.
  - Copied template folder (workdir/<template>): A template folder copied from ./templates into ./workdir. Expected structure includes src/components and src/app/page.jsx.
  - Components full path list (JSON array): The JSON array that choose_template_task must return listing the most important 4 components' full paths to update; later used by CreateContentCrew.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool


# ===========================================================
# Tool Instances
# ===========================================================
# TODO: search_internet_tool — unknown tool class "SearchtheinternetSearchToolssearchinternet"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("SearchtheinternetSearchToolssearchinternet")
def search_internet_tool(*args, **kwargs) -> str:
    """Performs internet search using an external search API (serper.dev). Requires SERPER_API_KEY environm"""
    return "search_internet_tool result"

# TODO: scrape_website_tool — unknown tool class "ScrapewebsitecontentBrowserToolsscrapeandsummarizewebsite"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("ScrapewebsitecontentBrowserToolsscrapeandsummarizewebsite")
def scrape_website_tool(*args, **kwargs) -> str:
    """Scrapes website HTML via browserless API and summarizes content using an internal summarization Task"""
    return "scrape_website_tool result"

# TODO: write_file_tool — unknown tool class "WritefiletoworkdirFileToolswritefile"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("WritefiletoworkdirFileToolswritefile")
def write_file_tool(*args, **kwargs) -> str:
    """Writes files into ./workdir with path sanitization and allowed extensions."""
    return "write_file_tool result"

# TODO: learn_templates_tool — unknown tool class "LearnlandingpageoptionsTemplateToolslearnlandingpageoptions"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("LearnlandingpageoptionsTemplateToolslearnlandingpageoptions")
def learn_templates_tool(*args, **kwargs) -> str:
    """Reads config/templates.json to list available templates."""
    return "learn_templates_tool result"

# TODO: copy_template_tool — unknown tool class "CopylandingpagetemplatetoprojectfolderTemplateToolscopylandingpagetemplatetoprojectfolder"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("CopylandingpagetemplatetoprojectfolderTemplateToolscopylandingpagetemplatetoprojectfolder")
def copy_template_tool(*args, **kwargs) -> str:
    """Copies a template folder from ./templates to ./workdir with safety checks."""
    return "copy_template_tool result"

# TODO: read_file_tool — unknown tool class "Readfilefilemanagementtoolkitreadfile"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("Readfilefilemanagementtoolkitreadfile")
def read_file_tool(*args, **kwargs) -> str:
    """Read file contents from workdir (used by agent toolkits)."""
    return "read_file_tool result"

# TODO: list_directory_tool — unknown tool class "Listdirectoryfilemanagementtoolkitlistdirectory"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("Listdirectoryfilemanagementtoolkitlistdirectory")
def list_directory_tool(*args, **kwargs) -> str:
    """List directories in workdir (used by agent toolkits)."""
    return "list_directory_tool result"

# TODO: file_management_toolkit — unknown tool class "Filemanagementtoolkitcontainerprovidesreadfilelistdirectorytools"
#   Implement as a custom BaseTool or replace with a crewai_tools equivalent.
@tool("Filemanagementtoolkitcontainerprovidesreadfilelistdirectorytools")
def file_management_toolkit(*args, **kwargs) -> str:
    """In the code this is an instantiation of FileManagementToolkit(root_dir='workdir', selected_tools=['r"""
    return "file_management_toolkit result"




@CrewBase
class ExpandIdeaCrewteam:
    """ExpandIdeaCrewteam crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # ── Agents ──────────────────────────────────────────

    @agent
    def senior_idea_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_idea_analyst'],
            tools=[search_internet_tool, scrape_website_tool],
        )

    @agent
    def senior_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_strategist'],
            tools=[search_internet_tool, scrape_website_tool],
        )

    @agent
    def senior_react_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_react_engineer'],
            tools=[search_internet_tool, scrape_website_tool, write_file_tool, learn_templates_tool, copy_template_tool, read_file_tool, list_directory_tool],
        )

    @agent
    def senior_content_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_content_editor'],
            tools=[write_file_tool, read_file_tool, list_directory_tool],
        )

    # ── Tasks ───────────────────────────────────────────

    @task
    def expand_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['expand_idea_task'],
            agent=self.senior_idea_analyst(),
        )

    @task
    def choose_template_task(self) -> Task:
        return Task(
            config=self.tasks_config['choose_template_task'],
            agent=self.senior_react_engineer(),
            context=[self.refine_idea_task()],
        )

    @task
    def component_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['component_content_task'],
            agent=self.senior_content_editor(),
            context=[self.refine_idea_task(), self.update_page_task()],
        )

    @task
    def refine_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['refine_idea_task'],
            agent=self.senior_strategist(),
            context=[self.expand_idea_task()],
        )

    @task
    def update_page_task(self) -> Task:
        return Task(
            config=self.tasks_config['update_page_task'],
            agent=self.senior_react_engineer(),
            context=[self.choose_template_task()],
        )

    @task
    def update_component_task(self) -> Task:
        return Task(
            config=self.tasks_config['update_component_task'],
            agent=self.senior_content_editor(),
            context=[self.component_content_task(), self.update_page_task()],
        )

    @task
    def qa_component_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_component_task'],
            agent=self.senior_content_editor(),
            context=[self.update_component_task()],
        )

    # ── Crew ────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """Creates the ExpandIdeaCrewteam"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
