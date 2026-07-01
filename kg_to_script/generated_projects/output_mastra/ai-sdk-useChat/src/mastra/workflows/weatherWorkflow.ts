/**
 * Workflow: weather-workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that fetches a weather forecast for a given city, then plans activities based on the forecast.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { planningAgent } from '../agents'

// ── Workflow Steps ──

const fetchWeather = createStep({
  id: 'Fetch Weather',
  description: `Fetches weather forecast for a given city by resolving the city name to coordinates and retrieving daily forecast data. Produces an array of forecast objects { date, maxTemp, minTemp, precipitationChance, condition, location }.`,
  inputSchema: z.object({city: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Summary of behavior:
    // TODO: Implement step logic
    throw new Error('Fetch Weather not implemented yet')
  },
})

const planActivities = createStep({
  id: 'Plan Activities',
  description: `Suggests activities based on the weather forecast. Calls an LLM agent (planningAgent) with the forecast data; receives a streaming text response which is concatenated into the final activities output.`,
  inputSchema: z.object({date: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Based on the following weather forecast for {location}, suggest appropriate activities:
    // This step uses agent: planningAgent
    // const result = await planningAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('Plan Activities not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * weather-workflow
 *
 * Workflow that fetches a weather forecast for a given city, then plans activities based on the forecast.
 */
export const weatherWorkflow = createWorkflow({
  id: 'weather-workflow',
  inputSchema: z.object({city: z.string()}),
  outputSchema: z.object({}),
  steps: [fetchWeather, planActivities],
})
  .parallel([fetchWeather, planActivities])
  .commit()
