import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

async function workflowStepPlanner(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)." +
        "\\nNode: workflowStepPlanner",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function workflowStepExecutor(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)." +
        "\\nNode: workflowStepExecutor",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("workflowStepPlanner", workflowStepPlanner)
  .addNode("workflowStepExecutor", workflowStepExecutor)
  .addEdge(START, "workflowStepPlanner")
  .addEdge("workflowStepPlanner", "workflowStepExecutor")
  .addEdge("workflowStepExecutor", "workflowStepPlanner")
  .addEdge("workflowStepExecutor", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
