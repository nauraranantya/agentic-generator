import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: blogpostGenerationTask
 * Agent: writer_1
 */
async function blogpostGenerationTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Writer." +
        "\nNode: blogpostGenerationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: ethicsReviewTask
 * Agent: ethics_reviewer_1
 */
async function ethicsReviewTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Ethics Reviewer." +
        "\nNode: ethicsReviewTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: metaAggregationTask
 * Agent: meta_reviewer_1
 */
async function metaAggregationTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Meta Reviewer." +
        "\nNode: metaAggregationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: blogpostGenerationTask
 * Agent: writer_1
 */
async function blogpostGenerationTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Writer." +
        "\nNode: blogpostGenerationTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("blogpostGenerationTask", blogpostGenerationTask)
  .addNode("ethicsReviewTask", ethicsReviewTask)
  .addNode("metaAggregationTask", metaAggregationTask)
  .addNode("blogpostGenerationTask", blogpostGenerationTask)
  .addEdge(START, "blogpostGenerationTask")
  .addEdge("blogpostGenerationTask", "ethicsReviewTask")
  .addEdge("ethicsReviewTask", "metaAggregationTask")
  .addEdge("metaAggregationTask", "blogpostGenerationTask")
  .addEdge("blogpostGenerationTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: workflow_reflection_blogpost
// Workflow: Reflection and Blogpost Writing Workflow Pattern
