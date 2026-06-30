import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const BlogCrewIndustryspecializedagentsexampleAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: weaviate_vector_search_tool
const weaviate_vector_search_tool = tool(
  async () => {
    return "Result of weaviate_vector_search_tool";
  },
  {
    name: "weaviate_vector_search_tool",
    description: "Vector search tool configured to query a Weaviate collection (WeaviateBlogChunk).",
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
    description: "Web search tool (SerperDev) used to retrieve web search results for background research.",
    schema: z.object({}),
  }
);



/**
 * Node: biomedicalAgentTaskResearchAWeaviateFeature
 * Agent: biomed_agent_1
 */
async function biomedicalAgentTaskResearchAWeaviateFeature(state: typeof BlogCrewIndustryspecializedagentsexampleAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Industry researcher focused on biomedical trends and their applications in AI." +
        "\nNode: biomedicalAgentTaskResearchAWeaviateFeature",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: healthcareAgentTaskResearchAWeaviateFeature
 * Agent: healthcare_agent_1
 */
async function healthcareAgentTaskResearchAWeaviateFeature(state: typeof BlogCrewIndustryspecializedagentsexampleAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.." +
        "\nNode: healthcareAgentTaskResearchAWeaviateFeature",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: financialAgentTaskResearchAWeaviateFeature
 * Agent: financial_agent_1
 */
async function financialAgentTaskResearchAWeaviateFeature(state: typeof BlogCrewIndustryspecializedagentsexampleAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a Insight analyst exploring innovations in finance, wealth tech, and regulatory tech." +
        "\nNode: financialAgentTaskResearchAWeaviateFeature",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(BlogCrewIndustryspecializedagentsexampleAnnotation)
  .addNode("biomedicalAgentTaskResearchAWeaviateFeature", biomedicalAgentTaskResearchAWeaviateFeature)
  .addNode("healthcareAgentTaskResearchAWeaviateFeature", healthcareAgentTaskResearchAWeaviateFeature)
  .addNode("financialAgentTaskResearchAWeaviateFeature", financialAgentTaskResearchAWeaviateFeature)
  .addEdge(START, "biomedicalAgentTaskResearchAWeaviateFeature")
  .addEdge("biomedicalAgentTaskResearchAWeaviateFeature", "healthcareAgentTaskResearchAWeaviateFeature")
  .addEdge("healthcareAgentTaskResearchAWeaviateFeature", "financialAgentTaskResearchAWeaviateFeature")
  .addEdge("financialAgentTaskResearchAWeaviateFeature", END)
;

export const graph = workflow.compile();
graph.name = "BlogCrewIndustryspecializedagentsexample";
// Workflow: blog_crew_workflow_pattern
// Workflow: Blog Crew Workflow Pattern
