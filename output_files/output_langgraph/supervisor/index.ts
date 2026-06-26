import { StateGraph, START, END } from "@langchain/langgraph";
import { SupervisorAnnotation, type SupervisorState } from "./types";
import { router } from "./nodes/router";
import { generalInput } from "./nodes/general-input";
import { ChatOpenAI } from "@langchain/openai";

async function stockbroker(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: stockbroker. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function tripPlanner(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: tripPlanner. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function openCode(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: openCode. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function orderPizza(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: orderPizza. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}
async function writerAgent(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    { role: "system", content: "Route: writerAgent. You are a supervisor." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

function handleRoute(state: SupervisorState):
  | "stockbroker"
  | "tripPlanner"
  | "openCode"
  | "orderPizza"
  | "generalInput"
  | "writerAgent"
{
  return state.next as
    | "stockbroker"
    | "tripPlanner"
    | "openCode"
    | "orderPizza"
    | "generalInput"
    | "writerAgent"
  ;
}

const builder = new StateGraph(SupervisorAnnotation)
  .addNode("router", router)
  .addNode("stockbroker", stockbroker)
  .addNode("tripPlanner", tripPlanner)
  .addNode("openCode", openCode)
  .addNode("orderPizza", orderPizza)
  .addNode("generalInput", generalInput)
  .addNode("writerAgent", writerAgent)
  .addConditionalEdges("router", handleRoute, [
    "stockbroker",
    "tripPlanner",
    "openCode",
    "orderPizza",
    "generalInput",
    "writerAgent",
  ])
  .addEdge(START, "router")
  .addEdge("stockbroker", END)
  .addEdge("tripPlanner", END)
  .addEdge("openCode", END)
  .addEdge("orderPizza", END)
  .addEdge("generalInput", END)
  .addEdge("writerAgent", END)
;

export const graph = builder.compile();
graph.name = "UnnamedProject";
