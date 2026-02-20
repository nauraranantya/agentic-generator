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

@tool('markdown_validation_tool')
def markdown_validation_tool(query: str) -> str:
    """markdown_validation_tool"""
    return f"[Tool stub: markdown_validation_tool] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

requirementsmanageragent = Agent(
    role='Requirements Manager',
    goal="""Provide a detailed list of the markdown linting results. Give a summary with actionable tasks to address the validation results. Write your response as if you were handing it to a developer to fix the issues. DO NOT provide examples of how to fix the issues or recommend other tools to use.""",
    backstory='Agent: Requirements_Manager',
    tools=[markdown_validation_tool],
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

syntax_review_task = Task(
    description="""Use the markdown_validation_tool to review the file(s) at this path: {filename}.
Be sure to pass only the file path to the markdown_validation_tool.
Use the following format to call the markdown_validation_tool:
Do I need to use a tool? Yes
Action: markdown_validation_tool
Action Input: {filename}

Get the validation results from the tool and then summarize it into a list of changes
the developer should make to the document.
DO NOT recommend ways to update the document.
DO NOT change any of the content of the document or add content to it. 
It is critical to your task to only respond with a list of changes.

If you already know the answer or if you do not need to use a tool, 
return it as your Final Answer.""",
    expected_output='A list of changes the developer should make to the document based on the markdown validation results.',
    agent=requirementsmanageragent
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[requirementsmanageragent],
        tasks=[syntax_review_task],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
