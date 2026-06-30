import asyncio

from team import (
    writer_annotation_agent_uuid_1,
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
        # Workflow Step: prepare_task
        # Workflow Edge: prepare_task -> write_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: prepare_task")
        print("=" * 80)

        task_prompt = """Binds the tool 'draft_text_document' with the model and streams its output (initStream). If state.context.writer.selected is present, a system message of 'Selected text in question: <selected>' is prepended. As model stream chunks arrive, tool call arguments (title, description) are extracted and a UI 'writer' component is populated with these arguments and isGenerating=true. Produces a draft candidate resource representing the tool call output."""
        # Execute via the assigned agent: writer_annotation_agent_uuid_1
        result = await writer_annotation_agent_uuid_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: write_task
        # Workflow Edge: write_task -> suggestions_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: write_task")
        print("=" * 80)

        task_prompt = """Generates the final text document content. Uses a non-streaming model invocation (tags ['nostream']) in implementation to get full content; however the code also uses a streaming invocation to update UI content progressively. System instruction: 'Write a text document based on the user's request. Only output the content, do not ask any additional questions.' If state.context.writer.selected is present the selected text is appended to the system instruction. Consumes conversation history and tool outputs; produces the final document content resource (FinalTextDocument)."""
        # Execute via the assigned agent: writer_annotation_agent_uuid_1
        result = await writer_annotation_agent_uuid_1.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: suggestions_task
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: suggestions_task")
        print("=" * 80)

        task_prompt = """Takes the last AI message; for each tool call in the message, emits a tool-type message 'Finished' referencing the tool_call id. Then invokes the model with the updated messages and appends the model's finish message to the conversation. This step does non-streaming invocation in the implementation (model.invoke)."""
        # Execute via the assigned agent: writer_annotation_agent_uuid_1
        result = await writer_annotation_agent_uuid_1.run(task=task_prompt)

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