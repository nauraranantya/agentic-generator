/**
 * Agent: Assistant / Code Writer
 * ID: code_writer_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Ability to execute arbitrary code snippets in a sandboxed local environment.
 *   - : Download historical stock close prices for given symbols and date range.
 *   - : Render time series plots for stock price data and save to image files.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Assistant / Code Writer
 * 
 * Instructions:
 * You are Assistant / Code Writer.
 */
export const codeWriterAgent = new Agent({
  id: `code_writer_agent`,
  name: `Assistant / Code Writer`,
  instructions: `You are Assistant / Code Writer.`,
  model: 'openai/gpt-4-turbo',
})
