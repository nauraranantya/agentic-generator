import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const JobPostingCrewTeamAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: website_search_tool
const website_search_tool = tool(
  async () => {
    return "Result of website_search_tool";
  },
  {
    name: "website_search_tool",
    description: "Tool used for general website search queries (instantiated in the solution as a web search tool).",
    schema: z.object({}),
  }
);
// Tool: serper_dev_tool
const serper_dev_tool = tool(
  async () => {
    return "Result of serper_dev_tool";
  },
  {
    name: "serper_dev_tool",
    description: "Tool used for developer-oriented web search or SERP querying (instantiated as SerperDevTool in the code).",
    schema: z.object({}),
  }
);
// Tool: file_read_tool
const file_read_tool = tool(
  async () => {
    return "Result of file_read_tool";
  },
  {
    name: "file_read_tool",
    description: "Tool to read local files; configured to read job_description_example.md",
    schema: z.object({}),
  }
);



/**
 * Node: researchCompanyCultureTask
 * Agent: research_agent
 */
async function researchCompanyCultureTask(state: typeof JobPostingCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Research Analyst" +
        "\\nNode: researchCompanyCultureTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: researchRoleRequirementsTask
 * Agent: research_agent
 */
async function researchRoleRequirementsTask(state: typeof JobPostingCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Research Analyst" +
        "\\nNode: researchRoleRequirementsTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: draftJobPostingTask
 * Agent: writer_agent
 */
async function draftJobPostingTask(state: typeof JobPostingCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Job Description Writer" +
        "\\nNode: draftJobPostingTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: reviewAndEditJobPostingTask
 * Agent: review_agent
 */
async function reviewAndEditJobPostingTask(state: typeof JobPostingCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Review and Editing Specialist" +
        "\\nNode: reviewAndEditJobPostingTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: industryAnalysisTask
 * Agent: research_agent
 */
async function industryAnalysisTask(state: typeof JobPostingCrewTeamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Role: Research Analyst" +
        "\\nNode: industryAnalysisTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(JobPostingCrewTeamAnnotation)
  .addNode("researchCompanyCultureTask", researchCompanyCultureTask)
  .addNode("researchRoleRequirementsTask", researchRoleRequirementsTask)
  .addNode("draftJobPostingTask", draftJobPostingTask)
  .addNode("reviewAndEditJobPostingTask", reviewAndEditJobPostingTask)
  .addNode("industryAnalysisTask", industryAnalysisTask)
  .addEdge(START, "researchCompanyCultureTask")
  .addEdge("researchCompanyCultureTask", "researchRoleRequirementsTask")
  .addEdge("researchRoleRequirementsTask", "draftJobPostingTask")
  .addEdge("draftJobPostingTask", "reviewAndEditJobPostingTask")
  .addEdge("reviewAndEditJobPostingTask", "industryAnalysisTask")
  .addEdge("industryAnalysisTask", END)
;

export const graph = workflow.compile();
graph.name = "JobPostingCrewTeam";
// Workflow: job_posting_workflow
// Workflow: Job Posting Workflow Pattern
