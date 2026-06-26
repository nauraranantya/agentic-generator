/**
 * Tool: weatherTool
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * weatherTool
 * 
 * Implementation: Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).
 */
export const weatherTool = createTool({
  id: 'weatherTool',
  description: `Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).`,
  inputSchema: z.object({location: z.string()}),
  outputSchema: z.object({}),  // TODO: Define output schema
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Tool exposing 'getWeather' capability. It resolves a location via a geocoding service, calls an external weather API (open-meteo) to get current conditions and returns a JSON structure containing temperature, feelsLike, humidity, windSpeed, windGust, conditions, and location. This tool is exposed over an SSE-backed server endpoint at http://localhost:8080/sse in the example environment. The tool expects a 'location' string (city name).
    // Configurations:
    //   - tool.name: getWeather
    //   - tool.name: Get current weather for a location
    //   - tool.name: { "location": "string (city name)" }
    //   - tool.name: SSE (server endpoint at http://localhost:8080/sse)
    //   - tool.description: getWeather
    //   - tool.description: Get current weather for a location
    //   - tool.description: { "location": "string (city name)" }
    //   - tool.description: SSE (server endpoint at http://localhost:8080/sse)
    //   - inputSchema: getWeather
    //   - inputSchema: Get current weather for a location
    //   - inputSchema: { "location": "string (city name)" }
    //   - inputSchema: SSE (server endpoint at http://localhost:8080/sse)
    //   - exposure: getWeather
    //   - exposure: Get current weather for a location
    //   - exposure: { "location": "string (city name)" }
    //   - exposure: SSE (server endpoint at http://localhost:8080/sse)
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool weatherTool not implemented yet')
  },
})
