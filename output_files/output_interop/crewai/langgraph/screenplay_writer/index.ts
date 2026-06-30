import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const AICrewforscreenwritingAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: task1Analysis
 * Agent: analyst
 */
async function task1Analysis(state: typeof AICrewforscreenwritingAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "role: analyse; goal: Distill arguments and identify who said what; backstory: Expert discussion analyst." +
        "\nNode: task1Analysis",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: task2Scriptwriting
 * Agent: scriptwriter
 */
async function task2Scriptwriting(state: typeof AICrewforscreenwritingAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "role: scriptwriter; goal: Produce dialogue-only screenplay; backstory: hates directional notes" +
        "\nNode: task2Scriptwriting",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: task3Formatting
 * Agent: formatter
 */
async function task3Formatting(state: typeof AICrewforscreenwritingAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "role: formatter; goal: Format text and remove bracketed actions; backstory: expert text formatter." +
        "\nNode: task3Formatting",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(AICrewforscreenwritingAnnotation)
  .addNode("task1Analysis", task1Analysis)
  .addNode("task2Scriptwriting", task2Scriptwriting)
  .addNode("task3Formatting", task3Formatting)
  .addEdge(START, "task1Analysis")
  .addEdge("task1Analysis", "task2Scriptwriting")
  .addEdge("task2Scriptwriting", "task3Formatting")
  .addEdge("task3Formatting", END)
;

export const graph = workflow.compile();
graph.name = "AICrewforscreenwriting";
// Workflow: workflow_pattern_screenplay
// Workflow: screenplay_creation_sequential
