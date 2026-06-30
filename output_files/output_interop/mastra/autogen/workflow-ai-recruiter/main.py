import asyncio

from team import (
    recruiter_agent,
)

from autogen_agentchat.conditions import (
    MaxMessageTermination,
)

INPUTS = {


    "resumeText":
        "",


    "candidateName":
        "",


    "specialty":
        "",

}


async def main():
    try:
        # Step-by-step sequential execution
        # ==================================================
        # Workflow Step: gather_candidate_info
        # Workflow Edge: gather_candidate_info -> ask_about_specialty
        # Workflow Edge: gather_candidate_info -> ask_about_role
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: gather_candidate_info")
        print("=" * 80)

        task_prompt = """Input schema (Zod): { resumeText: string }
Output schema (Zod): {
  candidateName: string,
  isTechnical: boolean,
  specialty: string,
  resumeText: string
}
Execution summary:
- Reads 'resumeText' from the workflow trigger context (context.getStepResult('trigger')?.resumeText).
- Constructs the prompt template below, substitutes resumeText, and sends it to the recruiter agent.
- Expects the agent output to be parsed into the defined output schema.
Prompt template (literal):
  You are given this resume text:
  "${resumeText}"
The task uses the recruiter agent's generation functionality (with an explicit output schema in the implementation) to produce structured candidate information."""
        # Execute via the assigned agent: recruiter_agent
        result = await recruiter_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: ask_about_specialty
        # Workflow Edge: ask_about_specialty -> ask_about_role
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: ask_about_specialty")
        print("=" * 80)

        task_prompt = """Output schema (Zod): { question: string }
Execution summary:
- Reads candidateInfo produced by gatherCandidateInfo (candidateName, specialty, resumeText).
- Generates a short, targeted question about how the candidate got into their specialty.
Prompt template (literal):
  You are a recruiter. Given the resume below, craft a short question
  for ${candidateName} about how they got into "${specialty}".
  Resume: ${resumeText}
The generated text is trimmed and returned as the 'question' field."""
        # Execute via the assigned agent: recruiter_agent
        result = await recruiter_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: ask_about_role
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: ask_about_role")
        print("=" * 80)

        task_prompt = """Output schema (Zod): { question: string }
Execution summary:
- Reads candidateInfo produced by gatherCandidateInfo (candidateName, resumeText).
- Generates a short question asking what interests the candidate most about the role.
Prompt template (literal):
  You are a recruiter. Given the resume below, craft a short question
  for ${candidateName} asking what interests them most about this role.
  Resume: ${resumeText}
The generated text is trimmed and returned as the 'question' field."""
        # Execute via the assigned agent: recruiter_agent
        result = await recruiter_agent.run(task=task_prompt)

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