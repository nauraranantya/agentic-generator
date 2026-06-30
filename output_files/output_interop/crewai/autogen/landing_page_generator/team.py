"""
Auto-generated AutoGen Team: ExpandIdeaCrewteam
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

from autogen_agentchat.agents import AssistantAgent

from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_agentchat.conditions import (

    MaxMessageTermination

)

from autogen_core.tools import FunctionTool

from autogen_ext.models.openai import (
    OpenAIChatCompletionClient
)

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini"
)


# ==================================================
# Generated Tool Stubs
# ==================================================


def search_internet_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SearchtheinternetSearchToolssearchinternet

    Description:
    Performs internet search using an external search API (serper.dev). Requires SERPER_API_KEY environment variable.
    """
    return (
        "Tool 'search_internet_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


search_internet_tool = FunctionTool(
    search_internet_tool_impl,
    description="""Performs internet search using an external search API (serper.dev). Requires SERPER_API_KEY environment variable."""
)


def scrape_website_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    ScrapewebsitecontentBrowserToolsscrapeandsummarizewebsite

    Description:
    Scrapes website HTML via browserless API and summarizes content using an internal summarization Task. Requires BROWSERLESS_API_KEY environment variable.
    """
    return (
        "Tool 'scrape_website_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


scrape_website_tool = FunctionTool(
    scrape_website_tool_impl,
    description="""Scrapes website HTML via browserless API and summarizes content using an internal summarization Task. Requires BROWSERLESS_API_KEY environment variable."""
)


def write_file_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    WritefiletoworkdirFileToolswritefile

    Description:
    Writes files into ./workdir with path sanitization and allowed extensions.
    """
    return (
        "Tool 'write_file_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


write_file_tool = FunctionTool(
    write_file_tool_impl,
    description="""Writes files into ./workdir with path sanitization and allowed extensions."""
)


def learn_templates_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    LearnlandingpageoptionsTemplateToolslearnlandingpageoptions

    Description:
    Reads config/templates.json to list available templates.
    """
    return (
        "Tool 'learn_templates_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


learn_templates_tool = FunctionTool(
    learn_templates_tool_impl,
    description="""Reads config/templates.json to list available templates."""
)


def copy_template_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    CopylandingpagetemplatetoprojectfolderTemplateToolscopylandingpagetemplatetoprojectfolder

    Description:
    Copies a template folder from ./templates to ./workdir with safety checks.
    """
    return (
        "Tool 'copy_template_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


copy_template_tool = FunctionTool(
    copy_template_tool_impl,
    description="""Copies a template folder from ./templates to ./workdir with safety checks."""
)


def read_file_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Readfilefilemanagementtoolkitreadfile

    Description:
    Read file contents from workdir (used by agent toolkits).
    """
    return (
        "Tool 'read_file_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


read_file_tool = FunctionTool(
    read_file_tool_impl,
    description="""Read file contents from workdir (used by agent toolkits)."""
)


def list_directory_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Listdirectoryfilemanagementtoolkitlistdirectory

    Description:
    List directories in workdir (used by agent toolkits).
    """
    return (
        "Tool 'list_directory_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


list_directory_tool = FunctionTool(
    list_directory_tool_impl,
    description="""List directories in workdir (used by agent toolkits)."""
)


def file_management_toolkit_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    Filemanagementtoolkitcontainerprovidesreadfilelistdirectorytools

    Description:
    In the code this is an instantiation of FileManagementToolkit(root_dir='workdir', selected_tools=['read_file','list_directory']). Modeled here as a Tool-like resource containing ReadFileTool and ListDirectoryTool.
    """
    return (
        "Tool 'file_management_toolkit' "
        "is a generated stub and "
        "has not been implemented yet."
    )


file_management_toolkit = FunctionTool(
    file_management_toolkit_impl,
    description="""In the code this is an instantiation of FileManagementToolkit(root_dir='workdir', selected_tools=['read_file','list_directory']). Modeled here as a Tool-like resource containing ReadFileTool and ListDirectoryTool."""
)


# ==================================================
# Agents
# ==================================================


senior_idea_analyst = AssistantAgent(
    name="senior_idea_analyst",
    model_client=model_client,
    system_message="""
Role:
Senior Idea Analyst

Goal:
Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.

Background:
You are a Senior Idea Analyst.
""",
)


senior_strategist = AssistantAgent(
    name="senior_strategist",
    model_client=model_client,
    system_message="""
Role:
Senior Communications Strategist

Goal:
Provide WHY, HOW, WHAT messaging and core message for the idea.

Background:
You are a Senior Communications Strategist.
""",
)


senior_react_engineer = AssistantAgent(
    name="senior_react_engineer",
    model_client=model_client,
    system_message="""
Role:
Senior React Engineer

Goal:
Select a Tailwind template that fits the idea and copy it into the working folder; then update components.

Background:
You are a Senior React Engineer.
""",
)


senior_content_editor = AssistantAgent(
    name="senior_content_editor",
    model_client=model_client,
    system_message="""
Role:
Senior Content Editor

Goal:
Produce content for components, update components, and QA them according to rules.

Background:
You are a Senior Content Editor.
""",
)



