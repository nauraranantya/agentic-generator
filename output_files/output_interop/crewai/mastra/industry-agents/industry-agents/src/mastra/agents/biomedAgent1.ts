/**
 * Agent: Industry researcher focused on biomedical trends and their applications in AI
 * ID: biomed_agent_1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - Vector Search: Capability to perform semantic vector search in a vector DB (Weaviate).
 *   - Web Search: Capability to perform web search queries using an external search API (SerperDev).
 */

import { Agent } from '@mastra/core/agent'

/**
 * Industry researcher focused on biomedical trends and their applications in AI
 * 
 * Instructions:
 * You are Industry researcher focused on biomedical trends and their applications in AI.
 */
export const biomedAgent1 = new Agent({
  id: `biomed_agent_1`,
  name: `Industry researcher focused on biomedical trends and their applications in AI`,
  instructions: `You are Industry researcher focused on biomedical trends and their applications in AI.`,
  model: 'openai/gpt-4o-mini',
})
