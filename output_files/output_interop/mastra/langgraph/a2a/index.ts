import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: researchTask
 * Agent: my_agent
 */
async function researchTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: researchTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: contentTask
 * Agent: content_creator_agent
 */
async function contentTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\nNode: contentTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("researchTask", researchTask)
  .addNode("contentTask", contentTask)
  .addEdge(START, "researchTask")
  .addEdge("researchTask", "contentTask")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: a2_a_example_pattern
