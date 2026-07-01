import asyncio

from team import (
    dane,
    dane_commit_message,
    dane_issue_labeler,
    dane_link_checker,
    dane_change_log,
    dane_new_contributor,
    dane_package_publisher,
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
        # Workflow Step: task_changelog_step_a1
        # Workflow Edge: task_changelog_step_a1 -> task_changelog_step_a2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_changelog_step_a1")
        print("=" * 80)

        task_prompt = """Get a git diff and connect to slack; runs git diff via execa """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_changelog_step_a2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_changelog_step_a2")
        print("=" * 80)

        task_prompt = """Generate changelog using the daneChangeLog agent and post to Slack """
        # Execute via the assigned agent: dane_change_log
        result = await dane_change_log.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_entry_message_input
        # Workflow Edge: task_entry_message_input -> task_entry_message_output
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_entry_message_input")
        print("=" * 80)

        task_prompt = """Prompt user to input a message (inquirer prompt) """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_entry_message_output
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_entry_message_output")
        print("=" * 80)

        task_prompt = """Send user message to Dane agent and stream/generate response """
        # Execute via the assigned agent: dane
        result = await dane.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_commit_get_diff
        # Workflow Edge: task_commit_get_diff -> task_commit_read_conventional_commit_spec
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_commit_get_diff")
        print("=" * 80)

        task_prompt = """Compute git diff of staged changes via git command """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_commit_read_conventional_commit_spec
        # Workflow Edge: task_commit_read_conventional_commit_spec -> task_commit_generate_message
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_commit_read_conventional_commit_spec")
        print("=" * 80)

        task_prompt = """Read conventional commit spec using fsTool """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_commit_generate_message
        # Workflow Edge: task_commit_generate_message -> task_commit_confirmation
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_commit_generate_message")
        print("=" * 80)

        task_prompt = """Generate commit message using DaneCommitMessage agent """
        # Execute via the assigned agent: dane_commit_message
        result = await dane_commit_message.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_commit_confirmation
        # Workflow Edge: task_commit_confirmation -> task_commit_commit
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_commit_confirmation")
        print("=" * 80)

        task_prompt = """Prompt human user to confirm commit message via inquirer confirm """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_commit_commit
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_commit_commit")
        print("=" * 80)

        task_prompt = """Perform git commit with generated message (execSync git commit) """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_first_get_pull_request
        # Workflow Edge: task_first_get_pull_request -> task_first_message_generator
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_first_get_pull_request")
        print("=" * 80)

        task_prompt = """Retrieve pull request data from GitHub integration and fetch diff """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_first_message_generator
        # Workflow Edge: task_first_message_generator -> task_first_create_message
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_first_message_generator")
        print("=" * 80)

        task_prompt = """Generate contributor welcome message using DaneNewContributor agent using PR title/body/diff and Mastra docs """
        # Execute via the assigned agent: dane_new_contributor
        result = await dane_new_contributor.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_first_create_message
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_first_create_message")
        print("=" * 80)

        task_prompt = """Post generated message as GitHub issue comment using github integration """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_issue_get_issue
        # Workflow Edge: task_issue_get_issue -> task_issue_label_issue
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_issue_get_issue")
        print("=" * 80)

        task_prompt = """Retrieve issue and repository labels using GitHub integration """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_issue_label_issue
        # Workflow Edge: task_issue_label_issue -> task_issue_apply_labels
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_issue_label_issue")
        print("=" * 80)

        task_prompt = """Use DaneIssueLabeler agent to decide labels for an issue """
        # Execute via the assigned agent: dane_issue_labeler
        result = await dane_issue_labeler.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_issue_apply_labels
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_issue_apply_labels")
        print("=" * 80)

        task_prompt = """Add labels to GitHub issue using integrations client """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_link_get_broken_links
        # Workflow Edge: task_link_get_broken_links -> task_link_report_broken_links
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_link_get_broken_links")
        print("=" * 80)

        task_prompt = """Run linkinator via shell to collect links; parse JSON output """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_link_report_broken_links
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_link_report_broken_links")
        print("=" * 80)

        task_prompt = """Report broken links by generating a message with DaneLinkChecker and posting to Slack """
        # Execute via the assigned agent: dane_link_checker
        result = await dane_link_checker.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_get_pacakges_to_publish
        # Workflow Edge: task_pkg_get_pacakges_to_publish -> task_pkg_assemble_packages
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_get_pacakges_to_publish")
        print("=" * 80)

        task_prompt = """Use DanePackagePublisher agent to analyze repo and list packages requiring publish """
        # Execute via the assigned agent: dane_package_publisher
        result = await dane_package_publisher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_assemble_packages
        # Workflow Edge: task_pkg_assemble_packages -> task_pkg_build_packages
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_assemble_packages")
        print("=" * 80)

        task_prompt = """Assemble file system paths for the packages reported by the agent and prepare build sets """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_build_packages
        # Workflow Edge: task_pkg_build_packages -> task_pkg_verify_build
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_build_packages")
        print("=" * 80)

        task_prompt = """Build packages using pnpmBuild tool for each package path (sequential and parallel phases) """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_verify_build
        # Workflow Edge: task_pkg_verify_build -> task_pkg_publish_changeset
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_verify_build")
        print("=" * 80)

        task_prompt = """Verify dist artifacts exist for all built packages """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_publish_changeset
        # Workflow Edge: task_pkg_publish_changeset -> task_pkg_set_latest_dist_tag
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_publish_changeset")
        print("=" * 80)

        task_prompt = """Use DanePackagePublisher agent to publish changeset (agent generates instructions) and then call pnpmChangesetPublish """
        # Execute via the assigned agent: dane_package_publisher
        result = await dane_package_publisher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_pkg_set_latest_dist_tag
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_pkg_set_latest_dist_tag")
        print("=" * 80)

        task_prompt = """Update npm dist-tag for published packages (agent assisted) """
        # Execute via the assigned agent: dane_package_publisher
        result = await dane_package_publisher.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tel_step_a1
        # Workflow Edge: task_tel_step_a1 -> task_tel_step_a2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tel_step_a1")
        print("=" * 80)

        task_prompt = """Create starting message for telephone game """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tel_step_a2
        # Workflow Edge: task_tel_step_a2 -> task_tel_step_b2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tel_step_a2")
        print("=" * 80)

        task_prompt = """Prompt user for a message (inquirer input) """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tel_step_b2
        # Workflow Edge: task_tel_step_b2 -> task_tel_step_c2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tel_step_b2")
        print("=" * 80)

        task_prompt = """Validate that the input message exists and pass through """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tel_step_c2
        # Workflow Edge: task_tel_step_c2 -> task_tel_step_d2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tel_step_c2")
        print("=" * 80)

        task_prompt = """Optionally suspend and ask user to confirm modification; if confirmed, call inline LLM (claude-3-5-haiku) to modify message """
        # Execute via the assigned agent: dane
        result = await dane.run(task=task_prompt)

        # Print step output
        if hasattr(result, "messages") and result.messages:
            print(result.messages[-1].content)
        else:
            print(result)

        # ==================================================
        # Workflow Step: task_tel_step_d2
        # ==================================================
        print("\n" + "=" * 80)
        print("Executing step: task_tel_step_d2")
        print("=" * 80)

        task_prompt = """Pass the final message to the next participant or output """
        # Execute via the assigned agent: agent
        result = await agent.run(task=task_prompt)

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