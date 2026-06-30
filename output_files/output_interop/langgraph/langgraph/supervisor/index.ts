import { StateGraph, START, END } from "@langchain/langgraph";
import { SupervisorAnnotation, type SupervisorState } from "./types";
import { router } from "./nodes/router";
import { generalInput } from "./nodes/general-input";
import { ChatOpenAI } from "@langchain/openai";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

// Tool: tool_stockbroker
const tool_stockbroker = tool(
  async () => {
    return "Result of tool_stockbroker";
  },
  {
    name: "tool_stockbroker",
    description: "Can fetch the price of a ticker, purchase/sell a ticker, or get the user's portfolio.",
    schema: z.object({}),
  }
);
// Tool: tool_trip_planner
const tool_trip_planner = tool(
  async () => {
    return "Result of tool_trip_planner";
  },
  {
    name: "tool_trip_planner",
    description: "Helps the user plan their trip. It can suggest restaurants and places to stay in any given location.",
    schema: z.object({}),
  }
);
// Tool: tool_open_code
const tool_open_code = tool(
  async () => {
    return "Result of tool_open_code";
  },
  {
    name: "tool_open_code",
    description: "Can write a React TODO app for the user. Only call this tool if the user requests a TODO app.",
    schema: z.object({}),
  }
);
// Tool: tool_order_pizza
const tool_order_pizza = tool(
  async () => {
    return "Result of tool_order_pizza";
  },
  {
    name: "tool_order_pizza",
    description: "Can order a pizza for the user.",
    schema: z.object({}),
  }
);
// Tool: tool_writer_agent
const tool_writer_agent = tool(
  async () => {
    return "Result of tool_writer_agent";
  },
  {
    name: "tool_writer_agent",
    description: "Can write a text document for the user. Only call this tool if they request a text document.",
    schema: z.object({}),
  }
);
// Tool: tool_router
const tool_router = tool(
  async () => {
    return "Result of tool_router";
  },
  {
    name: "tool_router",
    description: "A tool used by the router node to select which tool should handle the user's query (routes: stockbroker, tripPlanner, openCode, orderPizza, generalInput, writerAgent).",
    schema: z.object({}),
  }
);
// Tool: tool_general_input
const tool_general_input = tool(
  async () => {
    return "Result of tool_general_input";
  },
  {
    name: "tool_general_input",
    description: "Tool/node that responds to general user inputs and summarizes or follows up on tool results.",
    schema: z.object({}),
  }
);


/**
 * Route Target Node: stockbrokerTask
 * Agent: generative_ui_supervisor
 */
async function stockbrokerTask(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: stockbrokerTask. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Route Target Node: tripPlannerTask
 * Agent: generative_ui_supervisor
 */
async function tripPlannerTask(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: tripPlannerTask. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Route Target Node: openCodeTask
 * Agent: generative_ui_supervisor
 */
async function openCodeTask(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: openCodeTask. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Route Target Node: orderPizzaTask
 * Agent: generative_ui_supervisor
 */
async function orderPizzaTask(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: orderPizzaTask. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Route Target Node: writerAgentTask
 * Agent: generative_ui_supervisor
 */
async function writerAgentTask(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: writerAgentTask. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

function handleRoute(state: SupervisorState):
  | "stockbrokerTask"
  | "tripPlannerTask"
  | "openCodeTask"
  | "orderPizzaTask"
  | "generalInputTask"
  | "writerAgentTask"
{
  return state.next as
    | "stockbrokerTask"
    | "tripPlannerTask"
    | "openCodeTask"
    | "orderPizzaTask"
    | "generalInputTask"
    | "writerAgentTask"
  ;
}

const builder = new StateGraph(SupervisorAnnotation)
  .addNode("routerTask", router)
  .addNode("stockbrokerTask", stockbrokerTask)
  .addNode("tripPlannerTask", tripPlannerTask)
  .addNode("openCodeTask", openCodeTask)
  .addNode("orderPizzaTask", orderPizzaTask)
  .addNode("generalInputTask", generalInput)
  .addNode("writerAgentTask", writerAgentTask)
  .addConditionalEdges("routerTask", handleRoute, [
    "stockbrokerTask",
    "tripPlannerTask",
    "openCodeTask",
    "orderPizzaTask",
    "generalInputTask",
    "writerAgentTask",
  ])
  .addEdge(START, "routerTask")
  .addEdge("stockbrokerTask", END)
  .addEdge("tripPlannerTask", END)
  .addEdge("openCodeTask", END)
  .addEdge("orderPizzaTask", END)
  .addEdge("generalInputTask", END)
  .addEdge("writerAgentTask", END)
;

export const graph = builder.compile();
graph.name = "UnnamedProject";
// Workflow: generative_ui_workflow
// Workflow: Generative UI Agent Workflow
