/**
 * Workflow: chat_agent_state_graph
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Represents the StateGraph with a single 'chat' node. The START edge points to this node; modeled here by making the step a StartStep and setting stepOrder=1.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { chatAgent1 } from '../agents'

// ── Workflow Steps ──

const chatTask = createStep({
  id: 'chat_task',
  description: `Task logic (semantic summary extracted from source code):`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // You are a helpful assistant.
    // This step uses agent: chatAgent1
    // const result = await chatAgent1.generate('...')
    // TODO: Implement step logic
    throw new Error('chat_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * chat_agent_state_graph
 *
 * Represents the StateGraph with a single 'chat' node. The START edge points to this node; modeled here by making the step a StartStep and setting stepOrder=1.
 */
export const chatAgentStateGraph = createWorkflow({
  id: 'chat_agent_state_graph',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [chatTask],
})
  .then(chatTask)
  .commit()
