import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastrasystemagentorchestratorAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: memory_storage_upstash_tool
const memory_storage_upstash_tool = tool(
  async () => {
    return "Result of memory_storage_upstash_tool";
  },
  {
    name: "memory_storage_upstash_tool",
    description: "Represents the Upstash HTTP-backed storage used by the memory implementation.",
    schema: z.object({}),
  }
);
// Tool: memory_vector_pg_tool
const memory_vector_pg_tool = tool(
  async () => {
    return "Result of memory_vector_pg_tool";
  },
  {
    name: "memory_vector_pg_tool",
    description: "A tool",
    schema: z.object({}),
  }
);
// Tool: open_ai_sdk_tool
const open_ai_sdk_tool = tool(
  async () => {
    return "Result of open_ai_sdk_tool";
  },
  {
    name: "open_ai_sdk_tool",
    description: "Conceptual representation of the OpenAI client used to call gpt-4o. SDK details are not modeled; configuration captured as literals.",
    schema: z.object({}),
  }
);



/**
 * Node: setUpSessionAndThread
 * Agent: memory_agent
 */
async function setUpSessionAndThread(state: typeof MastrasystemagentorchestratorAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instructions for Memory Agent; used as persistent agent prompt." +
        "\\nNode: setUpSessionAndThread",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: suggestRecipesFromUserSListedIngredients
 * Agent: chef_agent
 */
async function suggestRecipesFromUserSListedIngredients(state: typeof MastrasystemagentorchestratorAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instructions for Chef Agent; used as persistent agent prompt." +
        "\\nNode: suggestRecipesFromUserSListedIngredients",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: suggestRecipesFromFriendSIngredients
 * Agent: chef_agent
 */
async function suggestRecipesFromFriendSIngredients(state: typeof MastrasystemagentorchestratorAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instructions for Chef Agent; used as persistent agent prompt." +
        "\\nNode: suggestRecipesFromFriendSIngredients",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: recallWhatWasCookedPreviously
 * Agent: chef_agent
 */
async function recallWhatWasCookedPreviously(state: typeof MastrasystemagentorchestratorAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level instructions for Chef Agent; used as persistent agent prompt." +
        "\\nNode: recallWhatWasCookedPreviously",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastrasystemagentorchestratorAnnotation)
  .addNode("setUpSessionAndThread", setUpSessionAndThread)
  .addNode("suggestRecipesFromUserSListedIngredients", suggestRecipesFromUserSListedIngredients)
  .addNode("suggestRecipesFromFriendSIngredients", suggestRecipesFromFriendSIngredients)
  .addNode("recallWhatWasCookedPreviously", recallWhatWasCookedPreviously)
  .addEdge(START, "setUpSessionAndThread")
  .addEdge("setUpSessionAndThread", "suggestRecipesFromUserSListedIngredients")
  .addEdge("suggestRecipesFromUserSListedIngredients", "suggestRecipesFromFriendSIngredients")
  .addEdge("suggestRecipesFromFriendSIngredients", "recallWhatWasCookedPreviously")
  .addEdge("recallWhatWasCookedPreviously", END)
;

export const graph = workflow.compile();
graph.name = "Mastrasystemagentorchestrator";
// Workflow: mastra_conversation_pattern
// Workflow: Mastra conversational flow (example run)
