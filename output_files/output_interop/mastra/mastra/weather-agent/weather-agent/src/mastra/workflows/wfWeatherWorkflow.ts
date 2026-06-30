/**
 * Workflow: weather-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that fetches weather for a city and plans activities. Input schema: { city: string }. Produces activities text.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { weatherAgent } from '../agents'

// Import tools used by workflow steps
import { weatherTool } from '../tools'

// ── Workflow Steps ──

const fetchWeatherTask = createStep({
  id: 'fetch-weather task',
  description: `Fetches weather forecast for a given city and produces forecast array resource. Semantics: take city -> produce daily forecast array with fields date, maxTemp, minTemp, precipitationChance, condition, location.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Fetches weather forecast for a given city and produces forecast array resource. Semantics: take city -> produce daily forecast array with fields date, maxTemp, minTemp, precipitationChance, condition, location.
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('fetch-weather task not implemented yet')
  },
})

const planActivities = createStep({
  id: 'plan-activities',
  description: `Suggests activities based on weather conditions. Input: forecast array (or forecast object). The step constructs a prompt 'Based on the following weather forecast for {location}, suggest appropriate activities: {JSON}' and streams agent response. Produces an activities text resource.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
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
 * Workflow that fetches weather for a city and plans activities. Input schema: { city: string }. Produces activities text.
 */
export const wfWeatherWorkflow = createWorkflow({
  id: 'weather-workflow',
  inputSchema: z.object({city: z.string()}),
  outputSchema: z.object({}),
  steps: [fetchWeatherTask, planActivities],
})
  .parallel([fetchWeatherTask, planActivities])
  .commit()
