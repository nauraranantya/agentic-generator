/**
 * Agent: Code Executor
 * ID: code_executor_agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Ability to execute arbitrary code snippets in a sandboxed local environment.
 *   - : Download historical stock close prices for given symbols and date range.
 *   - : Render time series plots for stock price data and save to image files.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolLocalCliExecutor, toolGetStockPrices, toolPlotStockPrices } from '../tools'

/**
 * Code Executor
 * 
 * Instructions:
 * You are Code Executor.
 */
export const codeExecutorAgent = new Agent({
  id: `code_executor_agent`,
  name: `Code Executor`,
  instructions: `You are Code Executor.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolLocalCliExecutor,
    toolGetStockPrices,
    toolPlotStockPrices,
  },
})
