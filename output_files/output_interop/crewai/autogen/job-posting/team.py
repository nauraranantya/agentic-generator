"""
Auto-generated AutoGen Team: JobPostingCrewTeam
Goals:
  - Hiring Goal: Goal: hire for the specified hiring needs (e.g., Production Assistant for TV production in Los Angeles, June 2025) using a compelling job posting aligned with company values.
Objectives:
  - Create Job Posting Objective: Collective objective: produce a job posting that aligns with company culture and hiring needs.
Resources:
  - DefaultInputs for JobPostingCrew: Example input values used for kickoff/train:
- company_domain: careers.wbd.com
- company_description: Warner Bros. Discovery is a premier global media and entertainment company, offering audiences the world’s most differentiated and complete portfolio of content, brands and franchises across television, film, sports, news, streaming and gaming. We're home to the world’s best storytellers, creating world-class products for consumers
- hiring_needs: Production Assistant, for a TV production set in Los Angeles in June 2025
- specific_benefits: Weekly Pay, Employee Meals, healthcare
These are preserved as the default input bundle used to initiate the crew."
  - job_description_example.md: # Amazing Job Description Example

## Company Overview
At InnovateTech, we're at the forefront of digital transformation, leveraging cutting-edge technologies to create impactful solutions. Our culture thrives on innovation, collaboration, and a commitment to excellence. Join us to be a part of a dynamic team shaping the future of tech.

## Job Title: Senior Software Engineer

### Location
Remote - Global Team

### Job Summary
As a Senior Software Engineer at InnovateTech, you'll lead the development of scalable software solutions that revolutionize how businesses interact with technology. You'll collaborate with cross-functional teams to drive projects from conception to deployment, ensuring high-quality and innovative outcomes.

### Responsibilities
- Design, develop, and implement high-quality software solutions that align with our strategic direction.
- Lead technical discussions and decision-making processes to drive technology forward.
- Mentor junior engineers, providing guidance and support to foster a culture of excellence and growth.
- Collaborate with stakeholders across the company to understand requirements and deliver beyond expectations.
- Stay abreast of industry trends and emerging technologies to incorporate best practices into our workflows.

### Requirements
- Bachelor's degree in Computer Science, Engineering, or related field.
- 5+ years of experience in software development, with a strong background in [Specific Technology/Programming Language].
- Proven track record of leading successful projects from inception to completion.
- Excellent problem-solving skills and a passion for technology.
- Strong communication and teamwork abilities.

### Benefits
- Competitive salary and equity package.
- Comprehensive health, dental, and vision insurance.
- Unlimited PTO to promote work-life balance.
- Remote work flexibility.
- Professional development stipends.
- Monthly wellness allowances.
- Inclusive and dynamic work culture.

### How to Apply
Please submit your resume, cover letter, and any relevant portfolio links to careers@innovatetech.com with the subject "Senior Software Engineer Application". We're excited to hear from you!

# ---

InnovateTech is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees.
  - draft_job_posting.md: Draft job posting produced by DraftJobPostingTask; initial markdown draft.
  - final_job_posting.md: Review-edited, final job posting in markdown, ready for publishing.
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


def website_search_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    WebsiteSearchTool

    Description:
    Tool used for general website search queries (instantiated in the solution as a web search tool).
    """
    return (
        "Tool 'website_search_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


website_search_tool = FunctionTool(
    website_search_tool_impl,
    description="""Tool used for general website search queries (instantiated in the solution as a web search tool)."""
)


def serper_dev_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    SerperDevTool

    Description:
    Tool used for developer-oriented web search or SERP querying (instantiated as SerperDevTool in the code).
    """
    return (
        "Tool 'serper_dev_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


serper_dev_tool = FunctionTool(
    serper_dev_tool_impl,
    description="""Tool used for developer-oriented web search or SERP querying (instantiated as SerperDevTool in the code)."""
)


def file_read_tool_impl(
    query: str = ""
) -> str:
    """
    AgentO Tool:
    FileReadTool

    Description:
    Tool to read local files; configured to read job_description_example.md
    """
    return (
        "Tool 'file_read_tool' "
        "is a generated stub and "
        "has not been implemented yet."
    )


file_read_tool = FunctionTool(
    file_read_tool_impl,
    description="""Tool to read local files; configured to read job_description_example.md"""
)


# ==================================================
# Agents
# ==================================================


research_agent = AssistantAgent(
    name="research_agent",
    model_client=model_client,
    system_message="""
Role:
Research Analyst

Goal:
Research Analyst

Background:
Role: Research Analyst
""",
)


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=model_client,
    system_message="""
Role:
Job Description Writer

Goal:
Job Description Writer

Background:
Role: Job Description Writer
""",
)


review_agent = AssistantAgent(
    name="review_agent",
    model_client=model_client,
    system_message="""
Role:
Review and Editing Specialist

Goal:
Review and Editing Specialist

Background:
Role: Review and Editing Specialist
""",
)



