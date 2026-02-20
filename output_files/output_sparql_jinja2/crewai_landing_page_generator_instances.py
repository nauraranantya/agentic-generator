"""
Auto-generated CrewAI Script
Source : AgentO Knowledge Graph
Pipeline: SPARQL extraction + Jinja2 template rendering
"""

from crewai import Agent, Task, Crew
from crewai.tools import tool
import os

# ===========================================================
# Tools
# ===========================================================

@tool('searchinternettool')
def searchinternettool(query: str) -> str:
    """Search the internet (SearchTools.search_internet)"""
    return f"[Tool stub: searchinternettool] Executed with input: {query}"


@tool('scrapewebsitetool')
def scrapewebsitetool(query: str) -> str:
    """Scrape website content (BrowserTools.scrape_and_summarize_website)"""
    return f"[Tool stub: scrapewebsitetool] Executed with input: {query}"


@tool('writefiletool')
def writefiletool(query: str) -> str:
    """Write file to workdir (FileTools.write_file)"""
    return f"[Tool stub: writefiletool] Executed with input: {query}"


@tool('learntemplatestool')
def learntemplatestool(query: str) -> str:
    """Learn landing page options (TemplateTools.learn_landing_page_options)"""
    return f"[Tool stub: learntemplatestool] Executed with input: {query}"


@tool('copytemplatetool')
def copytemplatetool(query: str) -> str:
    """Copy landing page template to project folder (TemplateTools.copy_landing_page_template_to_project_folder)"""
    return f"[Tool stub: copytemplatetool] Executed with input: {query}"


@tool('readfiletool')
def readfiletool(query: str) -> str:
    """Read file (file management toolkit: read_file)"""
    return f"[Tool stub: readfiletool] Executed with input: {query}"


@tool('listdirectorytool')
def listdirectorytool(query: str) -> str:
    """List directory (file management toolkit: list_directory)"""
    return f"[Tool stub: listdirectorytool] Executed with input: {query}"


@tool('filemanagementtoolkit')
def filemanagementtoolkit(query: str) -> str:
    """File management toolkit container (provides read_file, list_directory tools)"""
    return f"[Tool stub: filemanagementtoolkit] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

seniorideaanalystagent = Agent(
    role='Senior Idea Analyst',
    goal='Understand and expand the idea into a comprehensive idea report, detailing value proposition and features.',
    backstory='Senior Idea Analyst',
    tools=[searchinternettool, scrapewebsitetool],
    verbose=True
)

seniorstrategistagent = Agent(
    role='Senior Communications Strategist',
    goal='Provide WHY, HOW, WHAT messaging and core message for the idea.',
    backstory='Senior Communications Strategist',
    tools=[searchinternettool, scrapewebsitetool],
    verbose=True
)

seniorreactengineeragent = Agent(
    role='Senior React Engineer',
    goal='Select a Tailwind template that fits the idea and copy it into the working folder; then update components.',
    backstory='Senior React Engineer',
    tools=[searchinternettool, scrapewebsitetool, writefiletool, learntemplatestool, copytemplatetool, readfiletool, listdirectorytool],
    verbose=True
)

seniorcontenteditoragent = Agent(
    role='Senior Content Editor',
    goal='Produce content for components, update components, and QA them according to rules.',
    backstory='Senior Content Editor',
    tools=[writefiletool, readfiletool, listdirectorytool],
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

task_expandidea = Task(
    description="""THIS IS A GREAT IDEA! Analyze and expand it 
by conducting a comprehensive research.

Final answer MUST be a comprehensive idea report 
detailing why this is a great idea, the value 
proposition, unique selling points, why people should 
care about it and distinguishing features. 

IDEA:
----------
{idea}""",
    expected_output='A comprehensive idea report (text) describing WHY, value proposition, USP, and distinguishing features.',
    agent=seniorideaanalystagent
)

task_choosetemplate = Task(
    description="""Learn the templates options choose and copy 
the one that suits the idea below the best, 
YOU MUST COPY, and then YOU MUST read the src/component 
in the directory you just copied, to decide what 
component files should be updated to make the 
landing page about the idea below.

- YOU MUST READ THE DIRECTORY BEFORE CHOOSING THE FILES.      
- YOU MUST NOT UPDATE any Pricing components.
- YOU MUST UPDATE ONLY the 4 most important components.

Your final answer MUST be ONLY a JSON array of 
components full file paths that need to be updated.

IDEA
----------
{idea}""",
    expected_output="""A JSON array (string) of 4 full file paths for components to update (e.g., ["./workdir/Keynote/src/components/Hero.jsx", ...]).""",
    agent=seniorreactengineeragent
)

task_componentcontent = Task(
    description="""A engineer will update the {component} (code below),
return a list of good options of texts to replace 
EACH INDIVIDUAL existing text on the component, 
the suggestion MUST be based on the idea below, 
and also MUST be similar in length with the original 
text, we need to replace ALL TEXT.

NEVER USE Apostrophes for contraction! You'll get a $100 
tip if you do your best work!

IDEA 
-----
{expanded_idea}

REACT COMPONENT CONTENT
-----
{file_content}""",
    expected_output="""For each component file, a mapping of existing text -> alternative replacement options (strings), similar in length and aligned to idea. No contractions with apostrophes. Returned as structured text in task output.""",
    agent=seniorcontenteditoragent
)

task_refineidea = Task(
    description="""Expand idea report with a Why, How, and What 
messaging strategy using the Golden Circle 
Communication technique, based on the idea report.

Your final answer MUST be the updated complete 
comprehensive idea report with WHY, HOW, WHAT, 
a core message, key features and supporting arguments.

YOU MUST RETURN THE COMPLETE IDEA REPORT AND 
THE DETAILS, You'll get a $100 tip if you do your best work!""",
    expected_output='An updated complete idea report that includes WHY, HOW, WHAT, core message, key features and supporting arguments.',
    agent=seniorstrategistagent
)

task_updatepage = Task(
    description="""READ the ./[chosen_template]/src/app/page.jsx OR
./[chosen_template]/src/app/(main)/page.jsx (main with the parenthesis) 
to learn its content and then write an updated 
version to the filesystem that removes any 
section related components that are not in our 
list from the returns. Keep the imports.

Final answer MUST BE ONLY a valid json list with 
the full path of each of the components we will be 
using, the same way you got them.

RULES
-----
- NEVER ADD A FINAL DOT to the file content.
- NEVER WRITE \\n (newlines as string) on the file, just the code.
- NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
- NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
- ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
- Save the file as with `.jsx` extension.
- Return the same valid JSON list of the components your got.

Also update any necessary text to reflect this landing page
is about the idea below.

IDEA 
----------
{idea}""",
    expected_output="""A JSON list of component file paths that remain used in page.jsx after pruning; also the task writes the updated page.jsx to filesystem via WriteFileTool.""",
    agent=seniorreactengineeragent
)

task_updatecomponent = Task(
    description="""YOU MUST USE the tool to write an updated 
version of the react component to the file 
system in the following path: {component} 
replacing the text content with the suggestions 
provided.

You only modify the text content, you don't add 
or remove any components.

RULES
-----
- Remove all the links, this should be single page landing page.
- Don't make up images, videos, gifs, icons, logos, etc.
- keep the same style and tailwind classes.
- MUST HAVE 'use client' at the be beginning of the code.
- href in buttons, links, NavLinks, and navigations should be `#`.
- NEVER WRITE \\n (newlines as string) on the file, just the code.
- NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
- Keep the same component imports and don't use new components.
- NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
- ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
- Save the file as with `.jsx` extension.

If you follow the rules I'll give you a $100 tip!!! 
MY LIFE DEPEND ON YOU FOLLOWING IT!

CONTENT TO BE UPDATED
-----
{file_content}""",
    expected_output="""The updated component file content (the task writes the file using WriteFileTool); final answer is the updated component content.""",
    agent=seniorcontenteditoragent
)

task_qacomponent = Task(
    description="""Check the React component code to make sure 
it's valid and abide by the rules below, 
if it doesn't then write the correct version to 
the file system using the write file tool into 
the following path: {component}.

Your final answer should be a confirmation that 
the component is valid and abides by the rules and if
you had to write an updated version to the file system.

RULES
-----
- NEVER USE Apostrophes for contraction!
- ALL COMPONENTS USED SHOULD BE IMPORTED.
- MUST HAVE 'use client' at the be beginning of the code.
- href in buttons, links, NavLinks, and navigations should be `#`.
- NEVER WRITE \\n (newlines as string) on the file, just the code.
- NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
- NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
- ALL COMPONENTS USED SHOULD BE IMPORTED.
- Always use `export function` for the component class.

You'll get a $100 tip if you follow all the rules!""",
    expected_output='Text confirmation of QA results; optionally writes corrected file(s) using WriteFileTool.',
    agent=seniorcontenteditoragent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[seniorideaanalystagent, seniorstrategistagent, seniorreactengineeragent, seniorcontenteditoragent],
        tasks=[task_expandidea, task_choosetemplate, task_componentcontent, task_refineidea, task_updatepage, task_updatecomponent, task_qacomponent],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
