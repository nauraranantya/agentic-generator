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
import { stockAgent } from '../agents/stockAgent'

// Import tools used by workflow steps
import { stockPricesTool } from '../tools/stockPricesTool'

// ── Workflow Steps ──

const startStepFetchStockPrice = createStep({
  id: 'Start: Receive stock query',
  description: `Initial step: receive user query. In the example this corresponds to the call agent.generate('What is the current stock price of Apple (AAPL)?'). The code calls mastra.getAgent('stockAgent') then generate(...). Note: agent retrieval id in code ('stockAgent') differs from declared agent.id ('stock-agent') — see Issues/Assumptions.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Initial step: receive user query. In the example this corresponds to the call agent.generate('What is the current stock price of Apple (AAPL)?'). The code calls mastra.getAgent('stockAgent') then generate(...). Note: agent retrieval id in code ('stockAgent') differs from declared agent.id ('stock-agent') — see Issues/Assumptions.
    // TODO: Implement step logic
    throw new Error('Start: Receive stock query not implemented yet')
  },
})

const stepFetchStockPrice = createStep({
  id: 'Fetch step: agent uses tool',
  description: `Workflow step where the LLMAgent (stock_agent) processes the query using its LanguageModel and invokes the stockPrices tool to fetch the numeric price.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // What is the current stock price of Apple (AAPL)?
    // This step uses agent: stockAgent
    // const result = await stockAgent.generate('...')
    // This step uses tool: stockPricesTool
    // TODO: Implement step logic
    throw new Error('Fetch step: agent uses tool not implemented yet')
  },
})

const endStepFetchStockPrice = createStep({
  id: 'End: Present price to user',
  description: `Final step: format or present the fetched price. In src/index.ts this is represented by code that reads toolResults to find toolName === 'stockPrices' and then prints currentPrice to console.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Final step: format or present the fetched price. In src/index.ts this is represented by code that reads toolResults to find toolName === 'stockPrices' and then prints currentPrice to console.
    // TODO: Implement step logic
    throw new Error('End: Present price to user not implemented yet')
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
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [startStepFetchStockPrice, stepFetchStockPrice, endStepFetchStockPrice],
})
  .then(startStepFetchStockPrice)
  .then(stepFetchStockPrice)
  .then(endStepFetchStockPrice)
  .commit()
