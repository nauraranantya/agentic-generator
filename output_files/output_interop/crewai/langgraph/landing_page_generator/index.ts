import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const ExpandIdeaCrewteamAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: search_internet_tool
const search_internet_tool = tool(
  async () => {
    return "Result of search_internet_tool";
  },
  {
    name: "search_internet_tool",
    description: "Performs internet search using an external search API (serper.dev). Requires SERPER_API_KEY environment variable.",
    schema: z.object({}),
  }
);
// Tool: scrape_website_tool
const scrape_website_tool = tool(
  async () => {
    return "Result of scrape_website_tool";
  },
  {
    name: "scrape_website_tool",
    description: "Scrapes website HTML via browserless API and summarizes content using an internal summarization Task. Requires BROWSERLESS_API_KEY environment variable.",
    schema: z.object({}),
  }
);
// Tool: write_file_tool
const write_file_tool = tool(
  async () => {
    return "Result of write_file_tool";
  },
  {
    name: "write_file_tool",
    description: "Writes files into ./workdir with path sanitization and allowed extensions.",
    schema: z.object({}),
  }
);
// Tool: learn_templates_tool
const learn_templates_tool = tool(
  async () => {
    return "Result of learn_templates_tool";
  },
  {
    name: "learn_templates_tool",
    description: "Reads config/templates.json to list available templates.",
    schema: z.object({}),
  }
);
// Tool: copy_template_tool
const copy_template_tool = tool(
  async () => {
    return "Result of copy_template_tool";
  },
  {
    name: "copy_template_tool",
    description: "Copies a template folder from ./templates to ./workdir with safety checks.",
    schema: z.object({}),
  }
);
// Tool: read_file_tool
const read_file_tool = tool(
  async () => {
    return "Result of read_file_tool";
  },
  {
    name: "read_file_tool",
    description: "Read file contents from workdir (used by agent toolkits).",
    schema: z.object({}),
  }
);
// Tool: list_directory_tool
const list_directory_tool = tool(
  async () => {
    return "Result of list_directory_tool";
  },
  {
    name: "list_directory_tool",
    description: "List directories in workdir (used by agent toolkits).",
    schema: z.object({}),
  }
);
// Tool: file_management_toolkit
const file_management_toolkit = tool(
  async () => {
    return "Result of file_management_toolkit";
  },
  {
    name: "file_management_toolkit",
    description: "In the code this is an instantiation of FileManagementToolkit(root_dir='workdir', selected_tools=['read_file','list_directory']). Modeled here as a Tool-like resource containing ReadFileTool and ListDirectoryTool.",
    schema: z.object({}),
  }
);



/**
 * Node: expandIdeaTask
 * Agent: senior_idea_analyst
 */
async function expandIdeaTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior Idea Analyst." +
        "\nNode: expandIdeaTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: refineIdeaTask
 * Agent: senior_strategist
 */
async function refineIdeaTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior Communications Strategist." +
        "\nNode: refineIdeaTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: chooseTemplateTask
 * Agent: senior_react_engineer
 */
async function chooseTemplateTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior React Engineer." +
        "\nNode: chooseTemplateTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: updatePageTask
 * Agent: senior_react_engineer
 */
async function updatePageTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior React Engineer." +
        "\nNode: updatePageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: componentContentTask
 * Agent: senior_content_editor
 */
async function componentContentTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior Content Editor." +
        "\nNode: componentContentTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: updateComponentTask
 * Agent: senior_content_editor
 */
async function updateComponentTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior Content Editor." +
        "\nNode: updateComponentTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: qaComponentTask
 * Agent: senior_content_editor
 */
async function qaComponentTask(state: typeof ExpandIdeaCrewteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Senior Content Editor." +
        "\nNode: qaComponentTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(ExpandIdeaCrewteamAnnotation)
  .addNode("expandIdeaTask", expandIdeaTask)
  .addNode("refineIdeaTask", refineIdeaTask)
  .addNode("chooseTemplateTask", chooseTemplateTask)
  .addNode("updatePageTask", updatePageTask)
  .addNode("componentContentTask", componentContentTask)
  .addNode("updateComponentTask", updateComponentTask)
  .addNode("qaComponentTask", qaComponentTask)
  .addEdge(START, "expandIdeaTask")
  .addEdge("refineIdeaTask", "refineIdeaTask")
  .addEdge("expandIdeaTask", END)
  .addEdge("chooseTemplateTask", END)
  .addEdge("updatePageTask", END)
  .addEdge("componentContentTask", END)
  .addEdge("updateComponentTask", END)
  .addEdge("qaComponentTask", END)
;

export const graph = workflow.compile();
graph.name = "ExpandIdeaCrewteam";
// Workflow: expand_idea_workflow_pattern
// Workflow: Expand Idea workflow pattern
// Workflow: choose_template_workflow_pattern
// Workflow: Choose Template workflow pattern
// Workflow: create_content_workflow_pattern
// Workflow: Create Content workflow pattern
// Workflow: landing_page_workflow_pattern
// Workflow: Landing page overall workflow
