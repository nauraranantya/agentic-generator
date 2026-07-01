/**
 * Agent: Meta Quest Expert
 * ID: meta_quest_expert
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * Meta Quest Expert
 * 
 * Instructions:
 * Agent-level goal extracted from agents.yaml.
 */
export const metaQuestExpert = new Agent({
  id: `meta_quest_expert`,
  name: `Meta Quest Expert`,
  instructions: `Agent-level goal extracted from agents.yaml.`,
  model: 'openai/gpt-4o-mini',
})
