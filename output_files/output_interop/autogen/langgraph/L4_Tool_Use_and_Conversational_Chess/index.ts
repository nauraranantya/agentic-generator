import { ChatOpenAI } from "@langchain/openai";
import { Annotation, START, END, StateGraph } from "@langchain/langgraph";
import { tool } from "@langchain/core/tools";
import { z } from "zod";

const ChessplayersteamAnnotation = Annotation.Root({
  messages: Annotation<any[]>({
    reducer: (_, next) => next,
    default: () => [],
  }),
});

// Tool: board_proxy
const board_proxy = tool(
  async () => {
    return "Result of board_proxy";
  },
  {
    name: "board_proxy",
    description: "A conversational proxy agent that executes board-related tools (get_legal_moves, make_move). Created with llm_config=False in code; it receives tool execution requests and applies them to the ChessBoard resource.",
    schema: z.object({}),
  }
);
// Tool: tool_get_legal_moves
const tool_get_legal_moves = tool(
  async () => {
    return "Result of tool_get_legal_moves";
  },
  {
    name: "tool_get_legal_moves",
    description: "Registered tool name: 'get_legal_moves'. Description: Get legal moves. Returns a comma-separated list of legal moves in UCI format. In code, returns: 'Possible moves are: ' + ','.join([str(move) for move in board.legal_moves]). This tool reads the ChessBoard resource and produces a LegalMovesList resource.",
    schema: z.object({}),
  }
);
// Tool: tool_make_move
const tool_make_move = tool(
  async () => {
    return "Result of tool_make_move";
  },
  {
    name: "tool_make_move",
    description: "Registered tool name: 'make_move'. Description: apply a move in UCI format to the ChessBoard. Parameters: move (string, UCI). Behavior summary preserved: (1) convert the provided string to a chess.Move, push the move to the board state, set a made_move flag to True, display the board (SVG), identify the moved piece and return a human-readable message 'Moved <PieceName> (<PieceSymbol>) from <from_square> to <to_square>.' This tool reads and updates the ChessBoard resource and causes a termination predicate (is_termination_msg) to become true for nested chat closing.",
    schema: z.object({}),
  }
);



/**
 * Node: taskInitiateChatBlackWhite
 * Agent: player_white
 */
async function taskInitiateChatBlackWhite(state: typeof ChessplayersteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a white." +
        "\nNode: taskInitiateChatBlackWhite",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskMakeMove
 * Agent: player_white
 */
async function taskMakeMove(state: typeof ChessplayersteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a white." +
        "\nNode: taskMakeMove",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

/**
 * Node: taskMakeMove
 * Agent: player_white
 */
async function taskMakeMove(state: typeof ChessplayersteamAnnotation.State) {
  const model = new ChatOpenAI({ model: "gpt-4o-mini" });
  const response = await model.invoke([
    {
      role: "system",
      content:
        "You are a white." +
        "\nNode: taskMakeMove",
    },
    ...state.messages,
  ]);
  return { messages: [response] };
}

const workflow = new StateGraph(ChessplayersteamAnnotation)
  .addNode("taskInitiateChatBlackWhite", taskInitiateChatBlackWhite)
  .addNode("taskMakeMove", taskMakeMove)
  .addNode("taskMakeMove", taskMakeMove)
  .addEdge(START, "taskInitiateChatBlackWhite")
  .addEdge("taskInitiateChatBlackWhite", "taskMakeMove")
  .addEdge("taskMakeMove", "taskMakeMove")
  .addEdge("taskMakeMove", "taskMakeMove")
;

export const graph = workflow.compile();
graph.name = "Chessplayersteam";
// Workflow: workflow_pattern_conversational_chess
// Workflow: Conversational Chess Workflow Pattern
