import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MeetingPreparationCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: exa_search_tool
const exa_search_tool = tool(
  async () => {
    return "Result of exa_search_tool";
  },
  {
    name: "exa_search_tool",
    description: "Tool wrapping Exa (exa_py) search capabilities used by agents.
Provides three main operations: search(query), find_similar(url), and get_contents(ids).
The tool requires an EXA_API_KEY configuration value to access Exa APIs.",
    schema: z.object({}),
  }
);



/**
 * Node: researchTask
 * Agent: researcher_agent_1
 */
async function researchTask(state: typeof MeetingPreparationCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Research Specialist; Goal: Conduct thorough research on people and companies involved in the meeting" +
        "\nNode: researchTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: industryAnalysisTask
 * Agent: industry_analyst_agent_1
 */
async function industryAnalysisTask(state: typeof MeetingPreparationCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Industry Analyst; Goal: Analyze industry trends and opportunities" +
        "\nNode: industryAnalysisTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: meetingStrategyTask
 * Agent: meeting_strategy_agent_1
 */
async function meetingStrategyTask(state: typeof MeetingPreparationCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Meeting Strategy Advisor; Goal: Develop talking points and strategies" +
        "\nNode: meetingStrategyTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: summaryAndBriefingTask
 * Agent: briefing_coordinator_agent_1
 */
async function summaryAndBriefingTask(state: typeof MeetingPreparationCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Briefing Coordinator; Goal: Compile information into briefing document" +
        "\nNode: summaryAndBriefingTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MeetingPreparationCrewAnnotation)
  .addNode("researchTask", researchTask)
  .addNode("industryAnalysisTask", industryAnalysisTask)
  .addNode("meetingStrategyTask", meetingStrategyTask)
  .addNode("summaryAndBriefingTask", summaryAndBriefingTask)
  .addEdge(START, "researchTask")
  .addEdge("researchTask", "industryAnalysisTask")
  .addEdge("industryAnalysisTask", "meetingStrategyTask")
  .addEdge("meetingStrategyTask", "summaryAndBriefingTask")
  .addEdge("summaryAndBriefingTask", END)
;

export const graph = workflow.compile();
graph.name = "MeetingPreparationCrew";
// Workflow: meeting_preparation_pattern
// Workflow: Meeting Preparation Workflow Pattern
