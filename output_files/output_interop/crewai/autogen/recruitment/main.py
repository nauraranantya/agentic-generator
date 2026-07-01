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

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: task_research_candidates
        # Workflow Edge: task_research_candidates -> task_match_and_score_candidates
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_research_candidates")
        print("=" * 80)

        task_prompt = """Conduct thorough research to find potential candidates for the specified job. Utilize various online resources and databases to gather a comprehensive list of potential candidates. Ensure that the candidates meet the job requirements provided. """
        # Execute via the assigned agent: researcher
        result = await researcher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_match_and_score_candidates
        # Workflow Edge: task_match_and_score_candidates -> task_outreach_strategy
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_match_and_score_candidates")
        print("=" * 80)

        task_prompt = """Evaluate and match the candidates to the best job positions based on their qualifications and suitability. Score each candidate to reflect their alignment with the job requirements, ensuring a fair and transparent assessment process. """
        # Execute via the assigned agent: matcher
        result = await matcher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_outreach_strategy
        # Workflow Edge: task_outreach_strategy -> task_report_candidates
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_outreach_strategy")
        print("=" * 80)

        task_prompt = """Develop a comprehensive strategy to reach out to the selected candidates. Create effective outreach methods and templates that can engage the candidates and encourage them to consider the job opportunity. """
        # Execute via the assigned agent: communicator
        result = await communicator.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_report_candidates
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_report_candidates")
        print("=" * 80)

        task_prompt = """Compile a comprehensive report for recruiters on the best candidates to put forward. Summarize the findings from the previous tasks and provide clear recommendations based on the job requirements. """
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