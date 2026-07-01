/**
 * Agent: pizza-ordering-assistant
 * ID: PizzaOrderer-v1
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Capabilities:
 *   - find_store: Capability to find a pizza shop given a location and optional company name.
 *   - place_order: Capability to place a pizza order given store contact and order details.
 */

import { Agent } from '@mastra/core/agent'

/**
 * pizza-ordering-assistant
 * 
 * Instructions:
 * General system role description used by both nodes as the system message.
 */
export const pizzaOrdererV1 = new Agent({
  id: `PizzaOrderer-v1`,
  name: `pizza-ordering-assistant`,
  instructions: `General system role description used by both nodes as the system message.`,
  model: 'anthropic/claude-3-5-sonnet-latest',
})
