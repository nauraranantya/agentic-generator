/**
 * Tool: get-weather
 * 
 * Auto-generated from AgentO Knowledge Graph
 * 
 * Get current weather for a location.  Behavior summary: - Input: { location: string } (city name) - Execution:   1. Call geocoding API to resolve location -> latitude, longitude, name.   2. Call weather API with latitude & longitude to get current and hourly weather.   3. Map numeric weather_code to human-readable condition (mapping preserved in description).   4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location. - Errors: throws when location not found.
 */

import { createTool } from '@mastra/core/tools'
import { z } from 'zod'

/**
 * get-weather
 * 
 * Implementation: Get current weather for a location.  Behavior summary: - Input: { location: string } (city name) - Execution:   1. Call geocoding API to resolve location -> latitude, longitude, name.   2. Call weather API with latitude & longitude to get current and hourly weather.   3. Map numeric weather_code to human-readable condition (mapping preserved in description).   4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location. - Errors: throws when location not found.
 */
export const weatherTool = createTool({
  id: 'get-weather',
  description: `Get current weather for a location.

Behavior summary:
- Input: { location: string } (city name)
- Execution:
  1. Call geocoding API to resolve location -> latitude, longitude, name.
  2. Call weather API with latitude & longitude to get current and hourly weather.
  3. Map numeric weather_code to human-readable condition (mapping preserved in description).
  4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location.
- Errors: throws when location not found.`,
  inputSchema: z.object({location: z.string()}),
  outputSchema: z.object({temperature: z.string(), feelsLike: z.string(), humidity: z.string(), windSpeed: z.string(), windGust: z.string(), conditions: z.string(), location: z.string()}),
  execute: async ({ inputData }) => {
    // TODO: Implement tool logic
    // 
    // Description: Get current weather for a location.  Behavior summary: - Input: { location: string } (city name) - Execution:   1. Call geocoding API to resolve location -> latitude, longitude, name.   2. Call weather API with latitude & longitude to get current and hourly weather.   3. Map numeric weather_code to human-readable condition (mapping preserved in description).   4. Return normalized object with keys: temperature, feelsLike, humidity, windSpeed, windGust, conditions, location. - Errors: throws when location not found.
    // Configurations:
    //   - inputSchema: {"location": "string (city name)"}
    //   - outputSchema: {"temperature": "number", "feelsLike": "number", "humidity": "number", "windSpeed": "number", "windGust": "number", "conditions": "string", "location": "string"}
    // 
    // Implementation should:
    // 1. Use inputData according to inputSchema
    // 2. Perform the tool's logic
    // 3. Return result matching outputSchema
    
    throw new Error('Tool get-weather not implemented yet')
  },
})
