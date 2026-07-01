/**
 * Agent: Test Agent (defined in mastra config: 'test-agent')
 * ID: test-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolChangeColor } from '../tools/toolChangeColor'
import { toolChangeLogoSize } from '../tools/toolChangeLogoSize'
import { toolAddPost } from '../tools/toolAddPost'

/**
 * Test Agent (defined in mastra config: 'test-agent')
 * 
 * Instructions:
 * You are a browser client agent. You execute tools in the browser.
 */
export const agentBackend = new Agent({
  id: `test-agent`,
  name: `Test Agent (defined in mastra config: 'test-agent')`,
  instructions: `You are a browser client agent. You execute tools in the browser.`,
  model: 'openai/gpt-4o',
  tools: {
    toolChangeColor,
    toolChangeLogoSize,
    toolAddPost,
  },
})
