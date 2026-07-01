/**
 * Agent: travel analyzer
 * ID: travel-analyzer
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : 
 *   - : 
 *   - : 
 *   - : 
 *   - : 
 */

import { Agent } from '@mastra/core/agent'

/**
 * travel analyzer
 * 
 * Instructions:
 * You are travel analyzer.
 */
export const travelAnalyzer = new Agent({
  id: `travel-analyzer`,
  name: `travel analyzer`,
  instructions: `You are travel analyzer.`,
  model: 'openai/gpt-4o-mini',
})
