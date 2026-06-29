/**
 * Workflow: weather-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that fetches weather for a city and plans activities. Input schema: { city: string }. Produces activities text.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

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
  steps: [fetchWeatherTask],
})
  .parallel([fetchWeatherTask])
  .commit()
