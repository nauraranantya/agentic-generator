/**
 * Memory: forgetfulDemoMemory
 *
 * Memory configured with a custom ForgetfulProcessor to redact messages containing keywords like 'name'.
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const forgetfulDemoMemory = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    ForgetfulProcessor: 'keywords = [\'name\']
Processor behavior (preserved as descriptive text):
- Same behavior as repo variant but used for the interactive demo.
- When a message contains any keyword, it is replaced with an assistant message: \'<forgotten>I\'m getting forgetful ...</forgotten>\'.',
    options: 'lastMessages=30; semanticRecall=false',
  }),
})
