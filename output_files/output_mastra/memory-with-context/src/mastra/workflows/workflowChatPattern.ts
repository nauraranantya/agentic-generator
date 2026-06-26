/**
 * Workflow: workflow_chat_pattern
 *
 * Auto-generated from AgentO Knowledge Graph
 *
 * A workflow pattern that models the interactive chat loop: Start -> Receive user input -> Agent generate streaming response -> Repeat -> End
 */

import { createWorkflow, createStep } from '@mastra/core/workflows'
import { z } from 'zod'

// Import agents used by workflow steps
import { memoryAgent } from '../agents'

// ── Workflow Steps ──

const wsStartChat = createStep({
  id: 'ws_start_chat',
  description: `On session start the program sends a system-role message; uses prompt_system_firstChat if isFirstChat, otherwise prompt_system_returningChat. The timestamp is inserted at runtime.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Chat with user started now {{ISO_TIMESTAMP}}. Don't mention this message. This means some time has passed between this message and the one before. The user left and came back again. Say something to start the conversation up again.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('ws_start_chat not implemented yet')
  },
})

const wsReceiveUserInput = createStep({
  id: 'ws_receive_user_input',
  description: `A blocking read from a human input channel; in code this is achieved by Readline and awaiting user's input, then the input is forwarded to the agent.stream call.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // A blocking read from a human input channel; in code this is achieved by Readline and awaiting user's input, then the input is forwarded to the agent.stream call.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('ws_receive_user_input not implemented yet')
  },
})

const wsAgentGenerateResponse = createStep({
  id: 'ws_agent_generate_response',
  description: `Agent processes the user's message, streams text output. During streaming the implementation masks two tag sections: 'think' (internal chain-of-thought-like output) and 'working_memory' (memory saving operations). Spinners (status indicators) are displayed while sections stream; upon end spinners succeed and input reading resumes. The stream also interacts with the Memory component for saving/retrieving conversation context.`,
  inputSchema: z.object({}),
  outputSchema: z.object({}),
  execute: async ({ inputData }) => {
    // Agent processes the user's message, streams text output. During streaming the implementation masks two tag sections: 'think' (internal chain-of-thought-like output) and 'working_memory' (memory saving operations). Spinners (status indicators) are displayed while sections stream; upon end spinners succeed and input reading resumes. The stream also interacts with the Memory component for saving/retrieving conversation context.
    // This step uses agent: memoryAgent
    // const result = await memoryAgent.generate('...')
    // TODO: Implement step logic
    throw new Error('ws_agent_generate_response not implemented yet')
  },
})

// ── Workflow Definition ──

/**
 * workflow_chat_pattern
 *
 * A workflow pattern that models the interactive chat loop: Start -> Receive user input -> Agent generate streaming response -> Repeat -> End
 */
export const workflowChatPattern = createWorkflow({
  id: 'workflow_chat_pattern',
  inputSchema: z.object({A_workflow_pattern_that_models_the_interactive_chat_loop: z.string()}),
  outputSchema: z.object({}),
  steps: [wsStartChat, wsReceiveUserInput, wsAgentGenerateResponse],
})
  .then(wsStartChat)
  .then(wsReceiveUserInput)
  .then(wsAgentGenerateResponse)
  .commit()
