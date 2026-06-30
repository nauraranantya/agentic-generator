import asyncio

from team import (
    researcher,
    matcher,
    communicator,
    reporter,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "job_requirements":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: research_candidates_task
        # Workflow Edge: research_candidates_task -> match_and_score_candidates_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: research_candidates_task")
        print("=" * 80)

        task_prompt = """Conduct thorough research to find potential candidates for the specified job.
Utilize various online resources and databases to gather a comprehensive list of potential candidates.
Ensure that the candidates meet the job requirements provided.

Job Requirements:
{job_requirements}"""
        # Execute via the assigned agent: researcher
        result = await researcher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: match_and_score_candidates_task
        # Workflow Edge: match_and_score_candidates_task -> outreach_strategy_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: match_and_score_candidates_task")
        print("=" * 80)

        task_prompt = """Evaluate and match the candidates to the best job positions based on their qualifications and suitability.
Score each candidate to reflect their alignment with the job requirements, ensuring a fair and transparent assessment process.
Don't try to scrape people's linkedin, since you don't have access to it.

Job Requirements:
{job_requirements}"""
        # Execute via the assigned agent: matcher
        result = await matcher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: outreach_strategy_task
        # Workflow Edge: outreach_strategy_task -> report_candidates_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: outreach_strategy_task")
        print("=" * 80)

        task_prompt = """Develop a comprehensive strategy to reach out to the selected candidates.
Create effective outreach methods and templates that can engage the candidates and encourage them to consider the job opportunity.

Job Requirements:
{job_requirements}"""
        # Execute via the assigned agent: communicator
        result = await communicator.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: report_candidates_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: report_candidates_task")
        print("=" * 80)

        task_prompt = """Compile a comprehensive report for recruiters on the best candidates to put forward.
Summarize the findings from the previous tasks and provide clear recommendations based on the job requirements."""
        # Execute via the assigned agent: reporter
        result = await reporter.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        print("\n" + "=" * 80)
        print("DONE")
        print("=" * 80)

    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR")
        print("=" * 80)
        print(type(e).__name__)
        print(str(e))



if __name__ == "__main__":
    asyncio.run(main())