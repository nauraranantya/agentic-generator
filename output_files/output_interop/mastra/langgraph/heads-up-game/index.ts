import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraagenticsystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: lib_sql_store_tool
const lib_sql_store_tool = tool(
  async () => {
    return "Result of lib_sql_store_tool";
  },
  {
    name: "lib_sql_store_tool",
    description: "Persistent storage provider used by the Mastra system to store observability and memory state (file:../mastra.db).",
    schema: z.object({}),
  }
);
// Tool: lib_sql_vector_tool
const lib_sql_vector_tool = tool(
  async () => {
    return "Result of lib_sql_vector_tool";
  },
  {
    name: "lib_sql_vector_tool",
    description: "Vector store adapter used by agent Memory to store/retrieve embeddings.",
    schema: z.object({}),
  }
);



/**
 * Node: startTaskGenerateFamousPerson
 * Agent: famous_person_generator
 */
async function startTaskGenerateFamousPerson(state: typeof MastraagenticsystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions and constraints for generating a single famous person's name." +
        "\nNode: startTaskGenerateFamousPerson",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: aAndGuessHandling
 * Agent: game_agent
 */
async function aAndGuessHandling(state: typeof MastraagenticsystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions and required structured JSON output (response, gameWon)." +
        "\nNode: aAndGuessHandling",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: winTaskFinalization
 * Agent: famous_person_generator
 */
async function winTaskFinalization(state: typeof MastraagenticsystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions and constraints for generating a single famous person's name." +
        "\nNode: winTaskFinalization",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraagenticsystemAnnotation)
  .addNode("startTaskGenerateFamousPerson", startTaskGenerateFamousPerson)
  .addNode("aAndGuessHandling", aAndGuessHandling)
  .addNode("winTaskFinalization", winTaskFinalization)
  .addEdge(START, "startTaskGenerateFamousPerson")
  .addEdge("startTaskGenerateFamousPerson", "aAndGuessHandling")
  .addEdge("aAndGuessHandling", "winTaskFinalization")
  .addEdge("winTaskFinalization", END)
;

export const graph = workflow.compile();
graph.name = "Mastraagenticsystem";
// Workflow: heads_up_workflow
// Workflow: heads-up-workflow
