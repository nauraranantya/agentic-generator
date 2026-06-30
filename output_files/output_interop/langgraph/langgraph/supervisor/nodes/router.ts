import type { SupervisorState } from "../types";

const ROUTES = ["stockbrokerTask", "tripPlannerTask", "openCodeTask", "orderPizzaTask", "generalInputTask", "writerAgentTask"];
const FALLBACK = "generalInputTask";

export async function router(state: SupervisorState) {
  const last = state.messages?.[state.messages.length - 1];
  const text = String(last?.content ?? "").toLowerCase();

  for (const route of ROUTES) {
    if (text.includes(route.toLowerCase())) {
      return { next: route };
    }
  }

  return { next: FALLBACK };
}
