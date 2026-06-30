/**
 * Tool: markdown_validation_tool
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Tool definition (from src/markdown_validator/tools/markdownTools.py): - Tool name registered as 'markdown_validation_tool' - Signature (conceptual): input: file_path (string) -> output: validation_results (string) - Behavior:     * Checks whether file_path exists on filesystem; returns error string if not found.     * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.     * Uses format_scan_result to transform the scan result to a formatted string.     * On PyMarkdownApiException returns 'API Exception: <exception message>'. - Output format:     * If no failures: 'No markdown validation issues found.'     * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description - Constraints and usage note:     * The tool expects only the path (filename) as input.     * The task instructs the agent to pass only the filename to this tool.
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * markdown_validation_tool
 * 
 * Implementation: Tool definition (from src/markdown_validator/tools/markdownTools.py): - Tool name registered as 'markdown_validation_tool' - Signature (conceptual): input: file_path (string) -> output: validation_results (string) - Behavior:     * Checks whether file_path exists on filesystem; returns error string if not found.     * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.     * Uses format_scan_result to transform the scan result to a formatted string.     * On PyMarkdownApiException returns 'API Exception: <exception message>'. - Output format:     * If no failures: 'No markdown validation issues found.'     * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description - Constraints and usage note:     * The tool expects only the path (filename) as input.     * The task instructs the agent to pass only the filename to this tool.
 */
export const markdownValidationTool = createTool({
  id: 'markdown_validation_tool',
  description: `Tool definition (from src/markdown_validator/tools/markdownTools.py):
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
    * The task instructs the agent to pass only the filename to this tool.`,
  inputSchema: z.object({input: z.string(), If_failures: z.string()}),
  outputSchema: z.object({}),  // TODO: Define output schema
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Tool definition (from src/markdown_validator/tools/markdownTools.py): - Tool name registered as 'markdown_validation_tool' - Signature (conceptual): input: file_path (string) -> output: validation_results (string) - Behavior:     * Checks whether file_path exists on filesystem; returns error string if not found.     * Calls PyMarkdownApi().scan_path(file_path.strip()) to perform the markdown scan.     * Uses format_scan_result to transform the scan result to a formatted string.     * On PyMarkdownApiException returns 'API Exception: <exception message>'. - Output format:     * If no failures: 'No markdown validation issues found.'     * If failures: one line per failure with: File, Line, Rule, Rule name, Rule description - Constraints and usage note:     * The tool expects only the path (filename) as input.     * The task instructs the agent to pass only the filename to this tool.
    // Configurations:
    //   - tool_registration_name: markdown_validation_tool
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool markdown_validation_tool not implemented yet')
  },
})
