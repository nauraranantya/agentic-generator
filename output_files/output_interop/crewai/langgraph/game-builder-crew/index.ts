import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const GameBuilderCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: codeTask
 * Agent: senior_engineer_agent
 */
async function codeTask(state: typeof GameBuilderCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Senior Software Engineer" +
        "\nNode: codeTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: reviewTask
 * Agent: qa_engineer_agent
 */
async function reviewTask(state: typeof GameBuilderCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Software Quality Control Engineer" +
        "\nNode: reviewTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: evaluateTask
 * Agent: chief_qa_engineer_agent
 */
async function evaluateTask(state: typeof GameBuilderCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Chief Software Quality Control Engineer" +
        "\nNode: evaluateTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(GameBuilderCrewAnnotation)
  .addNode("codeTask", codeTask)
  .addNode("reviewTask", reviewTask)
  .addNode("evaluateTask", evaluateTask)
  .addEdge(START, "codeTask")
  .addEdge("codeTask", "reviewTask")
  .addEdge("reviewTask", "evaluateTask")
  .addEdge("evaluateTask", END)
;

export const graph = workflow.compile();
graph.name = "GameBuilderCrew";
// Workflow: game_builder_workflow
// Workflow: Game Builder Sequential Workflow
