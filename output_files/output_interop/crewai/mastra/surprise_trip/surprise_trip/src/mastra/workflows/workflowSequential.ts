/**
 * Workflow: workflow_sequential
 *
 * Auto-generated from AgentO Knowledge Graph
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { personalizedActivityPlanner, restaurantScout, itineraryCompiler } from '../agents'

// ── Workflow Steps ──

const taskPersonalizedActivityPlanningTask = createStep({
  id: 'task_personalized_activity_planning_task',
  description: `Research and find cool things to do at {destination}. Focus on activities and events that match the traveler's interests and age group. Utilize internet search tools and recommendation engines to gather the information.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Research and find cool things to do at {destination}. Focus on activities and events that match the traveler's interests and age group. Utilize internet search tools and recommendation engines to gather the information.
    // This step uses agent: personalizedActivityPlanner
    // const result = await personalizedActivityPlanner.generate('...')
    // TODO: Implement step logic
    throw new Error('task_personalized_activity_planning_task not implemented yet')
  },
})

const taskRestaurantScenicLocationScoutTask = createStep({
  id: 'task_restaurant_scenic_location_scout_task',
  description: `Find highly-rated restaurants and dining experiences at {destination}. Recommend scenic locations and fun activities that align with the traveler's preferences. Use internet search tools, restaurant review sites, and travel guides.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Find highly-rated restaurants and dining experiences at {destination}. Recommend scenic locations and fun activities that align with the traveler's preferences. Use internet search tools, restaurant review sites, and travel guides.
    // This step uses agent: restaurantScout
    // const result = await restaurantScout.generate('...')
    // TODO: Implement step logic
    throw new Error('task_restaurant_scenic_location_scout_task not implemented yet')
  },
})

const taskItineraryCompilationTask = createStep({
  id: 'task_itinerary_compilation_task',
  description: `Compile all researched information into a comprehensive day-by-day itinerary for the trip to {destination}. Ensure the itinerary integrates flights, hotel information, and all planned activities and dining experiences.`,
  inputSchema: z.object({}),
  outputSchema: z.object({A_detailed_itinerary_document_including_a_day_by: z.string()}),
  execute: async ({ inputData }) => {
    // Compile all researched information into a comprehensive day-by-day itinerary for the trip to {destination}. Ensure the itinerary integrates flights, hotel information, and all planned activities and dining experiences. Use text formatting and document creation tools to organize the information.
    // This step uses agent: itineraryCompiler
    // const result = await itineraryCompiler.generate('...')
    // TODO: Implement step logic
    throw new Error('task_itinerary_compilation_task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_sequential
 */
export const workflowSequential = createWorkflow({
  id: 'workflow_sequential',
  inputSchema: z.object({}),
  outputSchema: z.object({A_detailed_itinerary_document_including_a_day_by: z.string()}),
  steps: [taskPersonalizedActivityPlanningTask, taskRestaurantScenicLocationScoutTask, taskItineraryCompilationTask],
})
  .then(taskPersonalizedActivityPlanningTask)
  .then(taskRestaurantScenicLocationScoutTask)
  .then(taskItineraryCompilationTask)
  .commit()
