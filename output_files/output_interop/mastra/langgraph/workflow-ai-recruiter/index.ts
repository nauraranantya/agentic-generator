import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: gatherCandidateInfo
 * Agent: recruiter_agent
 */
async function gatherCandidateInfo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level static instruction used as the recruiter's persona/instruction set for generation." +
        "\nNode: gatherCandidateInfo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: askAboutSpecialty
 * Agent: recruiter_agent
 */
async function askAboutSpecialty(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level static instruction used as the recruiter's persona/instruction set for generation." +
        "\nNode: askAboutSpecialty",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: askAboutRole
 * Agent: recruiter_agent
 */
async function askAboutRole(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level static instruction used as the recruiter's persona/instruction set for generation." +
        "\nNode: askAboutRole",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("gatherCandidateInfo", gatherCandidateInfo)
  .addNode("askAboutSpecialty", askAboutSpecialty)
  .addNode("askAboutRole", askAboutRole)
  .addEdge(START, "gatherCandidateInfo")
  .addEdge("gatherCandidateInfo", "askAboutSpecialty")
  .addEdge("gatherCandidateInfo", "askAboutRole")
  .addEdge("askAboutSpecialty", END)
  .addEdge("askAboutRole", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: candidate_workflow
// Workflow: candidate-workflow
