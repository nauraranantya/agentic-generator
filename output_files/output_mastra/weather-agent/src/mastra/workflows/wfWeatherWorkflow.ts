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
import { weatherAgent } from '../agents/weatherAgent'

// Import tools used by workflow steps
import { weatherTool } from '../tools/weatherTool'

// ── Workflow Steps ──

const wfStepFetchWeather = createStep({
  id: 'fetch-weather',
  description: `Step that obtains a daily forecast for a city. Fetches daily temperature, precipitationChance, and weather codes and produces an array of forecast objects.`,
  inputSchema: z.object({ city: z.string() }),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // The step expects a trigger containing city name. It will produce daily forecasts for that city.
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('fetch-weather not implemented yet')
  },
})

const wfStepPlanActivities = createStep({
  id: 'wf-step-plan-activities',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Based on the following weather forecast for {location}, suggest appropriate activities:
    // This step uses agent: weatherAgent
    // const result = await weatherAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('wf-step-plan-activities not implemented yet')
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
  inputSchema: z.object({ city: z.string() }),
  outputSchema: z.object({}),
  steps: [wfStepFetchWeather, wfStepPlanActivities],
})
  .then(wfStepFetchWeather)
  .then(wfStepPlanActivities)
  .commit()
