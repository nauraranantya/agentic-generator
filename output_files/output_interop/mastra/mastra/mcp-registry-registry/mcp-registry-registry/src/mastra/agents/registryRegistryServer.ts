/**
 * Agent: mcp-server
 * ID: registry-registry-server
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - : Provides filtered listings of MCP registries (id, tag, name) and can emit detailed or summary responses.
 *   - : Fetch servers from a registry endpoint, apply registry-specific post-processing, and filter results by tag or search term.
 *   - : Ability to list registries and retrieve servers from registries via exposed tools.
 */

import { Agent } from '@mastra/core/agent'

// Import tools
import { toolRegistryList, toolRegistryServers } from '../tools'

/**
 * mcp-server
 * 
 * Instructions:
 * You are mcp-server.
 */
export const registryRegistryServer = new Agent({
  id: `registry-registry-server`,
  name: `mcp-server`,
  instructions: `You are mcp-server.`,
  model: 'openai/gpt-4o-mini',
  tools: {
    toolRegistryList,
    toolRegistryServers,
  },
})
