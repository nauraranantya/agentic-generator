import asyncio

from team import (
    email_assistant_agent,
    user_human,
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
        # Workflow Step: write_email_generate_draft
        # Workflow Edge: write_email_generate_draft -> ignore
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: write_email_generate_draft")
        print("=" * 80)

        task_prompt = """Generates a draft email (subject, body, to) by invoking the LLM with the Write Email Prompt and a tool named "write_email" implementing the sendEmailSchema. If insufficient information, prompts the user for missing information. Produces Draft Email resource and a model response message."""
        # Execute via the assigned agent: email_assistant_agent
        result = await email_assistant_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: ignore
        # Workflow Edge: ignore -> rewrite_email_apply_user_s_requested_changes
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: ignore")
        print("=" * 80)

        task_prompt = """Presents the current draft email to a human actor with allowed actions: ignore, response, edit, accept. If 'ignore' or no response -> ends conversation. If 'response' -> passes human text to rewriteEmail. If 'accept' or 'edit' (with structured args) -> may send or update the draft depending on edit content. Implementation validates edits contain subject, body, to when edit action used."""
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: rewrite_email_apply_user_s_requested_changes
        # Workflow Edge: rewrite_email_apply_user_s_requested_changes -> ignore
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: rewrite_email_apply_user_s_requested_changes")
        print("=" * 80)

        task_prompt = """Rewrites a previously generated draft email in response to a human 'response' action. It uses the Rewrite Email Prompt with substitution of the current draft and the human response text; it calls the same structured tool (write_email) and returns a new Draft Email resource. Implementation enforces: only proceed if humanResponse.args is a string and an existing email exists; otherwise error."""
        # Execute via the assigned agent: email_assistant_agent
        result = await email_assistant_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: send_email_finalize_send
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: send_email_finalize_send")
        print("=" * 80)

        task_prompt = """Finalizes and sends the email. In the implementation this yields a confirmation AI message 'Successfully sent email.' and produces a SentEmailRecord resource. This task is reached when the human accepts or when routing logic selects sending directly."""
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