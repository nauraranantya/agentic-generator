/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Chef Agent Goal (Recipe Retrieval): Return a useful recipe given an ingredient and available tools/equipment.
 * Environments:
 *   - My Utility MCP Server (myMcpServerTwo) (): MCP server providing tools, agents, workflows, and weather resources.
 *   - My Calculation & Data MCP Server (myMcpServer) (): MCP server providing calculator and fetchWeather tools.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent, chefAgentResponses, chefModelV2Agent, dynamicAgent, agentThatHarassesYou, errorAgent, networkAgent, weatherAgent, evalAgent } from './agents'

// Import workflows
import { recipeMakerWorkflow, lessComplexWorkflow, nestedWorkflow, myWorkflowX } from './workflows'

// Import memory instances
import { globalMemory, chefAgentMemory } from './memory'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * The system instance that contains agents, workflows, processors, MCP servers, and tools as configured in the source.
 */
export const mastra = new Mastra({
  agents: {
    chefAgent,
    chefAgentResponses,
    chefModelV2Agent,
    dynamicAgent,
    agentThatHarassesYou,
    errorAgent,
    networkAgent,
    weatherAgent,
    evalAgent,
  },
  workflows: {
    recipeMakerWorkflow,
    lessComplexWorkflow,
    nestedWorkflow,
    myWorkflowX,
  },
  memory: {
    globalMemory,
    chefAgentMemory,
  },
})
