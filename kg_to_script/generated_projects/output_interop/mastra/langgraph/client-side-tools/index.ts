import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const ClientApplicationViteReactTeamAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_change_color
const tool_change_color = tool(
  async () => {
    return "Result of tool_change_color";
  },
  {
    name: "tool_change_color",
    description: "Client-side tool that changes the application background color. Declared in clientSideToolCallsMap in src/App.tsx.",
    schema: z.object({}),
  }
);
// Tool: tool_change_logo_size
const tool_change_logo_size = tool(
  async () => {
    return "Result of tool_change_logo_size";
  },
  {
    name: "tool_change_logo_size",
    description: "Client-side tool that changes the size of the logo. Declared in clientSideToolCallsMap in src/App.tsx.",
    schema: z.object({}),
  }
);
// Tool: tool_add_post
const tool_add_post = tool(
  async () => {
    return "Result of tool_add_post";
  },
  {
    name: "tool_add_post",
    description: "Client-side tool that adds a new post to the 'posts' state array. Declared in clientSideToolCallsMap in src/App.tsx.",
    schema: z.object({}),
  }
);



/**
 * Node: userSubmitsMessage
 * Agent: agent
 */
async function userSubmitsMessage(state: typeof ClientApplicationViteReactTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts)." +
        "\nNode: userSubmitsMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: streamMessageToAgent
 * Agent: agent
 */
async function streamMessageToAgent(state: typeof ClientApplicationViteReactTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts)." +
        "\nNode: streamMessageToAgent",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: processStreamedEventsToolCallsToolResultsDeltasTextParts
 * Agent: agent
 */
async function processStreamedEventsToolCallsToolResultsDeltasTextParts(state: typeof ClientApplicationViteReactTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts)." +
        "\nNode: processStreamedEventsToolCallsToolResultsDeltasTextParts",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: executeAddPostTool
 * Agent: agent
 */
async function executeAddPostTool(state: typeof ClientApplicationViteReactTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts)." +
        "\nNode: executeAddPostTool",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: appendTextPartsToTheResponseTextState
 * Agent: agent
 */
async function appendTextPartsToTheResponseTextState(state: typeof ClientApplicationViteReactTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System/instruction prompt provided to the agent in mastra configuration (src/mastra/agents/index.ts)." +
        "\nNode: appendTextPartsToTheResponseTextState",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(ClientApplicationViteReactTeamAnnotation)
  .addNode("userSubmitsMessage", userSubmitsMessage)
  .addNode("streamMessageToAgent", streamMessageToAgent)
  .addNode("processStreamedEventsToolCallsToolResultsDeltasTextParts", processStreamedEventsToolCallsToolResultsDeltasTextParts)
  .addNode("executeAddPostTool", executeAddPostTool)
  .addNode("appendTextPartsToTheResponseTextState", appendTextPartsToTheResponseTextState)
  .addEdge(START, "userSubmitsMessage")
  .addEdge("userSubmitsMessage", "streamMessageToAgent")
  .addEdge("streamMessageToAgent", "processStreamedEventsToolCallsToolResultsDeltasTextParts")
  .addEdge("processStreamedEventsToolCallsToolResultsDeltasTextParts", "executeAddPostTool")
  .addEdge("executeAddPostTool", "appendTextPartsToTheResponseTextState")
;

export const graph = workflow.compile();
graph.name = "ClientApplicationViteReactTeam";
// Workflow: streaming_workflow
// Workflow: Streaming interaction workflow
