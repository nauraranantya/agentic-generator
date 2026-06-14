/**
 * Workflow: weather-workflow-with-tool-and-agent
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * Workflow that uses the weather tool to get forecast and then delegates planning to a reporting agent. Input schema: { location: string }
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { weatherReporterAgent } from '../agents/weatherReporterAgent'

// Import tools used by workflow steps
import { weatherTool } from '../tools/weatherTool'

// ── Workflow Steps ──

const wf2StepToolGetWeather = createStep({
  id: 'weatherTool step',
  description: `A step created from the weather tool. Accepts { location } and returns a forecast-like structure (tool output schema).`,
  inputSchema: z.object({ location: z.string() }),
  outputSchema: z.object({ temperature: z.number(), feelsLike: z.number(), humidity: z.number(), windSpeed: z.number(), windGust: z.number(), conditions: z.string(), location: z.string() }),
  execute: async ({ inputData }) => {
    // Task that calls the get-weather tool. Input: { location: string }. Output: simplified current weather object (temperature, feelsLike, humidity, windSpeed, windGust, conditions, location).
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('weatherTool step not implemented yet')
  },
})

const wf2StepMapPrompt = createStep({
  id: 'map prompt',
  description: `Mapping step that converts the previous step's output into a prompt for the agent. Logic: prompt = 'Forecast data: ' + JSON.stringify(inputData) (from tool). This mapping is represented as a prompt template.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Constructs a prompt string for an agent given forecast data. Template: 'Forecast data: ' + JSON.stringify(inputData)
    // TODO: Implement step logic
    throw new Error('map prompt not implemented yet')
  },
})

const wf2StepAgentReport = createStep({
  id: 'weatherReporterAgent step',
  description: `Step executed by a reporting agent that explains the weather and provides activities in reporter style. Input: agent input string.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Agent task that receives a prompt string and produces an explanatory text and activity suggestions. Uses the agent instruction template that enforces a specific output formatting (emoji sections, weather summary, activities, indoor alternatives, special considerations).
    // This step uses agent: weatherReporterAgent
    // const result = await weatherReporterAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('weatherReporterAgent step not implemented yet')
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
  inputSchema: z.object({ location: z.string() }),
  outputSchema: z.object({}),
  steps: [wf2StepToolGetWeather, wf2StepMapPrompt, wf2StepAgentReport],
})
  .then(wf2StepToolGetWeather)
  .then(wf2StepMapPrompt)
  .then(wf2StepAgentReport)
  .commit()
