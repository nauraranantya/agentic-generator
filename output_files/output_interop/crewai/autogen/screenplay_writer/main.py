import asyncio

from team import (
    spamfilter,
    analyst,
    scriptwriter,
    formatter,
    scorer,
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
        # Workflow Step: task1_analysis
        # Workflow Edge: task1_analysis -> task2_scriptwriting
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task1_analysis")
        print("=" * 80)

        task_prompt = """Analyse in much detail the following discussion:
### DISCUSSION:
(see :discussion_newsgroup_01)"""
        # Execute via the assigned agent: analyst
        result = await analyst.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task2_scriptwriting
        # Workflow Edge: task2_scriptwriting -> task3_formatting
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task2_scriptwriting")
        print("=" * 80)

        task_prompt = """Create a dialogue heavy screenplay from the discussion, between two persons. Do NOT write parentheticals. Leave out wrylies. You MUST SKIP directional notes."""
        # Execute via the assigned agent: scriptwriter
        result = await scriptwriter.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task3_formatting
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task3_formatting")
        print("=" * 80)

        task_prompt = """Format the script exactly like this:
  ## (person 1):
  (first text line from person 1)
         
  ## (person 2):
  (first text line from person 2)
         
  ## (person 1):
  (second text line from person 1)
         
  ## (person 2):
  (second text line from person 2)"""
        # Execute via the assigned agent: formatter
        result = await formatter.run(task=task_prompt)

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