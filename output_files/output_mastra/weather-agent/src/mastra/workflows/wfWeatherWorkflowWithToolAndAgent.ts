/**
 * Workflow: weather-workflow-with-tool-and-agent
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that uses the weather tool to get forecast and then delegates planning to a reporting agent. Input schema: { location: string }
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { weatherTool } from '../tools'

// ── Workflow Steps ──

const wf2StepToolGetWeather = createStep({
  id: 'weather tool call task',
  description: `Task that calls the get-weather tool. Input: { location: string }. Output: simplified current weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task that calls the get-weather tool. Input: { location: string }. Output: simplified current weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location).
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('weather tool call task not implemented yet')
  },
})

const wf2StepMapPrompt = createStep({
  id: 'map forecast to prompt task',
  description: `Takes the tool output and formats a short prompt string for the agent. Produces a single string resource.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Takes the tool output and formats a short prompt string for the agent. Produces a single string resource.
    // TODO: Implement step logic
    throw new Error('map forecast to prompt task not implemented yet')
  },
})

const wf2StepAgentReport = createStep({
  id: 'plan activities / explain weather task',
  description: `Agent task that receives a prompt string and produces an explanatory text and activity suggestions. Uses the agent instruction template that enforces a specific output formatting (emoji sections, weather summary, activities, indoor alternatives, special considerations).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Agent task that receives a prompt string and produces an explanatory text and activity suggestions. Uses the agent instruction template that enforces a specific output formatting (emoji sections, weather summary, activities, indoor alternatives, special considerations).
    // TODO: Implement step logic
    throw new Error('plan activities / explain weather task not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * weather-workflow-with-tool-and-agent
 *
 * Workflow that uses the weather tool to get forecast and then delegates planning to a reporting agent. Input schema: { location: string }
 */
export const wfWeatherWorkflowWithToolAndAgent = createWorkflow({
  id: 'weather-workflow-with-tool-and-agent',
  inputSchema: z.object({location: z.string()}),
  outputSchema: z.object({}),
  steps: [wf2StepToolGetWeather, wf2StepMapPrompt, wf2StepAgentReport],
})
  .parallel([wf2StepToolGetWeather, wf2StepMapPrompt, wf2StepAgentReport])
  .commit()
