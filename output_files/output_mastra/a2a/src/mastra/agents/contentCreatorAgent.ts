/**
 * Agent: LLM Agent
 * ID: content-creator-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective assigned to the team: gather research on agent networks and produce engaging content. Tasks ResearchTask and ContentTask contribute to this objective.
 */

import { Agent } from '@mastra/core/agent'

/**
 * LLM Agent
 * 
 * Instructions:
 * You are LLM Agent.
 */
export const contentCreatorAgent = new Agent({
  id: `content-creator-agent`,
  name: `LLM Agent`,
  instructions: `You are LLM Agent.`,
  model: 'openai/gpt-4o',
})
