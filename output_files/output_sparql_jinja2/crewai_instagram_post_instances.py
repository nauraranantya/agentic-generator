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

@tool('tool_browsertools_scrapeandsummarize')
def tool_browsertools_scrapeandsummarize(query: str) -> str:
    """BrowserTools.scrape_and_summarize_website"""
    return f"[Tool stub: tool_browsertools_scrapeandsummarize] Executed with input: {query}"


@tool('tool_searchtools_searchinternet')
def tool_searchtools_searchinternet(query: str) -> str:
    """SearchTools.search_internet"""
    return f"[Tool stub: tool_searchtools_searchinternet] Executed with input: {query}"


@tool('tool_searchtools_searchinstagram')
def tool_searchtools_searchinstagram(query: str) -> str:
    """SearchTools.search_instagram"""
    return f"[Tool stub: tool_searchtools_searchinstagram] Executed with input: {query}"

# ===========================================================
# Agents
# ===========================================================

agent_productcompetitor = Agent(
    role='Lead Market Analyst',
    goal='Lead Market Analyst',
    backstory="""Role: Lead Market Analyst
Goal: Conduct amazing analysis of the products and competitors, providing in-depth insights to guide marketing strategies.
Backstory: As the Lead Market Analyst at a premier digital marketing firm, you specialize in dissecting online business landscapes.
Tools: BrowserTools.scrape_and_summarize_website, SearchTools.search_internet
AllowDelegation: False
Verbose: True
Notes: Uses an Ollama model indicated by environment variable MODEL (see Config entries).""",
    verbose=True
)

agent_strategyplanner = Agent(
    role='Chief Marketing Strategist',
    goal='Chief Marketing Strategist',
    backstory="""Role: Chief Marketing Strategist
Goal: Synthesize amazing insights from product analysis to formulate incredible marketing strategies.
Backstory: You are the Chief Marketing Strategist at a leading digital marketing agency, known for crafting bespoke strategies that drive success.
Tools: BrowserTools.scrape_and_summarize_website, SearchTools.search_internet, SearchTools.search_instagram
Verbose: True
Notes: Uses an Ollama model indicated by environment variable MODEL (see Config entries).""",
    verbose=True
)

agent_creativecontentcreator = Agent(
    role='Creative Content Creator',
    goal='Creative Content Creator',
    backstory="""Role: Creative Content Creator
Goal: Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact Instagram ad copies.
Backstory: As a Creative Content Creator at a top-tier digital marketing agency, you excel in crafting narratives that resonate with audiences on social media.
Tools: BrowserTools.scrape_and_summarize_website, SearchTools.search_internet, SearchTools.search_instagram
Verbose: True
Notes: Uses an Ollama model indicated by environment variable MODEL (see Config entries).""",
    verbose=True
)

agent_seniorphotographer = Agent(
    role='Senior Photographer',
    goal='Senior Photographer',
    backstory="""Role: Senior Photographer
Goal: Take the most amazing photographs for instagram ads that capture emotions and convey a compelling message.
Backstory: As a Senior Photographer at a leading digital marketing agency, you are an expert at taking amazing photographs that inspire and engage.
Tools: BrowserTools.scrape_and_summarize_website, SearchTools.search_internet, SearchTools.search_instagram
AllowDelegation: False
Verbose: True
Notes: This agent receives an 'ad copy' (produced by the Copy Crew) as input to a task that asks for 3 photograph options and descriptions; model usage: Ollama (MODEL env var).""",
    verbose=True
)

agent_chiefcreativedirector = Agent(
    role='Chief Creative Director',
    goal='Chief Creative Director',
    backstory="""Role: Chief Creative Director
Goal: Oversee the work done by your team to make sure it's the best possible and aligned with the product's goals, review, approve, ask clarifying question or delegate follow up work if necessary to make decisions.
Backstory: You're the Chief Content Officer of leading digital marketing specialized in product branding.
Tools: BrowserTools.scrape_and_summarize_website, SearchTools.search_internet, SearchTools.search_instagram
Verbose: True
Notes: This agent reviews photos returned by the photographer and may delegate follow-up tasks. Uses Ollama model (MODEL env var).""",
    verbose=True
)

# ===========================================================
# Tasks (ordered by workflow steps)
# ===========================================================

task_productanalysis = Task(
    description="""Analyze the given product website: {product_website}.
Extra details provided by the customer: {product_details}.

Focus on identifying unique features, benefits,
and the overall narrative presented.

Your final report should clearly articulate the
product's key selling points, its market appeal,
and suggestions for enhancement or positioning.
Emphasize the aspects that make the product stand out.

Keep in mind, attention to detail is crucial for
a comprehensive analysis. It's currenlty 2024.""",
    expected_output='A long, detailed product analysis report describing features, market appeal, recommendations.',
    agent=agent_productcompetitor
)

task_takephotograph = Task(
    description="""You are working on a new campaign for a super important customer,
and you MUST take the most amazing photo ever for an instagram post
regarding the product, you have the following copy:
{copy}

This is the product you are working with: {product_website}.
Extra details provided by the customer: {product_details}.

Imagine what the photo you wanna take describe it in a paragraph.
Here are some examples for you follow:
- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

Think creatively and focus on how the image can capture the audience's
attention. Don't show the actual product on the photo.

Your final answer must be 3 options of photographs, each with 1 paragraph
describing the photograph exactly like the examples provided above.""",
    expected_output='3 paragraph photograph descriptions.',
    agent=agent_seniorphotographer
)

task_competitoranalysis = Task(
    description="""Explore competitor of: {product_website}.
Extra details provided by the customer: {product_details}.

Identify the top 3 competitors and analyze their
strategies, market positioning, and customer perception.

Your final report MUST include BOTH all context about {product_website}
and a detailed comparison to whatever competitor they have competitors.""",
    expected_output='A competitor analysis report including top 3 competitors and detailed comparison to the product.',
    agent=agent_productcompetitor
)

task_reviewphoto = Task(
    description="""Review the photos you got from the senior photographer.
Make sure it's the best possible and aligned with the product's goals,
review, approve, ask clarifying question or delegate follow up work if
necessary to make decisions. When delegating work send the full draft
as part of the information.

This is the product you are working with: {product_website}.
Extra details provided by the customer: {product_details}.

Here are some examples on how the final photographs should look like:
- high tech airplaine in a beautiful blue sky in a beautiful sunset super cripsy beautiful 4k, professional wide shot
- the last supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
- an bearded old man in the snows, using very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

Your final answer must be 3 reviewed options of photographs,
each with 1 paragraph description following the examples provided above.""",
    expected_output='Three reviewed photograph descriptions with approval and optionally delegated follow-up instructions.',
    agent=agent_chiefcreativedirector
)

task_campaigndevelopment = Task(
    description="""You're creating a targeted marketing campaign for: {product_website}.
Extra details provided by the customer: {product_details}.

To start this campaing we will need a strategy and creative content ideas.
It should be meticulously designed to captivate and engage
the product's target audience.

Based on your ideas your co-workers will create the content for the campaign.

Your final answer MUST be ideas that will resonate with the audience and
also include ALL context you have about the product and the customer.""",
    expected_output='A campaign strategy and creative ideas that include full context.',
    agent=agent_strategyplanner
)

task_instagramadcopy = Task(
    description="""Craft an engaging Instagram post copy.
The copy should be punchy, captivating, concise,
and aligned with the product marketing strategy.

Focus on creating a message that resonates with
the target audience and highlights the product's
unique selling points.

Your ad copy must be attention-grabbing and should
encourage viewers to take action, whether it's
visiting the website, making a purchase, or learning
more about the product.

Your final answer MUST be 3 options for an ad copy for instagram that
not only informs but also excites and persuades the audience.""",
    expected_output='Three distinct Instagram ad copy options.',
    agent=agent_creativecontentcreator
)

# ===========================================================
# Crew & Main
# ===========================================================

def main():
    crew = Crew(
        agents=[agent_productcompetitor, agent_strategyplanner, agent_creativecontentcreator, agent_seniorphotographer, agent_chiefcreativedirector],
        tasks=[task_productanalysis, task_takephotograph, task_competitoranalysis, task_reviewphoto, task_campaigndevelopment, task_instagramadcopy],
        verbose=True
    )
    result = crew.kickoff()
    print(result)


if __name__ == "__main__":
    main()
