import { createStep } from '@mastra/core/workflows'

// Ad-hoc Task: task0: spam check
export const task0_spam_check = createStep({
  id: 'task0_spam_check',
  description: `Read the following newsgroup post. If this contains vulgar language reply with STOP . If this is spam reply with STOP.
### NEWGROUP POST:
(see linked resource :discussion_newsgroup_01)`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
// Ad-hoc Task: task4: scoring
export const task4_scoring = createStep({
  id: 'task4_scoring',
  description: `Score the following script: ### SCRIPT: (link to formatted script)`,
  execute: async () => {
    // Ad-hoc task implementation placeholder
    return { status: 'success' };
  }
});
