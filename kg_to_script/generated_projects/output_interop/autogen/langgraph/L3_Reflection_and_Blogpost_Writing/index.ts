import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: taskWriteBlog
 * Agent: unnamed
 */
async function taskWriteBlog(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Writer." +
        "\nNode: taskWriteBlog",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCriticInitiate1
 * Agent: unnamed
 */
async function taskCriticInitiate1(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Critic." +
        "\nNode: taskCriticInitiate1",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskNestedSeoReview
 * Agent: unnamed
 */
async function taskNestedSeoReview(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a SEO Reviewer." +
        "\nNode: taskNestedSeoReview",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskNestedLegalReview
 * Agent: unnamed
 */
async function taskNestedLegalReview(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Legal Reviewer." +
        "\nNode: taskNestedLegalReview",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskNestedEthicsReview
 * Agent: unnamed
 */
async function taskNestedEthicsReview(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Ethics Reviewer." +
        "\nNode: taskNestedEthicsReview",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskMetaAggregate
 * Agent: unnamed
 */
async function taskMetaAggregate(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Meta Reviewer." +
        "\nNode: taskMetaAggregate",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCriticInitiate2
 * Agent: unnamed
 */
async function taskCriticInitiate2(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Critic." +
        "\nNode: taskCriticInitiate2",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskWriteBlog", taskWriteBlog)
  .addNode("taskCriticInitiate1", taskCriticInitiate1)
  .addNode("taskNestedSeoReview", taskNestedSeoReview)
  .addNode("taskNestedLegalReview", taskNestedLegalReview)
  .addNode("taskNestedEthicsReview", taskNestedEthicsReview)
  .addNode("taskMetaAggregate", taskMetaAggregate)
  .addNode("taskCriticInitiate2", taskCriticInitiate2)
  .addEdge(START, "taskWriteBlog")
  .addEdge("taskWriteBlog", "taskCriticInitiate1")
  .addEdge("taskCriticInitiate1", "taskNestedSeoReview")
  .addEdge("taskNestedSeoReview", "taskNestedLegalReview")
  .addEdge("taskNestedLegalReview", "taskNestedEthicsReview")
  .addEdge("taskNestedEthicsReview", "taskMetaAggregate")
  .addEdge("taskMetaAggregate", "taskCriticInitiate2")
  .addEdge("taskCriticInitiate2", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: pattern_nested
