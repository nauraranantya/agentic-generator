import { ChatAnthropic } from "@langchain/anthropic";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_pizza_finder
const tool_pizza_finder = tool(
  async () => {
    return "Result of tool_pizza_finder";
  },
  {
    name: "tool_pizza_finder",
    description: "Represents the external lookup mechanism that returns store contact information. In code this is emulated by constructing a ToolMessage with found shop details.",
    schema: z.object({}),
  }
);
// Tool: tool_pizza_ordering_system
const tool_pizza_ordering_system = tool(
  async () => {
    return "Result of tool_pizza_ordering_system";
  },
  {
    name: "tool_pizza_ordering_system",
    description: "Represents the external ordering mechanism that places the pizza order and returns confirmation. In code this is emulated by constructing a ToolMessage 'Pizza order successfully placed.'.",
    schema: z.object({}),
  }
);



/**
 * Node: findPizzaShopTask
 * Agent: pizza_orderer_v1
 */
async function findPizzaShopTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "General system role description used by both nodes as the system message." +
        "\nNode: findPizzaShopTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: placePizzaOrderTask
 * Agent: pizza_orderer_v1
 */
async function placePizzaOrderTask(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatAnthropic({ model: "claude-3-5-sonnet-latest" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "General system role description used by both nodes as the system message." +
        "\nNode: placePizzaOrderTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("findPizzaShopTask", findPizzaShopTask)
  .addNode("placePizzaOrderTask", placePizzaOrderTask)
  .addEdge(START, "findPizzaShopTask")
  .addEdge("findPizzaShopTask", "placePizzaOrderTask")
  .addEdge("placePizzaOrderTask", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
