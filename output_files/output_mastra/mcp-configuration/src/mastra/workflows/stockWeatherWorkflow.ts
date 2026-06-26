/**
 * Workflow: stock_weather_workflow
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A simple sequential workflow pattern: start -> weather lookup -> stock lookup -> end. The agent orchestrates tool calls to satisfy the incoming user request.
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import tools used by workflow steps
import { weatherTool, stockPriceTool } from '../tools'

// ── Workflow Steps ──

const startStockWeatherStep = createStep({
  id: 'start_stock_weather_step',
  description: `High-level task representing the incoming user prompt that asks for weather in Seattle and the current stock price of Apple (AAPL). This task triggers a workflow that coordinates tool calls to fetch weather and stock data.`,
  inputSchema: z.object({location: z.string()}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Whats the weather in Seattle and what is the current stock price of Apple (AAPL)?
    // TODO: Implement step logic
    throw new Error('start_stock_weather_step not implemented yet')
  },
})

const weatherLookupStep = createStep({
  id: 'weather_lookup_step',
  description: `Task representing the action to obtain current weather for a location. Executed by the Weather Tool which returns a structured JSON-like result with temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the action to obtain current weather for a location. Executed by the Weather Tool which returns a structured JSON-like result with temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location.
    // This step uses tool: weatherTool
    // TODO: Implement step logic
    throw new Error('weather_lookup_step not implemented yet')
  },
})

const stockLookupStep = createStep({
  id: 'stock_lookup_step',
  description: `Task representing the action to obtain the most recent stock close price for a given symbol. Executed by the Stock Price Tool which returns a JSON-like result with symbol and currentPrice.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Task representing the action to obtain the most recent stock close price for a given symbol. Executed by the Stock Price Tool which returns a JSON-like result with symbol and currentPrice.
    // This step uses tool: stockPriceTool
    // TODO: Implement step logic
    throw new Error('stock_lookup_step not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * stock_weather_workflow
 *
 * A simple sequential workflow pattern: start -> weather lookup -> stock lookup -> end. The agent orchestrates tool calls to satisfy the incoming user request.
 */
export const stockWeatherWorkflow = createWorkflow({
  id: 'stock_weather_workflow',
  inputSchema: z.object({A_simple_sequential_workflow_pattern: z.string()}),
  outputSchema: z.object({}),
  steps: [startStockWeatherStep, weatherLookupStep, stockLookupStep],
})
  .then(startStockWeatherStep)
  .then(weatherLookupStep)
  .then(stockLookupStep)
  .commit()
