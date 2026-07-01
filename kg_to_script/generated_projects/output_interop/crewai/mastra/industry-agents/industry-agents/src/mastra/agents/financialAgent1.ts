/**
 * Agent: Insight analyst exploring innovations in finance, wealth tech, and regulatory tech
 * ID: financial_agent_1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Vector Search: Capability to perform semantic vector search in a vector DB (Weaviate).
 *   - Web Search: Capability to perform web search queries using an external search API (SerperDev).
 */

import { Agent } from '@mastra/core/agent'

/**
 * Insight analyst exploring innovations in finance, wealth tech, and regulatory tech
 * 
 * Instructions:
 * You are Insight analyst exploring innovations in finance, wealth tech, and regulatory tech.
 */
export const financialAgent1 = new Agent({
  id: `financial_agent_1`,
  name: `Insight analyst exploring innovations in finance, wealth tech, and regulatory tech`,
  instructions: `You are Insight analyst exploring innovations in finance, wealth tech, and regulatory tech.`,
  model: 'openai/gpt-4o-mini',
})
