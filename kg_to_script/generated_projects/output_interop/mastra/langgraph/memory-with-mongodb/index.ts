import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: openai_tool
const openai_tool = tool(
  async () => {
    return "Result of openai_tool";
  },
  {
    name: "openai_tool",
    description: "Representing the usage of the OpenAI SDK via openai(...) calls in the source code.",
    schema: z.object({}),
  }
);
// Tool: mongo_db_store
const mongo_db_store = tool(
  async () => {
    return "Result of mongo_db_store";
  },
  {
    name: "mongo_db_store",
    description: "Storage backend used by Memory.storage in code (MongoDBStore). The code uses process.env.MONGODB_URI and dbName.",
    schema: z.object({}),
  }
);
// Tool: mongo_db_vector
const mongo_db_vector = tool(
  async () => {
    return "Result of mongo_db_vector";
  },
  {
    name: "mongo_db_vector",
    description: "Vector store used for semantic recall via MongoDB-backed vectors (MongoDBVector).",
    schema: z.object({}),
  }
);



/**
 * Node: chefInitialRecipeSuggestionTask
 * Agent: chef_agent
 */
async function chefInitialRecipeSuggestionTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a chef." +
        "\nNode: chefInitialRecipeSuggestionTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: chefFriendSIngredientsRecipeSuggestionTask
 * Agent: chef_agent
 */
async function chefFriendSIngredientsRecipeSuggestionTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a chef." +
        "\nNode: chefFriendSIngredientsRecipeSuggestionTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: chefMemoryQueryTaskAsksWhatWasCookedEarlier
 * Agent: chef_agent
 */
async function chefMemoryQueryTaskAsksWhatWasCookedEarlier(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a chef." +
        "\nNode: chefMemoryQueryTaskAsksWhatWasCookedEarlier",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: chatInitialSystemMessageTask
 * Agent: memory_agent
 */
async function chatInitialSystemMessageTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a memory." +
        "\nNode: chatInitialSystemMessageTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: chatInteractiveLoopTask
 * Agent: memory_agent
 */
async function chatInteractiveLoopTask(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a memory." +
        "\nNode: chatInteractiveLoopTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("chefInitialRecipeSuggestionTask", chefInitialRecipeSuggestionTask)
  .addNode("chefFriendSIngredientsRecipeSuggestionTask", chefFriendSIngredientsRecipeSuggestionTask)
  .addNode("chefMemoryQueryTaskAsksWhatWasCookedEarlier", chefMemoryQueryTaskAsksWhatWasCookedEarlier)
  .addNode("chatInitialSystemMessageTask", chatInitialSystemMessageTask)
  .addNode("chatInteractiveLoopTask", chatInteractiveLoopTask)
  .addEdge(START, "chefInitialRecipeSuggestionTask")
  .addEdge("chefInitialRecipeSuggestionTask", "chefFriendSIngredientsRecipeSuggestionTask")
  .addEdge("chefFriendSIngredientsRecipeSuggestionTask", "chefMemoryQueryTaskAsksWhatWasCookedEarlier")
  .addEdge("chefMemoryQueryTaskAsksWhatWasCookedEarlier", "chatInitialSystemMessageTask")
  .addEdge("chatInitialSystemMessageTask", "chatInteractiveLoopTask")
  .addEdge("chatInteractiveLoopTask", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
