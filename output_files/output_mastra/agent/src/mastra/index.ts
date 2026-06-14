/**
 * Mastra AI Instance - MastraSystem
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 */

import { Mastra } from '@mastra/core'

// Import agents
import { chefAgent } from './agents/chefAgent'
import { chefAgentResponses } from './agents/chefAgentResponses'
import { chefModelV2Agent } from './agents/chefModelV2Agent'
import { dynamicAgent } from './agents/dynamicAgent'
import { agentThatHarassesYou } from './agents/agentThatHarassesYou'
import { errorAgent } from './agents/errorAgent'
import { networkAgent } from './agents/networkAgent'
import { weatherAgent } from './agents/weatherAgent'
import { evalAgent } from './agents/evalAgent'

// Import workflows
import { recipeMakerWorkflow } from './workflows/recipeMakerWorkflow'
import { lessComplexWorkflow } from './workflows/lessComplexWorkflow'
import { nestedWorkflow } from './workflows/nestedWorkflow'
import { myWorkflowX } from './workflows/myWorkflowX'

// Import memory instances
import { globalMemory } from './memory/globalMemory'
import { chefAgentMemory } from './memory/chefAgentMemory'

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
