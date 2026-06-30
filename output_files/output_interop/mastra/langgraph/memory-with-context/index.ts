import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: taskInitialSystemMessage
 * Agent: memory_agent
 */
async function taskInitialSystemMessage(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code." +
        "\nNode: taskInitialSystemMessage",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskReceiveUserInput
 * Agent: memory_agent
 */
async function taskReceiveUserInput(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code." +
        "\nNode: taskReceiveUserInput",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAgentStreamResponse
 * Agent: memory_agent
 */
async function taskAgentStreamResponse(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "This prompt is supplied as the 'instructions' argument when creating the Agent instance in source code." +
        "\nNode: taskAgentStreamResponse",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskInitialSystemMessage", taskInitialSystemMessage)
  .addNode("taskReceiveUserInput", taskReceiveUserInput)
  .addNode("taskAgentStreamResponse", taskAgentStreamResponse)
  .addEdge(START, "taskInitialSystemMessage")
  .addEdge("taskInitialSystemMessage", "taskReceiveUserInput")
  .addEdge("taskReceiveUserInput", "taskAgentStreamResponse")
  .addEdge("taskAgentStreamResponse", "taskReceiveUserInput")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: workflow_chat_pattern
