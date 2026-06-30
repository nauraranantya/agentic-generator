import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const RecruitmentCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_serperdev
const tool_serperdev = tool(
  async () => {
    return "Result of tool_serperdev";
  },
  {
    name: "tool_serperdev",
    description: "Search / knowledge tool (SerperDev) used by agents for web search or knowledge lookups.",
    schema: z.object({}),
  }
);
// Tool: tool_scrapewebsite
const tool_scrapewebsite = tool(
  async () => {
    return "Result of tool_scrapewebsite";
  },
  {
    name: "tool_scrapewebsite",
    description: "General web scraping tool used to extract structured information from web pages.",
    schema: z.object({}),
  }
);
// Tool: tool_linkedin
const tool_linkedin = tool(
  async () => {
    return "Result of tool_linkedin";
  },
  {
    name: "tool_linkedin",
    description: "Retrieve LinkedIn profiles given a list of skills. Input is a comma-separated list of skills. Returns candidate name, position, location, and profile link. Implemented via a web client that navigates LinkedIn search and extracts entries (requires a LinkedIn session cookie in environment).",
    schema: z.object({}),
  }
);



/**
 * Node: researchCandidatesTask
 * Agent: researcher
 */
async function researchCandidatesTask(state: typeof RecruitmentCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level base instruction for researcher." +
        "\\nNode: researchCandidatesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: matchAndScoreCandidatesTask
 * Agent: matcher
 */
async function matchAndScoreCandidatesTask(state: typeof RecruitmentCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level base instruction for matcher." +
        "\\nNode: matchAndScoreCandidatesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: outreachStrategyTask
 * Agent: communicator
 */
async function outreachStrategyTask(state: typeof RecruitmentCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level base instruction for communicator." +
        "\\nNode: outreachStrategyTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: reportCandidatesTask
 * Agent: reporter
 */
async function reportCandidatesTask(state: typeof RecruitmentCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent-level base instruction for reporter." +
        "\\nNode: reportCandidatesTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(RecruitmentCrewAnnotation)
  .addNode("researchCandidatesTask", researchCandidatesTask)
  .addNode("matchAndScoreCandidatesTask", matchAndScoreCandidatesTask)
  .addNode("outreachStrategyTask", outreachStrategyTask)
  .addNode("reportCandidatesTask", reportCandidatesTask)
  .addEdge(START, "researchCandidatesTask")
  .addEdge("researchCandidatesTask", "matchAndScoreCandidatesTask")
  .addEdge("matchAndScoreCandidatesTask", "outreachStrategyTask")
  .addEdge("outreachStrategyTask", "reportCandidatesTask")
  .addEdge("reportCandidatesTask", END)
;

export const graph = workflow.compile();
graph.name = "RecruitmentCrew";
// Workflow: recruitment_workflow
// Workflow: Recruitment workflow pattern
