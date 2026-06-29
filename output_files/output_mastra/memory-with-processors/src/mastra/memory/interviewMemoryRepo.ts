/**
 * Memory: interviewMemoryRepo
 *
 * Memory configured to filter tool calls and forget keywords (repo example).
 *
 * Auto-generated from AgentO Knowledge Graph
 * Storage backend: libsql
 */

import { Memory } from '@mastra/memory'
import { LibSQLStore } from '@mastra/libsql'


export const interviewMemoryRepo = new Memory({
  storage: new LibSQLStore({
    id: 'mastra-libsql-store',
    ToolCallFilter: 'filters out all tool calls from stored memory (removes tool-call events from conversation history)',
    ForgetfulProcessor: 'keywords = [\'name\']
Processor behavior (preserved as descriptive text):
- For messages with role \'assistant\' or \'user\', inspect content.
- If the content contains any of the keywords (case-insensitive), replace the message with a single assistant message containing <forgotten> wrapper text indicating forgetting.
- Purpose: demo a processor that purposely forgets specific sensitive keywords (e.g., \'name\').',
    options: 'lastMessages=30; semanticRecall=false',
  }),
})
