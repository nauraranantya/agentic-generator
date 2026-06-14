/**
 * Workflow: airbnb-flow
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// ── Workflow Steps ──

const airbnbLocationStep = createStep({
  id: 'airbnbLocation',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // If accommodationType is 'hotel' call Search Hotels tool using arrivalCityId. If accommodationType is 'airbnb', first call Search Airbnb Location tool to get place id and then call Search Airbnb tool using that id, typeOfPlace, startDate, endDate. Do NOT call Airbnb tools if accommodationType is hotel. Do NOT call searchHotels if accommodationType is airbnb.
    // TODO: Implement step logic
    throw new Error('airbnbLocation not implemented yet')
  },
})

const accommodationStep = createStep({
  id: 'accommodation',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // If accommodationType is 'hotel' call Search Hotels tool using arrivalCityId. If accommodationType is 'airbnb', first call Search Airbnb Location tool to get place id and then call Search Airbnb tool using that id, typeOfPlace, startDate, endDate. Do NOT call Airbnb tools if accommodationType is hotel. Do NOT call searchHotels if accommodationType is airbnb.
    // TODO: Implement step logic
    throw new Error('accommodation not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * airbnb-flow
 */
export const airbnbFlowPattern = createWorkflow({
  id: 'airbnb-flow',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [airbnbLocationStep, accommodationStep],
})
  .then(airbnbLocationStep)
  .then(accommodationStep)
  .commit()
