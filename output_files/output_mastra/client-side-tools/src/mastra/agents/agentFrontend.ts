/**
 * Agent: Frontend Agent (runtime id: 'agent')
 * ID: agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolChangeColor } from '../tools/toolChangeColor'
import { toolChangeLogoSize } from '../tools/toolChangeLogoSize'
import { toolAddPost } from '../tools/toolAddPost'

/**
 * Frontend Agent (runtime id: 'agent')
 * 
 * Instructions:
 * You are a browser client agent. You execute tools in the browser.
 */
export const agentFrontend = new Agent({
  id: `agent`,
  name: `Frontend Agent (runtime id: 'agent')`,
  instructions: `You are a browser client agent. You execute tools in the browser.`,
  model: 'openai/gpt-4o',
  tools: {
    toolChangeColor,
    toolChangeLogoSize,
    toolAddPost,
  },
})
