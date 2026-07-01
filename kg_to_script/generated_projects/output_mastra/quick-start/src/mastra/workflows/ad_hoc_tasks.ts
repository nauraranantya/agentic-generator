import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task_generate_species
export const task_generate_species = createStep({
  id: 'task_generate_species',
  description: `What is the most popular cat species?`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
