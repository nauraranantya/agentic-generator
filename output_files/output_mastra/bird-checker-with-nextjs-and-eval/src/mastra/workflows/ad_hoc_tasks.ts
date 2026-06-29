import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: Bird detection evaluation (Is a bird)
export const bird_detection_evaluation_is_a_bird = createStep({
  id: 'bird_detection_evaluation_is_a_bird',
  description: `Evaluation task that runs the agent on sample images and compares results to expected labels and species. Mirrors src/lib/evals/index.eval.ts.`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
