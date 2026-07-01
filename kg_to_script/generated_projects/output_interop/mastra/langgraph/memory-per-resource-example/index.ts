import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: taskStartConversation
 * Agent: personal_assistant
 */
async function taskStartConversation(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions configured at creation time (Agent.instructions in source code)." +
        "\nNode: taskStartConversation",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskUpdateMemory
 * Agent: personal_assistant
 */
async function taskUpdateMemory(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions configured at creation time (Agent.instructions in source code)." +
        "\nNode: taskUpdateMemory",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskInteractiveChat
 * Agent: personal_assistant
 */
async function taskInteractiveChat(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent instructions configured at creation time (Agent.instructions in source code)." +
        "\nNode: taskInteractiveChat",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskStartConversation", taskStartConversation)
  .addNode("taskUpdateMemory", taskUpdateMemory)
  .addNode("taskInteractiveChat", taskInteractiveChat)
  .addEdge(START, "taskStartConversation")
  .addEdge("taskStartConversation", "taskUpdateMemory")
  .addEdge("taskUpdateMemory", "taskInteractiveChat")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: per_resource_working_memory_pattern
// Workflow: Per-Resource Working Memory Pattern
