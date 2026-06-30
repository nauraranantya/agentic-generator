import asyncio

from team import (
    chef_agent,
    chef_agent_responses,
    chef_model_v2_agent,
    dynamic_agent,
    agent_that_harasses_you,
    error_agent,
    network_agent,
    weather_agent,
    eval_agent,
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
        # Workflow Step: task_my_step
        # Workflow Edge: task_my_step -> task_my_step_2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_my_step")
        print("=" * 80)

        task_prompt = """Task backing my-step. Performs the core recipe extraction (echo ingredient back) and returns result string."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_my_step_2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_my_step_2")
        print("=" * 80)

        task_prompt = """Second step in recipe-maker that finalizes the output; returns static placeholder 'suh' in the source."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_add_letter
        # Workflow Edge: task_add_letter -> task_add_letter_b
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_add_letter")
        print("=" * 80)

        task_prompt = """Execution: returns { text: text + 'A' } after ~500ms."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_add_letter_b
        # Workflow Edge: task_add_letter_b -> task_add_letter_c
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_add_letter_b")
        print("=" * 80)

        task_prompt = """Execution: returns { text: text + 'B' }."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_add_letter_c
        # Workflow Edge: task_add_letter_c -> task_add_letter_with_count
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_add_letter_c")
        print("=" * 80)

        task_prompt = """Execution: returns { text: text + 'C' }."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_add_letter_with_count
        # Workflow Edge: task_add_letter_with_count -> task_suspend_resume
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_add_letter_with_count")
        print("=" * 80)

        task_prompt = """Execution: returns text + 'D' and iterationCount+1."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_suspend_resume
        # Workflow Edge: task_suspend_resume -> task_short_text
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_suspend_resume")
        print("=" * 80)

        task_prompt = """Requires user input to resume. Modeled as a suspend/resume interactive step."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_short_text
        # Workflow Edge: task_short_text -> task_long_text
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_short_text")
        print("=" * 80)

        task_prompt = """Branch step executed when text length <= 10."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_long_text
        # Workflow Edge: task_long_text -> task_nested_text_processor
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_long_text")
        print("=" * 80)

        task_prompt = """Branch step executed when text length > 10."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_nested_text_processor
        # Workflow Edge: task_nested_text_processor -> task_final_step
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_nested_text_processor")
        print("=" * 80)

        task_prompt = """Executes nested sub-workflow that appends letters A then B."""
        # Execute via the assigned agent: chef_model_v2_agent
        result = await chef_model_v2_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_final_step
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_final_step")
        print("=" * 80)

        task_prompt = """Finalization operation adding '-ENDED'."""
        # Execute via the assigned agent: chef_agent
        result = await chef_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_one
        # Workflow Edge: task_step_one -> task_step_two
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_one")
        print("=" * 80)

        task_prompt = """Takes { inputValue }, returns { doubledValue: inputValue*2 }."""
        # Execute via the assigned agent: dynamic_agent
        result = await dynamic_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_two
        # Workflow Edge: task_step_two -> task_step_three
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_two")
        print("=" * 80)

        task_prompt = """If resumeData.extraNumber absent => suspend({}) and return interim; else compute incrementedValue."""
        # Execute via the assigned agent: dynamic_agent
        result = await dynamic_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_three
        # Workflow Edge: task_step_three -> task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_three")
        print("=" * 80)

        task_prompt = """Returns { tripledValue: incrementedValue * 3 }."""
        # Execute via the assigned agent: dynamic_agent
        result = await dynamic_agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_step_four
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_step_four")
        print("=" * 80)

        task_prompt = """Returns { isEven: tripledValue % 2 === 0 }."""
        # Execute via the assigned agent: dynamic_agent
        result = await dynamic_agent.run(task=task_prompt)

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