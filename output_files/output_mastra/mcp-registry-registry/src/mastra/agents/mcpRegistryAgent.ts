/**
 * Agent: MCP Registry Agent
 * ID: mcp-registry-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { mcpClient } from '../tools/mcpClient'
import { mcpRegistryTool } from '../tools/mcpRegistryTool'

/**
 * MCP Registry Agent
 * 
 * Instructions:
 * You are a helpful assistant that provides information about MCP registries. You can search for registries by ID, tag, or name.
 */
export const mcpRegistryAgent = new Agent({
  id: `mcp-registry-agent`,
  name: `MCP Registry Agent`,
  instructions: `You are a helpful assistant that provides information about MCP registries. You can search for registries by ID, tag, or name.`,
  model: 'openai/gpt-4o',
  tools: {
    mcpClient,
    mcpRegistryTool,
  },
})
