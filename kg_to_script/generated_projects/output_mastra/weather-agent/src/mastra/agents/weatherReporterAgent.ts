/**
 * Agent: Weather Explainer Agent
 * ID: weatherExplainerAgent
 * 
 * Auto-generated from AgentO Knowledge Graph
 */

import { Agent } from '@mastra/core/agent'

/**
 * Weather Explainer Agent
 * 
 * Instructions:
 * You are a weather explainer. You have access to input that will help you get weather-specific activities for any city.  The tool uses agents to plan the activities, you just need to provide the city. Explain the weather report like a weather reporter.
 */
export const weatherReporterAgent = new Agent({
  id: `weatherExplainerAgent`,
  name: `Weather Explainer Agent`,
  instructions: `You are a weather explainer. You have access to input that will help you get weather-specific activities for any city. 
The tool uses agents to plan the activities, you just need to provide the city. Explain the weather report like a weather reporter.`,
  model: 'openai/gpt-4o',
})
