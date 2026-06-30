import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Get git diff task
export const get_git_diff_task = createStep({
  id: 'get_git_diff_task',
  description: `Reads staged changes from a git repository at repoPath. Produces 'diff' string resource.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Read conventional commit spec
export const read_conventional_commit_spec = createStep({
  id: 'read_conventional_commit_spec',
  description: `Read file data/crawl/conventional-commit.json using fsTool action 'read'. If not present, fallback to built-in guidelines.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Generate commit message
export const generate_commit_message = createStep({
  id: 'generate_commit_message',
  description: `Agent is asked to produce commit message and meta information. If diff empty return 'No staged changes found' and generated=false; otherwise return generated=true and commit message string.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: User confirmation
export const user_confirmation = createStep({
  id: 'user_confirmation',
  description: `Interactive confirmation step; modeled as a task that expects boolean response. Implementation uses inquirer.prompt confirm.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Create git commit task
export const create_git_commit_task = createStep({
  id: 'create_git_commit_task',
  description: `Performs git commit using execaTool after confirmation. Produces commit status.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Start message
export const start_message = createStep({
  id: 'start_message',
  description: `Initial step produces a message string 'Test'.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Pass message through (user input)
export const pass_message_through_user_input = createStep({
  id: 'pass_message_through_user_input',
  description: `Prompts user to enter a message; ensures non-empty.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Check message exists
export const check_message_exists = createStep({
  id: 'check_message_exists',
  description: `Verifies the message exists in workflow state and returns it; may throw if not found.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Ask modify message
export const ask_modify_message = createStep({
  id: 'ask_modify_message',
  description: `If resumeData.confirm is true, agent.generate is called to change the message; otherwise workflow suspends.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Pass final message
export const pass_final_message = createStep({
  id: 'pass_final_message',
  description: `Returns message from stepC2.output to finish the workflow.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Get broken links task
export const get_broken_links_task = createStep({
  id: 'get_broken_links_task',
  description: `Runs linkinator, parse results and outputs array of broken link objects: { url, status, state, parent? }.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Report broken links to Slack
export const report_broken_links_to_slack = createStep({
  id: 'report_broken_links_to_slack',
  description: `Agent asked to format the broken link list as Slack-friendly markdown and to send to specified channel using Slack toolset returned by MCP.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Generate per-module changelog
export const generate_per_module_changelog = createStep({
  id: 'generate_per_module_changelog',
  description: `For each module with changes, agent.generate is invoked with: Time window, Module path, Git diff, and tasks to create structured narrative changelog grouped by categories (New features, Improvements, Notable bug fixes, Build/deployment improvements, Performance optimizations).`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Compile changelog and post to Slack
export const compile_changelog_and_post_to_slack = createStep({
  id: 'compile_changelog_and_post_to_slack',
  description: `Combines module summaries and requests agent to format full changelog message then uses Slack toolset to post to channel.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Build all packages
export const build_all_packages = createStep({
  id: 'build_all_packages',
  description: `Build monorepo packages; may call pnpmBuild per-package or run root-level pnpm run build as implementation.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Publish all packages
export const publish_all_packages = createStep({
  id: 'publish_all_packages',
  description: `Executes publish step and expects success; on error reporting, stop workflow.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Set dist tags
export const set_dist_tags = createStep({
  id: 'set_dist_tags',
  description: `Iterates package.json files under package directories and runs npm dist-tag add <pkg>@<version> latest.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: User chat input
export const user_chat_input = createStep({
  id: 'user_chat_input',
  description: `Prompt user with '\\n You:' and validate non-empty input; returns {message: string}.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Agent response generation
export const agent_response_generation = createStep({
  id: 'agent_response_generation',
  description: `Agent receives message, optional context: resourceId/threadId, and produces textual response. Supports streaming of text.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Fetch issue from GitHub
export const fetch_issue_from_git_hub = createStep({
  id: 'fetch_issue_from_git_hub',
  description: `Uses GitHub integration to get issue and labels. Output: title, body, labelNames[]`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Generate labels task
export const generate_labels_task = createStep({
  id: 'generate_labels_task',
  description: `Agent is prompted with issue title/body and available labels; returns labels array.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Apply labels to GitHub issue
export const apply_labels_to_git_hub_issue = createStep({
  id: 'apply_labels_to_git_hub_issue',
  description: `Uses GitHub integration to add labels to issue.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Get pull request
export const get_pull_request = createStep({
  id: 'get_pull_request',
  description: `Fetch PR via GitHub client and fetch diff URL to retrieve diff text.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Generate new contributor message
export const generate_new_contributor_message = createStep({
  id: 'generate_new_contributor_message',
  description: `Agent provided PR title/body/diff and Mastra docs; generate intro, checklist entries based on guidelines, and outro.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: Create PR comment
export const create_pr_comment = createStep({
  id: 'create_pr_comment',
  description: `Uses GitHub API to create a comment with intro, checklist as - [ ] items, and outro.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
