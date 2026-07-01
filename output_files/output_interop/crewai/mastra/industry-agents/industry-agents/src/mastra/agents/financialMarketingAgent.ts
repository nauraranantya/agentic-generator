/**
 * Agent: Insight analyst exploring innovations in finance, wealth tech, and regulatory tech
 * ID: FinancialMarketingAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Performs semantic vector search over document chunks in Weaviate.
 *   - : Performs web search via Serper.dev.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolWeaviateVectorSearchTool, toolSerperDevTool } from '../tools'

/**
 * Insight analyst exploring innovations in finance, wealth tech, and regulatory tech
 * 
 * Instructions:
 * Monitor financial sector trends including AI in trading, compliance automation, and client advisory, and assess how Weaviate’s tools can enable cutting-edge financial applications.
 */
export const financialMarketingAgent = new Agent({
  id: `FinancialMarketingAgent`,
  name: `Insight analyst exploring innovations in finance, wealth tech, and regulatory tech`,
  instructions: `Monitor financial sector trends including AI in trading, compliance automation, and client advisory, and assess how Weaviate’s tools can enable cutting-edge financial applications.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolWeaviateVectorSearchTool,
    toolSerperDevTool,
  },
})
