import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task_generate_most_popular_species
export const task_generate_most_popular_species = createStep({
  id: 'task_generate_most_popular_species',
  description: `Task where the agent is asked 'What is the most popular cat species?' and expected to return a JSON object matching the output schema { species: string }.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
