/**
 * Agent: AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.
 * ID: healthcare_agent_1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Vector Search: Capability to perform semantic vector search in a vector DB (Weaviate).
 *   - Web Search: Capability to perform web search queries using an external search API (SerperDev).
 */

import { Agent } from '@mastra/core/agent'

/**
 * AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.
 * 
 * Instructions:
 * You are AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement..
 */
export const healthcareAgent1 = new Agent({
  id: `healthcare_agent_1`,
  name: `AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement.`,
  instructions: `You are AI-savvy marketer specializing in healthcare systems, digital health, and patient engagement..`,
  model: 'openai/gpt-4o-mini',
})
