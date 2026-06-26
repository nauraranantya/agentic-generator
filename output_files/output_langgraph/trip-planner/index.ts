import { StateGraph, START, END } from "@langchain/langgraph";
import { SupervisorAnnotation, type SupervisorState } from "./types";
import { router } from "./nodes/router";
import { generalInput } from "./nodes/general-input";
import { ChatOpenAI } from "@langchain/openai";

async function stepCallTools(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    { role: "system", content: "Route: stepCallTools. You are a assistant / trip-planner." },
    ...state.messages,
  ]);
  return { messages: [response] };
}

function handleRoute(state: SupervisorState):
  | "stepCallTools"
{
  return state.next as
    | "stepCallTools"
  ;
}

const builder = new StateGraph(SupervisorAnnotation)
  .addNode("stepExtraction", router)
  .addNode("stepCallTools", stepCallTools)
  .addConditionalEdges("stepExtraction", handleRoute, [
    "stepCallTools",
  ])
  .addEdge(START, "stepExtraction")
  .addEdge("stepCallTools", END)
;

export const graph = builder.compile();
graph.name = "UnnamedProject";
