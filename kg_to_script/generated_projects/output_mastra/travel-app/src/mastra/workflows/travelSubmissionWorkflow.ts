/**
 * Workflow: travel-submission
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { travelAgent } from '../agents'

// Import tools used by workflow steps
import { searchFlightsTool, searchAttractionsTool } from '../tools'

// Import nested sub-workflows
import { airbnbFlowPattern } from './airbnbFlowPattern'

// ── Workflow Steps ──

const findOutboundFlight = createStep({
  id: 'Find Outbound Flight',
  description: `Select 1 outbound flight for the given departureLocation -> arrivalLocation and date range. Return entire flight object including legs and timestamps. Consider flightPriority to trade off price vs convenience.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Select 1 outbound flight for the given departureLocation -> arrivalLocation and date range. Return entire flight object including legs and timestamps. Consider flightPriority to trade off price vs convenience.
    // This step uses agent: travelAgent
    // const result = await travelAgent.generate('...')
    // This step uses tool: searchFlightsTool
    // TODO: Implement step logic
    throw new Error('Find Outbound Flight not implemented yet')
  },
})

const findReturnFlight = createStep({
  id: 'Find Return Flight',
  description: `Select 1 return flight for the given arrivalLocation -> departureLocation and date range. Return entire flight object including legs and timestamps.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Select 1 return flight for the given arrivalLocation -> departureLocation and date range. Return entire flight object including legs and timestamps.
    // This step uses tool: searchFlightsTool
    // TODO: Implement step logic
    throw new Error('Find Return Flight not implemented yet')
  },
})

const findAccommodationHotelOrAirbnb = createStep({
  id: 'Find Accommodation (Hotel or Airbnb)',
  description: `If accommodationType is 'hotel' call Search Hotels tool using arrivalCityId. If accommodationType is 'airbnb', first call Search Airbnb Location tool to get place id and then call Search Airbnb tool using that id, typeOfPlace, startDate, endDate. Do NOT call Airbnb tools if accommodationType is hotel. Do NOT call searchHotels if accommodationType is airbnb.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // If accommodationType is 'hotel' call Search Hotels tool using arrivalCityId. If accommodationType is 'airbnb', first call Search Airbnb Location tool to get place id and then call Search Airbnb tool using that id, typeOfPlace, startDate, endDate. Do NOT call Airbnb tools if accommodationType is hotel. Do NOT call searchHotels if accommodationType is airbnb.
    // TODO: Implement step logic
    throw new Error('Find Accommodation (Hotel or Airbnb) not implemented yet')
  },
})

const findAttractions = createStep({
  id: 'Find Attractions',
  description: `Find three activities and attractions for the customer based on interests and arrivalAttractionId; return id, name, description, rating, price, imageUrl, location.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Find three activities and attractions for the customer based on interests and arrivalAttractionId; return id, name, description, rating, price, imageUrl, location.
    // This step uses tool: searchAttractionsTool
    // TODO: Implement step logic
    throw new Error('Find Attractions not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * travel-submission
 */
export const travelSubmissionWorkflow = createWorkflow({
  id: 'travel-submission',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [findOutboundFlight, findReturnFlight, findAccommodationHotelOrAirbnb, findAttractions],
})
  .then(findOutboundFlight)
  .then(findReturnFlight)
  .then(findAccommodationHotelOrAirbnb)
  .then(findAttractions)
  .commit()
