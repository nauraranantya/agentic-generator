/**
 * Workflow: Order Pizza Graph
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { pizzaOrdererV1 } from '../agents'

// Import tools used by workflow steps
import { toolPizzaFinder, toolPizzaOrderingSystem } from '../tools'

// ── Workflow Steps ──

const findPizzaShopTask = createStep({
  id: 'Find Pizza Shop Task',
  description: `Source semantics captured from node 'findStore':`,
  inputSchema: z.object({location: z.string(), pizza_company: z.string()}),
  outputSchema: z.object({with_fields: z.string()}),
  execute: async ({ inputData }) => {
    // You are a helpful AI assistant, tasked with extracting information from the conversation between you, and the user, in order to find a pizza shop for them.
    // This step uses agent: pizzaOrdererV1
    // const result = await pizzaOrdererV1.generate('...')
    // This step uses tool: toolPizzaFinder
    // TODO: Implement step logic
    throw new Error('Find Pizza Shop Task not implemented yet')
  },
})

const placePizzaOrderTask = createStep({
  id: 'Place Pizza Order Task',
  description: `Source semantics captured from node 'orderPizza':`,
  inputSchema: z.object({address: z.string(), phone_number: z.string(), order: z.string()}),
  outputSchema: z.object({with_fields: z.string()}),
  execute: async ({ inputData }) => {
    // You are a helpful AI assistant, tasked with placing an order for a pizza for the user.
    // This step uses agent: pizzaOrdererV1
    // const result = await pizzaOrdererV1.generate('...')
    // This step uses tool: toolPizzaOrderingSystem
    // TODO: Implement step logic
    throw new Error('Place Pizza Order Task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Order Pizza Graph
 */
export const orderPizzaGraph = createWorkflow({
  id: 'Order Pizza Graph',
  inputSchema: z.object({location: z.string(), pizza_company: z.string()}),
  outputSchema: z.object({with_fields: z.string()}),
  steps: [findPizzaShopTask, placePizzaOrderTask],
})
  .then(findPizzaShopTask)
  .then(placePizzaOrderTask)
  .commit()
