import { ChatOpenAI } from "@langchain/openai";
import type { SupervisorState } from "../types";

export async function generalInput(state: SupervisorState) {
  const model = new ChatOpenAI({ model: "gpt-4o" });
  const response = await model.invoke([
    {
      role: "system",
      content: "General assistant route. You are a assistant / trip-planner.",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}
