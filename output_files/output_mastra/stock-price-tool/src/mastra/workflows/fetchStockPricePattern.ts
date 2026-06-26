/**
 * Workflow: Fetch Stock Price Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple workflow pattern that accepts a stock-symbol query, has the agent generate and delegate to the stockPrices tool, and produces a numeric price as output.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { stockAgent } from '../agents'

// Import tools used by workflow steps
import { stockPricesTool } from '../tools'

// ── Workflow Steps ──

const stepFetchStockPrice = createStep({
  id: 'Fetch stock price for symbol (AAPL example)',
  description: `Task representing the user's invocation in src/index.ts where the agent is asked: 'What is the current stock price of Apple (AAPL)?'. The agent handles the query using its model and invokes the stockPrices tool to fetch the numeric price.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // What is the current stock price of Apple (AAPL)?
    // This step uses agent: stockAgent
    // const result = await stockAgent.generate('...')
    // This step uses tool: stockPricesTool
    // TODO: Implement step logic
    throw new Error('Fetch stock price for symbol (AAPL example) not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Fetch Stock Price Pattern
 *
 * A simple workflow pattern that accepts a stock-symbol query, has the agent generate and delegate to the stockPrices tool, and produces a numeric price as output.
 */
export const fetchStockPricePattern = createWorkflow({
  id: 'Fetch Stock Price Pattern',
  inputSchema: z.object({A_simple_workflow_pattern_that_accepts_a_stock: z.string()}),
  outputSchema: z.object({}),
  steps: [stepFetchStockPrice],
})
  .then(stepFetchStockPrice)
  .commit()
