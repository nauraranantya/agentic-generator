/**
 * Workflow: Stock + Weather Workflow Pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple sequential workflow pattern: start -> weather lookup -> stock lookup -> end. The agent orchestrates tool calls to satisfy the incoming user request.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { weatherTool } from '../tools/weatherTool'
import { stockPriceTool } from '../tools/stockPriceTool'

// ── Workflow Steps ──

const startStockWeatherStep = createStep({
  id: 'Start Step',
  description: `Initial step which receives or recognizes the user prompt and decides required sub-tasks (weather and stock lookups).`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Whats the weather in Seattle and what is the current stock price of Apple (AAPL)?
    // TODO: Implement step logic
    throw new Error('Start Step not implemented yet')
  },
})

const weatherLookupStep = createStep({
  id: 'Weather Lookup Step',
  description: `Step that triggers the weather tool to fetch current weather for specified location.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the action to obtain current weather for a location. Executed by the Weather Tool which returns a structured JSON-like result with temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location.
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('Weather Lookup Step not implemented yet')
  },
})

const stockLookupStep = createStep({
  id: 'Stock Lookup Step',
  description: `Step that triggers the stock price tool to fetch the stock price for the specified symbol.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the action to obtain the most recent stock close price for a given symbol. Executed by the Stock Price Tool which returns a JSON-like result with symbol and currentPrice.
    // This step uses tool: stockPriceTool
    // TODO: Implement step logic
    throw new Error('Stock Lookup Step not implemented yet')
  },
})

const endStockWeatherStep = createStep({
  id: 'End Step',
  description: `Completion step where the agent composes results from the produced resources and crafts the final reply to the user.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Completion step where the agent composes results from the produced resources and crafts the final reply to the user.
    // TODO: Implement step logic
    throw new Error('End Step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * Stock + Weather Workflow Pattern
 *
 * A simple sequential workflow pattern: start -> weather lookup -> stock lookup -> end. The agent orchestrates tool calls to satisfy the incoming user request.
 */
export const stockWeatherWorkflow = createWorkflow({
  id: 'Stock + Weather Workflow Pattern',
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  steps: [startStockWeatherStep, weatherLookupStep, stockLookupStep, endStockWeatherStep],
})
  .then(startStockWeatherStep)
  .then(weatherLookupStep)
  .then(stockLookupStep)
  .then(endStockWeatherStep)
  .commit()
