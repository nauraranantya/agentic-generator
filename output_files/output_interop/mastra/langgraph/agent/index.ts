import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const MastraSystemAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: cooking_tool
const cooking_tool = tool(
  async () => {
    return "Result of cooking_tool";
  },
  {
    name: "cooking_tool",
    description: "Tool ID: cooking-tool
    Description: Used to cook given an ingredient
    Input schema (zod): { ingredient: string }
    Behavior: Simulated long-running operation (sleep ~5000ms). Logs the ingredient and returns 'My tool result'.
    Note: When available, context.agent.toolCallId is logged by the tool for tracing.",
    schema: z.object({}),
  }
);
// Tool: weather_info_tool
const weather_info_tool = tool(
  async () => {
    return "Result of weather_info_tool";
  },
  {
    name: "weather_info_tool",
    description: "Tool ID: weather-info
    Description: Fetches the current weather information for a given city.
    Input schema: { city: string }
    Returns: an object with city, weather, temperature_celsius, temperature_fahrenheit, humidity, wind.",
    schema: z.object({}),
  }
);
// Tool: calculator_tool
const calculator_tool = tool(
  async () => {
    return "Result of calculator_tool";
  },
  {
    name: "calculator_tool",
    description: "Tool ID: calculator
    Description: Performs basic arithmetic operations (add, subtract).
    Input schema: { num1: number, num2: number, operation: 'add'|'subtract' }
    Output: numeric result.",
    schema: z.object({}),
  }
);
// Tool: fetch_weather_tool
const fetch_weather_tool = tool(
  async () => {
    return "Result of fetch_weather_tool";
  },
  {
    name: "fetch_weather_tool",
    description: "Tool ID: fetchWeather
    Description: Simulated forecast for a city. Uses a simple mapping from city to temperature string.
    Input schema: { city: string }
    Output: string describing weather (e.g., 'The weather in X is 20°C and sunny.').",
    schema: z.object({}),
  }
);
// Tool: string_utils_tool
const string_utils_tool = tool(
  async () => {
    return "Result of string_utils_tool";
  },
  {
    name: "string_utils_tool",
    description: "Tool ID: stringUtils
    Description: Performs utility operations on strings (uppercase, reverse).
    Input schema: { text: string, action: 'uppercase'|'reverse' }
    Output: transformed text.
    Note: Source code had a small bug (used inputData variable in execute); semantic behavior preserved here.",
    schema: z.object({}),
  }
);
// Tool: greet_user_tool
const greet_user_tool = tool(
  async () => {
    return "Result of greet_user_tool";
  },
  {
    name: "greet_user_tool",
    description: "Tool ID: greetUser
    Description: Generates a personalized greeting.
    Input schema: { name: string }
    Output: greeting string 'Hello, {name}! Welcome to the MCP server.'",
    schema: z.object({}),
  }
);
// Tool: collect_contact_info_tool
const collect_contact_info_tool = tool(
  async () => {
    return "Result of collect_contact_info_tool";
  },
  {
    name: "collect_contact_info_tool",
    description: "Tool ID: collectContactInfo
    Description: Collects user contact information through elicitation (interactive).
    Input schema: { reason?: string }
    Behavior:
      - Calls MCP elicitation session to send a request with JSON schema (name, email, phone).
      - Waits for user response via an elicitation handler. Interprets actions: accept/reject/cancel.
      - Returns a string summarizing collection outcome or an error.
    Elicitation requestedSchema (JSON):
      {
        type: 'object',
        properties: {
          name: { type: 'string', title: 'Full Name', description: 'Your full name' },
          email: { type: 'string', title: 'Email Address', description: 'Your email address', format: 'email' },
          phone: { type: 'string', title: 'Phone Number', description: 'Your phone number (optional)' }
        },
        required: ['name','email']
      }",
    schema: z.object({}),
  }
);



/**
 * Node: taskMyStep
 * Agent: chef_agent
 */
async function taskMyStep(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskMyStep",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskMyStep2
 * Agent: chef_agent
 */
async function taskMyStep2(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskMyStep2",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAddLetter
 * Agent: chef_model_v2_agent
 */
async function taskAddLetter(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskAddLetter",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAddLetterB
 * Agent: chef_model_v2_agent
 */
async function taskAddLetterB(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskAddLetterB",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAddLetterC
 * Agent: chef_model_v2_agent
 */
async function taskAddLetterC(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskAddLetterC",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskAddLetterWithCount
 * Agent: chef_model_v2_agent
 */
async function taskAddLetterWithCount(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskAddLetterWithCount",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskSuspendResume
 * Agent: chef_agent
 */
async function taskSuspendResume(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskSuspendResume",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskShortText
 * Agent: chef_model_v2_agent
 */
async function taskShortText(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskShortText",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskLongText
 * Agent: chef_model_v2_agent
 */
async function taskLongText(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskLongText",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskNestedTextProcessor
 * Agent: chef_model_v2_agent
 */
async function taskNestedTextProcessor(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskNestedTextProcessor",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskFinalStep
 * Agent: chef_agent
 */
async function taskFinalStep(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskFinalStep",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepOne
 * Agent: dynamic_agent
 */
async function taskStepOne(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskStepOne",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepTwo
 * Agent: dynamic_agent
 */
async function taskStepTwo(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskStepTwo",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepThree
 * Agent: dynamic_agent
 */
async function taskStepThree(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskStepThree",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskStepFour
 * Agent: dynamic_agent
 */
async function taskStepFour(state: typeof MastraSystemAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a LLM Agent." +
        "\\nNode: taskStepFour",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(MastraSystemAnnotation)
  .addNode("taskMyStep", taskMyStep)
  .addNode("taskMyStep2", taskMyStep2)
  .addNode("taskAddLetter", taskAddLetter)
  .addNode("taskAddLetterB", taskAddLetterB)
  .addNode("taskAddLetterC", taskAddLetterC)
  .addNode("taskAddLetterWithCount", taskAddLetterWithCount)
  .addNode("taskSuspendResume", taskSuspendResume)
  .addNode("taskShortText", taskShortText)
  .addNode("taskLongText", taskLongText)
  .addNode("taskNestedTextProcessor", taskNestedTextProcessor)
  .addNode("taskFinalStep", taskFinalStep)
  .addNode("taskStepOne", taskStepOne)
  .addNode("taskStepTwo", taskStepTwo)
  .addNode("taskStepThree", taskStepThree)
  .addNode("taskStepFour", taskStepFour)
  .addEdge(START, "taskMyStep")
  .addEdge("taskMyStep", "taskMyStep2")
  .addEdge("taskMyStep2", "taskAddLetter")
  .addEdge("taskAddLetter", "taskAddLetterB")
  .addEdge("taskAddLetterB", "taskAddLetterC")
  .addEdge("taskAddLetterC", "taskAddLetterWithCount")
  .addEdge("taskAddLetterWithCount", "taskSuspendResume")
  .addEdge("taskSuspendResume", "taskShortText")
  .addEdge("taskShortText", "taskLongText")
  .addEdge("taskLongText", "taskNestedTextProcessor")
  .addEdge("taskNestedTextProcessor", "taskFinalStep")
  .addEdge("taskFinalStep", "taskStepOne")
  .addEdge("taskStepOne", "taskStepTwo")
  .addEdge("taskStepTwo", "taskStepThree")
  .addEdge("taskStepThree", "taskStepFour")
  .addEdge("taskStepFour", END)
;

export const graph = workflow.compile();
graph.name = "MastraSystem";
// Workflow: recipe_maker_workflow
// Workflow: recipe-maker
// Workflow: less_complex_workflow
// Workflow: lessComplexWorkflow
// Workflow: nested_workflow
// Workflow: data-processing
// Workflow: my_workflow_x
// Workflow: my-workflow
