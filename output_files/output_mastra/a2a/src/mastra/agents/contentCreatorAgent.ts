/**
 * Agent: Content Creator Agent
 * ID: content-creator-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * Content Creator Agent
 * 
 * Instructions:
 * Create engaging content
 */
export const contentCreatorAgent = new Agent({
  id: `content-creator-agent`,
  name: `Content Creator Agent`,
  instructions: `Create engaging content`,
  model: 'openai/gpt-4o',
})
