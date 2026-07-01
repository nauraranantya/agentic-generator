/**
 * Tool: toolExtract
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Tool name: "extract" Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM. Schema (Zod, represented informally): {   location: string (describe: The location to plan the trip for. Can be a city, state, or country.),   startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),   endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),   numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.) } Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * toolExtract
 * 
 * Implementation: Tool name: "extract" Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM. Schema (Zod, represented informally): {   location: string (describe: The location to plan the trip for. Can be a city, state, or country.),   startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),   endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),   numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.) } Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.
 */
export const toolExtract = createTool({
  id: 'toolExtract',
  description: `Tool name: "extract"
Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM.
Schema (Zod, represented informally):
{
  location: string (describe: The location to plan the trip for. Can be a city, state, or country.),
  startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),
  endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),
  numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.)
}
Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.`,
  inputSchema: z.object({Purpose: z.string(), location: z.string(), startDate: z.string(), endDate: z.string(), numberOfGuests: z.number(), Behavior: z.string()}),
  outputSchema: z.object({}),  // TODO: Define output schema
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Tool name: "extract" Purpose: Extract TripDetails from conversation history. Bound to the agent's LLM. Schema (Zod, represented informally): {   location: string (describe: The location to plan the trip for. Can be a city, state, or country.),   startDate: string (optional, describe: The start date of the trip. YYYY-MM-DD),   endDate: string (optional, describe: The end date of the trip. YYYY-MM-DD),   numberOfGuests: number (describe: The number of guests. Defaults to 2 if unspecified.) } Behavior: the tool returns only fields specified by the user; do not make up values. If location is missing, a clarification message should be generated requesting the location.
    // Configurations:
    //   - schema: location:string; startDate?:string; endDate?:string; numberOfGuests?:number
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool toolExtract not implemented yet')
  },
})
