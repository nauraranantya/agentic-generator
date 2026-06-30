import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MarkDownValidatorCrewAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: markdown_validation_tool
const markdown_validation_tool = tool(
  async () => {
    return "Result of markdown_validation_tool";
  },
  {
    name: "markdown_validation_tool",
    description: "Tool definition (from src/markdown_validator/tools/markdownTools.py):
- Tool name registered as 'markdown_validation_tool'
- Signature (conceptual): input: file_path (string) -> output: validation_results (string)
- Behavior:
    * Checks whether file_path exists on filesystem; returns error string if not found.
    * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.
    * Uses format_scan_result to transform the scan result to a formatted string.
    * On PyMarkdownApiException returns 'API Exception: <exception message>'.
- Output format:
    * If no failures: 'No markdown validation issues found.'
    * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description
- Constraints and usage note:
    * The tool expects only the path (filename) as input.
    * The task instructs the agent to pass only the filename to this tool.",
    schema: z.object({}),
  }
);



/**
 * Node: syntaxReviewTask
 * Agent: requirements_manager
 */
async function syntaxReviewTask(state: typeof MarkDownValidatorCrewAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "Agent backstory: expert business analyst and software QA specialist." +
        "\nNode: syntaxReviewTask",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MarkDownValidatorCrewAnnotation)
  .addNode("syntaxReviewTask", syntaxReviewTask)
  .addEdge(START, "syntaxReviewTask")
;

export const graph = workflow.compile();
graph.name = "MarkDownValidatorCrew";
// Workflow: markdown_validation_workflow_pattern
// Workflow: Markdown Validation Workflow (sequential)
