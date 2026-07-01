import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task0
export const task0 = createStep({
  id: 'task0',
  description: `Read the following newsgroup post. If this contains vulgar language reply with STOP . If this is spam reply with STOP. ### NEWGROUP POST: {{discussion}}`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task4
export const task4 = createStep({
  id: 'task4',
  description: `Score the following script: ### SCRIPT: {{script}}`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
