/**
 * Workflow: Stockbroker
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Top-level workflow pattern representing the Stockbroker StateGraph. The compiled graph contains a single 'agent' node which calls external tools and returns UI items.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { stockbroker01 } from '../agents'

// ── Workflow Steps ──

const callTools = createStep({
  id: 'Call tools',
  description: `Task executed by the Stockbroker agent to call the language model with bound tools and to route resulting tool calls to tool-specific handlers. Uses the system prompt and conversation messages as input to the LLM.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // When invoking tools the agent binds the following tool definitions to the LLM: 
    // This step uses agent: stockbroker01
    // const result = await stockbroker01.generate('...')
    // TODO: Implement step logic
    throw new Error('Call tools not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Stockbroker
 *
 * Top-level workflow pattern representing the Stockbroker StateGraph. The compiled graph contains a single 'agent' node which calls external tools and returns UI items.
 */
export const stockbrokerWorkflow = createWorkflow({
  id: 'Stockbroker',
  inputSchema: z.object({Top: z.string()}),
  outputSchema: z.object({}),
  steps: [callTools],
})
  .then(callTools)
  .commit()
