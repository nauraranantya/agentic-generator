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

// Tool: duck_duck_go_tool
const duck_duck_go_tool = tool(
  async () => {
    return "Result of duck_duck_go_tool";
  },
  {
    name: "duck_duck_go_tool",
    description: "An instance of DuckDuckGoSearchRun created in main.py and intended for web search functionality. (Note: installed via 'duckduckgo-search' if used.)",
    schema: z.object({}),
  }
);



/**
 * Node: task1
 * Agent: agent_1_name
 */
async function task1(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)" +
        "\\nNode: task1",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: task2
 * Agent: agent_2_name
 */
async function task2(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "agent settings: allow_delegation=False; verbose=True; llm=ChatOpenAI(gpt-3.5-turbo)" +
        "\\nNode: task2",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("task1", task1)
  .addNode("task2", task2)
  .addEdge(START, "task1")
  .addEdge("task1", "task2")
  .addEdge("task2", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: custom_crew_workflow
