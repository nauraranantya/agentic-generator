import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task:fetchWeather
export const task_fetch_weather = createStep({
  id: 'task_fetch_weather',
  description: `Task executed by fetchWeather tool: returns textual forecast for the given city.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task:calculator
export const task_calculator = createStep({
  id: 'task_calculator',
  description: `Calculator tool performs arithmetic operations requested by agent or workflow.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
