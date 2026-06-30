import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";

const UnnamedProjectAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});




/**
 * Node: taskCollectPersonalInfo
 * Agent: onboarding_personal_information_agent
 */
async function taskCollectPersonalInfo(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a personal_information_collector." +
        "\nNode: taskCollectPersonalInfo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCollectTopicPreferences
 * Agent: onboarding_personal_information_agent
 */
async function taskCollectTopicPreferences(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a personal_information_collector." +
        "\nNode: taskCollectTopicPreferences",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskCustomerProxyToEngagement
 * Agent: onboarding_personal_information_agent
 */
async function taskCustomerProxyToEngagement(state: typeof UnnamedProjectAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-3.5-turbo" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a personal_information_collector." +
        "\nNode: taskCustomerProxyToEngagement",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(UnnamedProjectAnnotation)
  .addNode("taskCollectPersonalInfo", taskCollectPersonalInfo)
  .addNode("taskCollectTopicPreferences", taskCollectTopicPreferences)
  .addNode("taskCustomerProxyToEngagement", taskCustomerProxyToEngagement)
  .addEdge(START, "taskCollectPersonalInfo")
  .addEdge("taskCollectPersonalInfo", "taskCollectTopicPreferences")
  .addEdge("taskCollectTopicPreferences", "taskCustomerProxyToEngagement")
  .addEdge("taskCustomerProxyToEngagement", END)
;

export const graph = workflow.compile();
graph.name = "UnnamedProject";
// Workflow: customer_onboarding_workflow
