import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: mcp_client
const mcp_client = tool(
  async () => {
    return "Result of mcp_client";
  },
  {
    name: "mcp_client",
    description: "Client used by the Mastra configuration to enumerate available MCP tool endpoints. In the source it is an MCPClient instance with server configuration; provides a listTools() capability.",
    schema: z.object({}),
  }
);
// Tool: mcp_registry_tool
const mcp_registry_tool = tool(
  async () => {
    return "Result of mcp_registry_tool";
  },
  {
    name: "mcp_registry_tool",
    description: "Tool instance representing the MCP registry server process launched via the configured command. In the source the agent's tools are populated by await mcp.listTools(); the registry server is configured to run as a node process and communicate over stdio (path: ../../packages/mcp-registry-registry/dist/stdio.js).",
    schema: z.object({}),
  }
);



/**
 * Node: initializeAgentTask
 * Agent: mcp_registry_agent
 */
async function initializeAgentTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent bootstrap prompt / instruction used to guide agent behavior independent of a specific task." +
        "\\nNode: initializeAgentTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: searchMcpRegistriesTask
 * Agent: mcp_registry_agent
 */
async function searchMcpRegistriesTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent bootstrap prompt / instruction used to guide agent behavior independent of a specific task." +
        "\\nNode: searchMcpRegistriesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: finalizeTask
 * Agent: mcp_registry_agent
 */
async function finalizeTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent bootstrap prompt / instruction used to guide agent behavior independent of a specific task." +
        "\\nNode: finalizeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("initializeAgentTask", initializeAgentTask)
  .addNode("searchMcpRegistriesTask", searchMcpRegistriesTask)
  .addNode("finalizeTask", finalizeTask)
  .addEdge(START, "initializeAgentTask")
  .addEdge("initializeAgentTask", "searchMcpRegistriesTask")
  .addEdge("searchMcpRegistriesTask", "finalizeTask")
  .addEdge("finalizeTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: mastra_simple_workflow
