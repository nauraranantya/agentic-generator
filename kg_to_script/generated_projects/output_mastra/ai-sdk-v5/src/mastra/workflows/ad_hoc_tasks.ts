import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Fetch current weather
export const fetch_current_weather = createStep({
  id: 'fetch_current_weather',
  description: `Task to fetch current weather for a specified location. Implemented by invoking the 'get-weather' tool. The agent will ask the user for a location if not provided.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: weather-agent participation placeholder
export const weather_agent_participation_placeholder = createStep({
  id: 'weather_agent_participation_placeholder',
  description: `A provenance-style record that the agent participates in the fetch current weather task.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
