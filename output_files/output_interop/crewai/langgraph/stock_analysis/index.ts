import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const StockAnalysisCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: tool_calculator
const tool_calculator = tool(
  async () => {
    return "Result of tool_calculator";
  },
  {
    name: "tool_calculator",
    description: "Calculator tool (from src/stock_analysis/tools/calculator_tool.py).
    Purpose: perform mathematical calculations expressed as arithmetic expressions (examples: '200*7', '5000/2*10').
    Implementation notes summarized: safe AST evaluation allowing operators + - * / ** % and unary +/-. Filters allowed characters using regex '^[0-9+\\-*/().% ]+$'. Raises ValueError on invalid input or errors (syntax, division by zero, unsupported nodes).",
    schema: z.object({}),
  }
);
// Tool: tool_scrape_website
const tool_scrape_website = tool(
  async () => {
    return "Result of tool_scrape_website";
  },
  {
    name: "tool_scrape_website",
    description: "Tool used to fetch and convert HTML pages into text for downstream processing. Referenced from crewai_tools usage in the crew.",
    schema: z.object({}),
  }
);
// Tool: tool_website_search
const tool_website_search = tool(
  async () => {
    return "Result of tool_website_search";
  },
  {
    name: "tool_website_search",
    description: "Tool used for general website search (referenced from crewai_tools in the crew).",
    schema: z.object({}),
  }
);
// Tool: tool_txt_search
const tool_txt_search = tool(
  async () => {
    return "Result of tool_txt_search";
  },
  {
    name: "tool_txt_search",
    description: "Tool used for searching plaintext resources (referenced from crewai_tools in the crew).",
    schema: z.object({}),
  }
);
// Tool: sec10_k_tool_generic
const sec10_k_tool_generic = tool(
  async () => {
    return "Result of sec10_k_tool_generic";
  },
  {
    name: "sec10_k_tool_generic",
    description: "A RAG-style tool for semantic search in 10-K filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-K filing via the SEC API (sec_api.QueryApi using environment variable SEC_API_API_KEY), requests the filing details URL, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\\s\\n]' and adds resulting text to its internal RAG index (DataType.TEXT).",
    schema: z.object({}),
  }
);
// Tool: sec10_k_tool_amzn
const sec10_k_tool_amzn = tool(
  async () => {
    return "Result of sec10_k_tool_amzn";
  },
  {
    name: "sec10_k_tool_amzn",
    description: "Instance of SEC10KTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-K, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10KToolSchema (only search_query required subsequently).",
    schema: z.object({}),
  }
);
// Tool: sec10_q_tool_generic
const sec10_q_tool_generic = tool(
  async () => {
    return "Result of sec10_q_tool_generic";
  },
  {
    name: "sec10_q_tool_generic",
    description: "A RAG-style tool for semantic search in 10-Q filings (class src/stock_analysis/tools/sec_tools.py).
    Default args_schema: requires search_query and stock_name.
    Behavior: when initialized with a specific stock_name, it fetches the most recent 10-Q filing via the SEC API, converts HTML to text using html2text, cleans non-alphanumeric characters with regex r'[^a-zA-Z$0-9\\s\\n]' and adds resulting text to its internal index (DataType.TEXT).",
    schema: z.object({}),
  }
);
// Tool: sec10_q_tool_amzn
const sec10_q_tool_amzn = tool(
  async () => {
    return "Result of sec10_q_tool_amzn";
  },
  {
    name: "sec10_q_tool_amzn",
    description: "Instance of SEC10QTool initialized with stock_name='AMZN'. On init it attempted to fetch AMZN's latest 10-Q, converted it to text, cleaned non-alphanumeric characters, and added the text to its internal index. Its args_schema becomes FixedSEC10QToolSchema (only search_query required subsequently).",
    schema: z.object({}),
  }
);



/**
 * Node: research
 * Agent: research_analyst_agent
 */
async function research(state: typeof StockAnalysisCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System prompt for the research analyst agent." +
        "\nNode: research",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: filingsAnalysis
 * Agent: financial_analyst_agent
 */
async function filingsAnalysis(state: typeof StockAnalysisCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration)." +
        "\nNode: filingsAnalysis",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: financialAnalysis
 * Agent: financial_analyst_agent
 */
async function financialAnalysis(state: typeof StockAnalysisCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "This prompt is produced from the second factory for financial_analyst_agent in the code (duplicate configuration)." +
        "\nNode: financialAnalysis",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: recommend
 * Agent: investment_advisor_agent
 */
async function recommend(state: typeof StockAnalysisCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "System prompt for the investment advisor agent." +
        "\nNode: recommend",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(StockAnalysisCrewAnnotation)
  .addNode("research", research)
  .addNode("filingsAnalysis", filingsAnalysis)
  .addNode("financialAnalysis", financialAnalysis)
  .addNode("recommend", recommend)
  .addEdge(START, "research")
  .addEdge("research", "filingsAnalysis")
  .addEdge("filingsAnalysis", "financialAnalysis")
  .addEdge("financialAnalysis", "recommend")
  .addEdge("recommend", END)
;

export const graph = workflow.compile();
graph.name = "StockAnalysisCrew";
// Workflow: stock_analysis_workflow
// Workflow: Stock Analysis Sequential Workflow
