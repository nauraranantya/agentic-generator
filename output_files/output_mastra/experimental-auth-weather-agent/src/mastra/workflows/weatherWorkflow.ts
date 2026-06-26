/**
 * Workflow: weather-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that (1) fetches weather for a city and (2) generates activity recommendations based on the forecast.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { weatherAgent } from '../agents'

// Import tools used by workflow steps
import { weatherTool } from '../tools'

// ── Workflow Steps ──

const fetchWeatherStep = createStep({
  id: 'fetch-weather',
  description: `Fetches weather forecast for a given city.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Fetches weather forecast for a given city.
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('fetch-weather not implemented yet')
  },
})

const planActivitiesStep = createStep({
  id: 'plan-activities',
  description: `Suggests activities based on the normalized weather forecast.`,
  inputSchema: z.object({fields: z.string()}),
  outputSchema: z.object({A_single_string_containing_planned_activities_formatted_according_to_the_activity: z.string()}),
  execute: async ({ inputData }) => {
    // Based on the following weather forecast for {location}, suggest appropriate activities:
    // This step uses agent: weatherAgent
    // const result = await weatherAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('plan-activities not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * weather-workflow
 *
 * Workflow that (1) fetches weather for a city and (2) generates activity recommendations based on the forecast.
 */
export const weatherWorkflow = createWorkflow({
  id: 'weather-workflow',
  inputSchema: z.object({}),
  outputSchema: z.object({A_single_string_containing_planned_activities_formatted_according_to_the_activity: z.string()}),
  steps: [fetchWeatherStep, planActivitiesStep],
})
  .parallel([fetchWeatherStep, planActivitiesStep])
  .commit()
