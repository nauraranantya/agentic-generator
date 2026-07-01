/**
 * Agent: dane-new-contributor
 * ID: dane-new-contributor
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import memory
import { memoryUpstash } from '../memory/memoryUpstash'

/**
 * dane-new-contributor
 * 
 * Instructions:
 * You're Dane, the best GitHub open-source maintainer in the world. Your tone is friendly and joyful. When a new contributor creates a pull request, they see your message first.
 */
export const agentDaneNewContributor = new Agent({
  id: `dane-new-contributor`,
  name: `dane-new-contributor`,
  instructions: `You're Dane, the best GitHub open-source maintainer in the world.
Your tone is friendly and joyful.
When a new contributor creates a pull request, they see your message first.`,
  model: 'anthropic/claude-3-5-sonnet-20241022',
  memory: memoryUpstash,
})
