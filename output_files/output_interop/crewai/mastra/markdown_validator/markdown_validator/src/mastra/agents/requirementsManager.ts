/**
 * Agent: Requirements Manager
 * ID: Requirements_Manager
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Identify markdown syntax issues using pymarkdown, returning formatted scan failures (file, line, rule, description).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { markdownValidationTool } from '../tools'

/**
 * Requirements Manager
 * 
 * Instructions:
 * Provide a detailed list of the markdown linting results. Give a summary with actionable tasks to address the validation results. Write your response as if you were handing it to a developer to fix the issues. DO NOT provide examples of how to fix the issues or recommend other tools to use.
 */
export const requirementsManager = new Agent({
  id: `Requirements_Manager`,
  name: `Requirements Manager`,
  instructions: `Provide a detailed list of the markdown linting results.
Give a summary with actionable tasks to address the validation results.
Write your response as if you were handing it to a developer to fix the issues.
DO NOT provide examples of how to fix the issues or recommend other tools to use.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    markdownValidationTool,
  },
})
