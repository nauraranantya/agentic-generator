/**
 * Workflow: SurpriseTravel Sequential Workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow pattern with three sequential steps: (1) personalized activity planning, (2) restaurant and scenic location scouting, (3) itinerary compilation.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { personalizedActivityPlanner, restaurantScout, itineraryCompiler } from '../agents'

// ── Workflow Steps ──

const personalizedActivityPlanningTask = createStep({
  id: 'personalized_activity_planning_task',
  description: `Research and find cool things to do at {destination}.`,
  inputSchema: z.object({origin: z.string(), destination: z.string(), age: z.string(), hotel_location: z.string(), flight_information: z.string(), trip_duration: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task: Research and find activities and events at {destination} tailored to the traveler's profile.
    // This step uses agent: personalizedActivityPlanner
    // const result = await personalizedActivityPlanner.generate('...')
    // TODO: Implement step logic
    throw new Error('personalized_activity_planning_task not implemented yet')
  },
})

const restaurantScenicLocationScoutTask = createStep({
  id: 'restaurant_scenic_location_scout_task',
  description: `Find highly-rated restaurants and dining experiences at {destination}.`,
  inputSchema: z.object({origin: z.string(), destination: z.string(), age: z.string(), hotel_location: z.string(), flight_information: z.string(), trip_duration: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task: Find restaurants and scenic locations at {destination}, provide addresses, types, descriptions and ratings.
    // This step uses agent: restaurantScout
    // const result = await restaurantScout.generate('...')
    // TODO: Implement step logic
    throw new Error('restaurant_scenic_location_scout_task not implemented yet')
  },
})

const itineraryCompilationTask = createStep({
  id: 'itinerary_compilation_task',
  description: `Compile all researched information into a comprehensive day-by-day itinerary for the trip to {destination}.`,
  inputSchema: z.object({origin: z.string(), destination: z.string(), age: z.string(), hotel_location: z.string(), flight_information: z.string(), trip_duration: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task: Compile all researched information into a day-by-day itinerary for the trip to {destination}, include flights, hotel, activities and restaurants.
    // This step uses agent: itineraryCompiler
    // const result = await itineraryCompiler.generate('...')
    // TODO: Implement step logic
    throw new Error('itinerary_compilation_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * SurpriseTravel Sequential Workflow
 *
 * Workflow pattern with three sequential steps: (1) personalized activity planning, (2) restaurant and scenic location scouting, (3) itinerary compilation.
 */
export const surpriseTravelWorkflow = createWorkflow({
  id: 'SurpriseTravel Sequential Workflow',
  inputSchema: z.object({origin: z.string(), destination: z.string(), age: z.string(), hotel_location: z.string(), flight_information: z.string(), trip_duration: z.string()}),
  outputSchema: z.object({}),
  steps: [personalizedActivityPlanningTask, restaurantScenicLocationScoutTask, itineraryCompilationTask],
})
  .then(personalizedActivityPlanningTask)
  .then(restaurantScenicLocationScoutTask)
  .then(itineraryCompilationTask)
  .commit()
