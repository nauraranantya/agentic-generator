/**
 * Agent: crypto-agent
 * ID: crypto-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Search available crypto coins by keyword (implements searchCryptoCoins tool behavior).
 *   - : Get current crypto price by coin id (implements getCryptoPrice tool behavior).
 *   - : Get historical crypto prices for chart (implements getHistoricalCryptoPrices tool behavior).
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { searchCryptoCoinsTool, getCryptoPriceTool, getHistoricalCryptoPricesTool } from '../tools'

// Import memory
import { cryptoAgentMemory } from '../memory'

/**
 * crypto-agent
 * 
 * Instructions:
 * You are crypto-agent.
 */
export const cryptoAgent = new Agent({
  id: `crypto-agent`,
  name: `crypto-agent`,
  instructions: `You are crypto-agent.`,
  model: 'openai/gpt-4o-mini.',
  tools: {
    searchCryptoCoinsTool,
    getCryptoPriceTool,
    getHistoricalCryptoPricesTool,
  },
  memory: cryptoAgentMemory,
})
