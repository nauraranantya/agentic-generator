/**
 * Agent: AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.
 * ID: HealthcareMarketingAgent
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
 * AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.
 * 
 * Instructions:
 * Stay updated on healthcare policy shifts, digital health trends, and explore how Weaviate’s features can optimize workflows in hospital systems, EHR integration, and health communication.
 */
export const healthcareMarketingAgent = new Agent({
  id: `HealthcareMarketingAgent`,
  name: `AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.`,
  instructions: `Stay updated on healthcare policy shifts, digital health trends, and explore how Weaviate’s features can optimize workflows in hospital systems, EHR integration, and health communication.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolWeaviateVectorSearchTool,
    toolSerperDevTool,
  },
})
