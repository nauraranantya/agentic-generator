import asyncio

from team import (
    email_assistant_agent,
    human_user,
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
        # Workflow Step: task_write_email
        # Workflow Edge: task_write_email -> task_write_email
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_write_email")
        print("=" * 80)

        task_prompt = """LLM task that generates an initial email draft from conversation history. """
        # Execute via the assigned agent: email_assistant_agent
        result = await email_assistant_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_interrupt
        # Workflow Edge: task_interrupt -> task_send_email
        # Workflow Edge: task_interrupt -> task_rewrite_email
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_interrupt")
        print("=" * 80)

        task_prompt = """Human-in-the-loop interruption UI which can edit, accept, ignore, or request a rewrite. """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_rewrite_email
        # Workflow Edge: task_rewrite_email -> task_interrupt
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_rewrite_email")
        print("=" * 80)

        task_prompt = """LLM task that rewrites the email according to user edits or responses. """
        # Execute via the assigned agent: email_assistant_agent
        result = await email_assistant_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_send_email
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_send_email")
        print("=" * 80)

        task_prompt = """Finalization step that sends/renders the sent email confirmation. """
        # Execute via the assigned agent: email_assistant_agent
        result = await email_assistant_agent.run(task=task_prompt)

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