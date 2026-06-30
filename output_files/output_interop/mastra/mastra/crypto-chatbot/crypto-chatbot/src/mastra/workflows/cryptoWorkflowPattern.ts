/**
 * Workflow: Crypto workflow pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { searchCryptoCoinsTool, getCryptoPriceTool, getHistoricalCryptoPricesTool } from '../tools'

// ── Workflow Steps ──

const searchCryptoCoinsTask = createStep({
  id: 'search_crypto_coins_task',
  description: `Semantic task corresponding to the searchCryptoCoins tool.`,
  inputSchema: z.object({ keyword: z.string() }),
  outputSchema: z.object({example_fields: z.string()}),
  execute: async ({ inputData }) => {
    // Search all available crypto coins by a keyword.
    // This step uses tool: searchCryptoCoinsTool
    // TODO: Implement step logic
    throw new Error('search_crypto_coins_task not implemented yet')
  },
})

const getCryptoPriceTask = createStep({
  id: 'get_crypto_price_task',
  description: `Semantic task corresponding to the getCryptoPrice tool.`,
  inputSchema: z.object({ id: z.string() }),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Get crypto price by coin id
    // This step uses tool: getCryptoPriceTool
    // TODO: Implement step logic
    throw new Error('get_crypto_price_task not implemented yet')
  },
})

const getHistoricalCryptoPricesTask = createStep({
  id: 'get_historical_crypto_prices_task',
  description: `Semantic task corresponding to the getHistoricalCryptoPrices tool.`,
  inputSchema: z.object({ id: z.string(), days: z.number() }),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Get historical crypto prices for use in a chart
    // This step uses tool: getHistoricalCryptoPricesTool
    // TODO: Implement step logic
    throw new Error('get_historical_crypto_prices_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Crypto workflow pattern
 */
export const cryptoWorkflowPattern = createWorkflow({
  id: 'Crypto workflow pattern',
  inputSchema: z.object({ keyword: z.string() }),
  outputSchema: z.object({}),
  steps: [searchCryptoCoinsTask, getCryptoPriceTask, getHistoricalCryptoPricesTask],
})
  .then(searchCryptoCoinsTask)
  .then(getCryptoPriceTask)
  .then(getHistoricalCryptoPricesTask)
  .commit()
