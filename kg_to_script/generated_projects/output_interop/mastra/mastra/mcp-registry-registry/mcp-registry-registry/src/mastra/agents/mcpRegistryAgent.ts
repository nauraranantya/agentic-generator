/**
 * Agent: registry
 * ID: mcp-registry-agent
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Objectives:
 *   - : Objective for the MCP Registry Agent and Team: enable searching and retrieving MCP registry information by ID, tag, or name.
 * Capabilities:
 *   - : Capability to return the set of available MCP tools. In source code this is invoked at initialization (await mcp.listTools()) to populate the agent's tools.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { mcpClient, mcpRegistryTool } from '../tools'

/**
 * registry
 * 
 * Instructions:
 * Agent bootstrap prompt / instruction used to guide agent behavior independent of a specific task.
 */
export const mcpRegistryAgent = new Agent({
  id: `mcp-registry-agent`,
  name: `registry`,
  instructions: `Agent bootstrap prompt / instruction used to guide agent behavior independent of a specific task.`,
  model: 'openai/gpt-4o',
  tools: {
    mcpClient,
    mcpRegistryTool,
  },
})
