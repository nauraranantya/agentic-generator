import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraagentsystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_execa_tool
const tool_execa_tool = tool(
  async () => {
    return "Result of tool_execa_tool";
  },
  {
    name: "tool_execa_tool",
    description: "Tool wrapping execa to run commands and stream output to console. Input: {command, args}. Output: {message}.",
    schema: z.object({}),
  }
);
// Tool: tool_fs_tool
const tool_fs_tool = tool(
  async () => {
    return "Result of tool_fs_tool";
  },
  {
    name: "tool_fs_tool",
    description: "File system tool to read/write/append files.",
    schema: z.object({}),
  }
);
// Tool: tool_slack_mcp
const tool_slack_mcp = tool(
  async () => {
    return "Result of tool_slack_mcp";
  },
  {
    name: "tool_slack_mcp",
    description: "MCP client configured to run Slack container. Exposes tools for posting to Slack.",
    schema: z.object({}),
  }
);
// Tool: tool_list_events
const tool_list_events = tool(
  async () => {
    return "Result of tool_list_events";
  },
  {
    name: "tool_list_events",
    description: "Tool that lists calendar events by reading Mac Calendar via AppleScript and parsing into event objects.",
    schema: z.object({}),
  }
);
// Tool: tool_browser_tool
const tool_browser_tool = tool(
  async () => {
    return "Result of tool_browser_tool";
  },
  {
    name: "tool_browser_tool",
    description: "Opens a headless chromium browser, retrieves page content and returns chunked textual document representation.",
    schema: z.object({}),
  }
);
// Tool: tool_google_search
const tool_google_search = tool(
  async () => {
    return "Result of tool_google_search";
  },
  {
    name: "tool_google_search",
    description: "Performs a Google search and returns a list of result URLs.",
    schema: z.object({}),
  }
);
// Tool: tool_read_pdf
const tool_read_pdf = tool(
  async () => {
    return "Result of tool_read_pdf";
  },
  {
    name: "tool_read_pdf",
    description: "Reads PDF file and extracts textual content; validates file path and type.",
    schema: z.object({}),
  }
);
// Tool: tool_pnpm_build
const tool_pnpm_build = tool(
  async () => {
    return "Result of tool_pnpm_build";
  },
  {
    name: "tool_pnpm_build",
    description: "Build a package using pnpm run build at provided packagePath. Input: {name, packagePath}.",
    schema: z.object({}),
  }
);
// Tool: tool_pnpm_changeset_status
const tool_pnpm_changeset_status = tool(
  async () => {
    return "Result of tool_pnpm_changeset_status";
  },
  {
    name: "tool_pnpm_changeset_status",
    description: "Checks 'pnpm publish -r --dry-run --no-git-checks' to determine which packages need to be published. Returns array of package names.",
    schema: z.object({}),
  }
);
// Tool: tool_pnpm_changeset_publish
const tool_pnpm_changeset_publish = tool(
  async () => {
    return "Result of tool_pnpm_changeset_publish";
  },
  {
    name: "tool_pnpm_changeset_publish",
    description: "Publishes packages via pnpm changeset publish.",
    schema: z.object({}),
  }
);
// Tool: tool_active_dist_tag
const tool_active_dist_tag = tool(
  async () => {
    return "Result of tool_active_dist_tag";
  },
  {
    name: "tool_active_dist_tag",
    description: "Sets an npm dist tag on a package using npm dist-tag add <pkg>@<version> latest.",
    schema: z.object({}),
  }
);



/**
 * Node: getGitDiffTask
 * Agent: dane
 */
async function getGitDiffTask(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: getGitDiffTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: readConventionalCommitSpec
 * Agent: dane
 */
async function readConventionalCommitSpec(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: readConventionalCommitSpec",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: generateCommitMessage
 * Agent: dane_commit_message
 */
async function generateCommitMessage(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: generateCommitMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: userConfirmation
 * Agent: dane
 */
async function userConfirmation(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: userConfirmation",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: createGitCommitTask
 * Agent: dane
 */
async function createGitCommitTask(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: createGitCommitTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: startMessage
 * Agent: dane
 */
async function startMessage(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: startMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: passMessageThroughUserInput
 * Agent: dane
 */
async function passMessageThroughUserInput(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: passMessageThroughUserInput",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: checkMessageExists
 * Agent: dane
 */
async function checkMessageExists(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: checkMessageExists",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: askModifyMessage
 * Agent: dane
 */
async function askModifyMessage(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: askModifyMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: passFinalMessage
 * Agent: dane
 */
async function passFinalMessage(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: passFinalMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getBrokenLinksTask
 * Agent: dane
 */
async function getBrokenLinksTask(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: getBrokenLinksTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: reportBrokenLinksToSlack
 * Agent: dane_link_checker
 */
async function reportBrokenLinksToSlack(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: reportBrokenLinksToSlack",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: generatePerModuleChangelog
 * Agent: dane_package_publisher
 */
async function generatePerModuleChangelog(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: generatePerModuleChangelog",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: compileChangelogAndPostToSlack
 * Agent: dane_package_publisher
 */
async function compileChangelogAndPostToSlack(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: compileChangelogAndPostToSlack",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: buildAllPackages
 * Agent: dane
 */
async function buildAllPackages(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: buildAllPackages",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: publishAllPackages
 * Agent: dane
 */
async function publishAllPackages(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: publishAllPackages",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: setDistTags
 * Agent: dane
 */
async function setDistTags(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: setDistTags",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: userChatInput
 * Agent: dane
 */
async function userChatInput(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: userChatInput",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: agentResponseGeneration
 * Agent: dane
 */
async function agentResponseGeneration(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: agentResponseGeneration",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: fetchIssueFromGitHub
 * Agent: dane
 */
async function fetchIssueFromGitHub(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: fetchIssueFromGitHub",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: generateLabelsTask
 * Agent: dane_issue_labeler
 */
async function generateLabelsTask(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: generateLabelsTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: applyLabelsToGitHubIssue
 * Agent: dane
 */
async function applyLabelsToGitHubIssue(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: applyLabelsToGitHubIssue",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: getPullRequest
 * Agent: dane
 */
async function getPullRequest(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: getPullRequest",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: generateNewContributorMessage
 * Agent: dane_new_contributor
 */
async function generateNewContributorMessage(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: generateNewContributorMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: createPrComment
 * Agent: dane
 */
async function createPrComment(state: typeof MastraagentsystemAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-20241022" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a assistant." +
        "\nNode: createPrComment",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraagentsystemAnnotation)
  .addNode("getGitDiffTask", getGitDiffTask)
  .addNode("readConventionalCommitSpec", readConventionalCommitSpec)
  .addNode("generateCommitMessage", generateCommitMessage)
  .addNode("userConfirmation", userConfirmation)
  .addNode("createGitCommitTask", createGitCommitTask)
  .addNode("startMessage", startMessage)
  .addNode("passMessageThroughUserInput", passMessageThroughUserInput)
  .addNode("checkMessageExists", checkMessageExists)
  .addNode("askModifyMessage", askModifyMessage)
  .addNode("passFinalMessage", passFinalMessage)
  .addNode("getBrokenLinksTask", getBrokenLinksTask)
  .addNode("reportBrokenLinksToSlack", reportBrokenLinksToSlack)
  .addNode("generatePerModuleChangelog", generatePerModuleChangelog)
  .addNode("compileChangelogAndPostToSlack", compileChangelogAndPostToSlack)
  .addNode("buildAllPackages", buildAllPackages)
  .addNode("publishAllPackages", publishAllPackages)
  .addNode("setDistTags", setDistTags)
  .addNode("userChatInput", userChatInput)
  .addNode("agentResponseGeneration", agentResponseGeneration)
  .addNode("fetchIssueFromGitHub", fetchIssueFromGitHub)
  .addNode("generateLabelsTask", generateLabelsTask)
  .addNode("applyLabelsToGitHubIssue", applyLabelsToGitHubIssue)
  .addNode("getPullRequest", getPullRequest)
  .addNode("generateNewContributorMessage", generateNewContributorMessage)
  .addNode("createPrComment", createPrComment)
  .addEdge(START, "getGitDiffTask")
  .addEdge("getGitDiffTask", "readConventionalCommitSpec")
  .addEdge("readConventionalCommitSpec", "generateCommitMessage")
  .addEdge("generateCommitMessage", "userConfirmation")
  .addEdge("userConfirmation", "createGitCommitTask")
  .addEdge("createGitCommitTask", "startMessage")
  .addEdge("startMessage", "passMessageThroughUserInput")
  .addEdge("passMessageThroughUserInput", "checkMessageExists")
  .addEdge("checkMessageExists", "askModifyMessage")
  .addEdge("askModifyMessage", "passFinalMessage")
  .addEdge("passFinalMessage", "getBrokenLinksTask")
  .addEdge("getBrokenLinksTask", "reportBrokenLinksToSlack")
  .addEdge("reportBrokenLinksToSlack", "generatePerModuleChangelog")
  .addEdge("generatePerModuleChangelog", "compileChangelogAndPostToSlack")
  .addEdge("compileChangelogAndPostToSlack", "buildAllPackages")
  .addEdge("buildAllPackages", "publishAllPackages")
  .addEdge("publishAllPackages", "setDistTags")
  .addEdge("setDistTags", "userChatInput")
  .addEdge("userChatInput", "agentResponseGeneration")
  .addEdge("agentResponseGeneration", "fetchIssueFromGitHub")
  .addEdge("fetchIssueFromGitHub", "generateLabelsTask")
  .addEdge("generateLabelsTask", "applyLabelsToGitHubIssue")
  .addEdge("applyLabelsToGitHubIssue", "getPullRequest")
  .addEdge("getPullRequest", "generateNewContributorMessage")
  .addEdge("generateNewContributorMessage", "createPrComment")
  .addEdge("createPrComment", END)
;

export const graph = workflow.compile();
graph.name = "Mastraagentsystem";
// Workflow: workflow_commit_message
// Workflow: commit-message workflow
// Workflow: workflow_telephone_game
// Workflow: telephoneGame workflow
// Workflow: workflow_link_checker
// Workflow: link-checker workflow
// Workflow: workflow_changelog
// Workflow: changelog workflow
// Workflow: workflow_package_publisher
// Workflow: pnpm-changset-publisher
// Workflow: workflow_message
// Workflow: message (entry) workflow
// Workflow: workflow_github_issue_labeler
// Workflow: github-issue-labeler workflow
// Workflow: workflow_github_first_contributor
// Workflow: github-first-contributor-message workflow
