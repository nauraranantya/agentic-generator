import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_plan
const tool_plan = tool(
  async () => {
    return "Result of tool_plan";
  },
  {
    name: "tool_plan",
    description: "Represents the logical tool 'plan' that is invoked by the planner node to expose executed/rejected/remaining plan lists as tool_call args.",
    schema: z.object({}),
  }
);
// Tool: tool_update_file
const tool_update_file = tool(
  async () => {
    return "Result of tool_update_file";
  },
  {
    name: "tool_update_file",
    description: "Tool invoked by executor to apply a code/file update. It accepts args { new_file_content, executed_plan_item } and returns a tool message used to indicate acceptance or rejection.",
    schema: z.object({}),
  }
);



/**
 * Node: plannerTaskProducePlanToolCall
 * Agent: open_code_agent_001
 */
async function plannerTaskProducePlanToolCall(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)." +
        "\nNode: plannerTaskProducePlanToolCall",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush
 * Agent: open_code_agent_001
 */
async function executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a planner-executor LLM agent (coordinates planning and performs file updates via tools and UI prompts)." +
        "\nNode: executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("plannerTaskProducePlanToolCall", plannerTaskProducePlanToolCall)
  .addNode("executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush", executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush)
  .addEdge(START, "plannerTaskProducePlanToolCall")
  .addEdge("plannerTaskProducePlanToolCall", "executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush")
  .addEdge("executorTaskApplyNextPlanItemViaUpdateFileToolCallAndUiPush", "plannerTaskProducePlanToolCall")
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
