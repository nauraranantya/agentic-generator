/**
 * Mastra AI Instance - SurpriseTravelCrew
 * 
 * Auto-generated from AgentO Knowledge Graph
 * Pipeline: KG (.ttl) → SPARQL → Pydantic IR → TypeScript
 * Goals:
 *   - Goal: personalized activity planner: Research and find cool things to do at the destination, including activities and events that match the traveler's interests and age group
 *   - Goal: restaurant scout: Find highly-rated restaurants and dining experiences at the destination, and recommend scenic locations and fun activities
 *   - Goal: itinerary compiler: Compile all researched information into a comprehensive day-by-day itinerary, ensuring the integration of flights and hotel information
 * Objectives:
 *   - : Produce a per-day list of recommended activities and events including details and suitability rationale.
 *   - : Produce recommended restaurants and scenic locations with ratings and descriptions for each relevant day.
 *   - : Produce a single integrated itinerary document that schedules flights, hotel, day plans, activities and restaurants.
 */

import { Mastra } from '@mastra/core'

// Import agents
import { personalizedActivityPlanner, restaurantScout, itineraryCompiler } from './agents'

// Import workflows
import { surpriseTravelWorkflow } from './workflows'

/**
 * Mastra instance with registered agents, workflows, and memory.
 *
 * SurpriseTravel crew coordinating agents to plan a surprise travel itinerary.
    Agents: personalized_activity_planner, restaurant_scout, itinerary_compiler.
    Process: sequential (represented in steps order).
 */
export const mastra = new Mastra({
  agents: {
    personalizedActivityPlanner,
    restaurantScout,
    itineraryCompiler,
  },
  workflows: {
    surpriseTravelWorkflow,
  },
})
