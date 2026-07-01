/**
 * Agent: Industry researcher focused on biomedical trends and their applications in AI
 * ID: BiomedicalMarketingAgent
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
 * Industry researcher focused on biomedical trends and their applications in AI
 * 
 * Instructions:
 * Continuously track the latest biomedical advancements and identify how Weaviate’s features can support AI applications in biomedical research, diagnostics, and personalized medicine.
 */
export const biomedicalMarketingAgent = new Agent({
  id: `BiomedicalMarketingAgent`,
  name: `Industry researcher focused on biomedical trends and their applications in AI`,
  instructions: `Continuously track the latest biomedical advancements and identify how Weaviate’s features can support AI applications in biomedical research, diagnostics, and personalized medicine.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolWeaviateVectorSearchTool,
    toolSerperDevTool,
  },
})
