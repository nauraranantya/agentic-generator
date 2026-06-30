/**
 * Agent: Meta Quest Expert
 * ID: meta_quest_expert
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective assigned to the crew: answer user questions by using available knowledge sources (PDF manual) and agent capabilities.
 */

import { Agent } from '@mastra/core/agent'

/**
 * Meta Quest Expert
 * 
 * Instructions:
 * Agent-level instruction/backstory used to guide the agent's independent reasoning and responses.
 */
export const metaQuestExpert = new Agent({
  id: `meta_quest_expert`,
  name: `Meta Quest Expert`,
  instructions: `Agent-level instruction/backstory used to guide the agent's independent reasoning and responses.`,
  model: 'openai/gpt-4o-mini',
})
