"""
SPARQL-based data extractor for AgentO Knowledge Graphs.

Loads .ttl files via rdflib and runs SPARQL queries aligned to
the agentO.ttl ontology (v0.2) to extract agents, tasks, tools,
prompts, and workflow ordering.

Key ontology mappings handled:
  - LLMAgent  (agents, subclass of Tool — filtered out of tool queries)
  - Task      (with performedByAgent, taskPrompt / hasPrompt)
  - Tool      (standalone tools used via agentToolUsage)
  - WorkflowStep / StartStep / EndStep  (ordering via stepOrder)
  - Prompt    (promptInstruction, promptOutputIndicator)
  - Config    (fallback source for goal, expected_output, backstory)
"""

from typing import Dict, List, Any
from rdflib import Graph
import re


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _str(val) -> str:
    """Convert an rdflib term to a stripped Python string."""
    return str(val).strip() if val else ""


def _safe_name(iri: str) -> str:
    """
    Convert an IRI fragment into a valid, lowercase Python identifier.

    Examples:
        "http://…/onto#CustomAgent1"  → "customagent1"
        "http://…/onto#DuckDuckGoTool" → "duckduckgotool"
    """
    if not iri:
        return "unnamed"
    name = iri.split("/")[-1].split("#")[-1]
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    if not name:
        return "unnamed"
    if name[0].isdigit():
        name = f"_{name}"
    return name.lower()


def load_graph(file_path: str) -> Graph:
    """Load an RDF graph from a Turtle (.ttl) or RDF/XML (.rdf) file."""
    g = Graph()
    try:
        g.parse(file_path, format="turtle")
    except Exception as turtle_err:
        try:
            g.parse(file_path, format="xml")
        except Exception:
            # Surface the Turtle error (more informative for .ttl files)
            raise ValueError(
                f"Failed to parse {file_path}: {turtle_err}"
            ) from turtle_err
    return g


# ──────────────────────────────────────────────
# SPARQL Queries  (aligned to agentO.ttl v0.2)
# ──────────────────────────────────────────────

# --- Tools (exclude LLMAgent which is a Tool subclass) ---
TOOLS_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?tool ?title ?label ?desc ?comment
WHERE {
    ?tool a :Tool .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
    OPTIONAL { ?tool dcterms:title ?title }
    OPTIONAL { ?tool rdfs:label   ?label }
    OPTIONAL { ?tool dcterms:description ?desc }
    OPTIONAL { ?tool rdfs:comment ?comment }
}
"""

# --- Agents (LLMAgent) with direct properties ---
AGENTS_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?agent ?agentID ?role ?backstory ?title ?label
                ?goalTitle ?goalDesc
WHERE {
    ?agent a :LLMAgent .
    OPTIONAL { ?agent :agentID ?agentID }
    OPTIONAL { ?agent :agentRole ?role }
    OPTIONAL { ?agent dcterms:description ?backstory }
    OPTIONAL { ?agent dcterms:title ?title }
    OPTIONAL { ?agent rdfs:label   ?label }
    OPTIONAL {
        ?agent :hasAgentGoal ?goal .
        OPTIONAL { ?goal dcterms:title       ?goalTitle }
        OPTIONAL { ?goal dcterms:description ?goalDesc  }
    }
}
"""

# --- Agent → Tool links (agentToolUsage) ---
AGENT_TOOLS_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT DISTINCT ?agent ?tool
WHERE {
    ?agent a :LLMAgent ;
           :agentToolUsage ?tool .
    ?tool  a :Tool .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
}
"""

# --- Fallback: agent goal from Config (configKey = "goal") ---
AGENT_GOAL_CONFIG_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT ?agent ?configValue
WHERE {
    ?agent a :LLMAgent ;
           :hasAgentConfig ?config .
    ?config :configKey   "goal" ;
            :configValue ?configValue .
}
"""

# --- Fallback: agent backstory from Config (configKey = "backstory") ---
AGENT_BACKSTORY_CONFIG_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT ?agent ?configValue
WHERE {
    ?agent a :LLMAgent ;
           :hasAgentConfig ?config .
    ?config :configKey   "backstory" ;
            :configValue ?configValue .
}
"""

# --- Tasks with direct properties ---
TASKS_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?task ?taskTitle ?taskLabel ?taskDesc ?agent
WHERE {
    ?task a :Task .
    OPTIONAL { ?task dcterms:title       ?taskTitle }
    OPTIONAL { ?task rdfs:label          ?taskLabel }
    OPTIONAL { ?task dcterms:description ?taskDesc  }
    OPTIONAL { ?task :performedByAgent   ?agent     }
}
"""

# --- Task prompt data (handles both :taskPrompt and :hasPrompt) ---
TASK_PROMPTS_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT DISTINCT ?task ?promptInstr ?promptOutput
WHERE {
    ?task a :Task .
    {
        { ?task :taskPrompt ?prompt }
        UNION
        { ?task :hasPrompt  ?prompt }
    }
    ?prompt a :Prompt .
    OPTIONAL { ?prompt :promptInstruction    ?promptInstr  }
    OPTIONAL { ?prompt :promptOutputIndicator ?promptOutput }
}
"""

# --- Fallback: task expected_output from Config ---
TASK_EXPECTED_CONFIG_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT ?task ?configValue
WHERE {
    ?task a :Task ;
          :hasAgentConfig ?config .
    ?config :configKey   "expected_output" ;
            :configValue ?configValue .
}
"""

# --- Workflow ordering (WorkflowStep + StartStep + EndStep) ---
WORKFLOW_QUERY = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>

SELECT DISTINCT ?step ?stepOrder ?task
WHERE {
    ?step a ?stepType .
    VALUES ?stepType { :WorkflowStep :StartStep :EndStep }
    ?step :hasAssociatedTask ?task .
    OPTIONAL { ?step :stepOrder ?stepOrder }
}
ORDER BY ?stepOrder
"""


# ──────────────────────────────────────────────
# Extraction Functions
# ──────────────────────────────────────────────

def extract_tools(g: Graph) -> List[Dict[str, Any]]:
    """Extract all standalone Tool instances (excludes LLMAgent)."""
    tools: List[Dict[str, Any]] = []
    seen: set = set()

    for row in g.query(TOOLS_QUERY):
        iri = _str(row.tool)
        if iri in seen:
            continue
        seen.add(iri)
        tools.append({
            "iri": iri,
            "var": _safe_name(iri),
            "title": _str(row.title) or _str(row.label) or _safe_name(iri),
            "description": (
                _str(row.desc) or _str(row.comment) or "CrewAI Tool"
            ),
        })
    return tools


def extract_agents(g: Graph) -> List[Dict[str, Any]]:
    """
    Extract all LLMAgent instances with role, goal, backstory, tools.

    Goal resolution order:
      1. :hasAgentGoal → Goal → dcterms:description
      2. :hasAgentConfig with configKey "goal"
      3. Fall back to agent role
    """
    agents: Dict[str, Dict[str, Any]] = {}

    # ---- Primary agent properties ----
    for row in g.query(AGENTS_QUERY):
        iri = _str(row.agent)
        if iri in agents:
            continue
        agents[iri] = {
            "iri": iri,
            "var": _safe_name(iri),
            "agent_id": _str(row.agentID) or _safe_name(iri),
            "role": _str(row.role) or "",
            "backstory": _str(row.backstory) or "",
            "title": _str(row.title) or _str(row.label) or "",
            "goal": _str(row.goalDesc) or _str(row.goalTitle) or "",
            "tools": [],
        }

    # ---- Agent → Tool links ----
    for row in g.query(AGENT_TOOLS_QUERY):
        iri = _str(row.agent)
        if iri in agents:
            tool_var = _safe_name(_str(row.tool))
            if tool_var not in agents[iri]["tools"]:
                agents[iri]["tools"].append(tool_var)

    # ---- Fallback: goal from Config ----
    for row in g.query(AGENT_GOAL_CONFIG_QUERY):
        iri = _str(row.agent)
        if iri in agents and not agents[iri]["goal"]:
            agents[iri]["goal"] = _str(row.configValue)

    # ---- Fallback: backstory from Config ----
    for row in g.query(AGENT_BACKSTORY_CONFIG_QUERY):
        iri = _str(row.agent)
        if iri in agents and not agents[iri]["backstory"]:
            agents[iri]["backstory"] = _str(row.configValue)

    # ---- Final defaults ----
    for agent in agents.values():
        if not agent["goal"]:
            agent["goal"] = agent["role"] or "Complete assigned tasks"
        if not agent["role"]:
            agent["role"] = "LLM Agent"
        if not agent["backstory"]:
            agent["backstory"] = f"Agent: {agent['agent_id']}"

    return list(agents.values())


def extract_tasks(g: Graph) -> List[Dict[str, Any]]:
    """
    Extract all Task instances with description, expected output, and agent.

    Expected output resolution order:
      1. Prompt → :promptOutputIndicator
      2. Config with configKey "expected_output"
      3. Generated default from task title
    """
    tasks: Dict[str, Dict[str, Any]] = {}

    # ---- Primary task properties ----
    for row in g.query(TASKS_QUERY):
        iri = _str(row.task)
        if iri in tasks:
            continue
        tasks[iri] = {
            "iri": iri,
            "var": _safe_name(iri),
            "title": _str(row.taskTitle) or _str(row.taskLabel) or _safe_name(iri),
            "description": _str(row.taskDesc) or "",
            "agent_var": _safe_name(_str(row.agent)) if row.agent else "",
            "expected_output": "",
        }

    # ---- Prompt data (taskPrompt / hasPrompt) ----
    for row in g.query(TASK_PROMPTS_QUERY):
        iri = _str(row.task)
        if iri not in tasks:
            continue
        if row.promptOutput and not tasks[iri]["expected_output"]:
            tasks[iri]["expected_output"] = _str(row.promptOutput)
        # Use prompt instruction as description fallback
        if row.promptInstr and not tasks[iri]["description"]:
            tasks[iri]["description"] = _str(row.promptInstr)

    # ---- Fallback: expected output from Config ----
    for row in g.query(TASK_EXPECTED_CONFIG_QUERY):
        iri = _str(row.task)
        if iri in tasks and not tasks[iri]["expected_output"]:
            tasks[iri]["expected_output"] = _str(row.configValue)

    # ---- Final defaults ----
    for task in tasks.values():
        if not task["expected_output"]:
            task["expected_output"] = f"Completed: {task['title']}"
        if not task["description"]:
            task["description"] = task["title"]

    return list(tasks.values())


def extract_workflow_order(g: Graph) -> List[str]:
    """Extract ordered task IRIs from WorkflowStep instances."""
    ordered: List[str] = []
    for row in g.query(WORKFLOW_QUERY):
        iri = _str(row.task)
        if iri and iri not in ordered:
            ordered.append(iri)
    return ordered


# ──────────────────────────────────────────────
# Public API
# ──────────────────────────────────────────────

def extract_all(file_path: str) -> Dict[str, Any]:
    """
    Full extraction pipeline for a single KG file.

    Returns:
        dict with keys: tools, agents, tasks
        (tasks are ordered by workflow steps when available)
    """
    g = load_graph(file_path)

    tools = extract_tools(g)
    agents = extract_agents(g)
    tasks = extract_tasks(g)

    # Reorder tasks according to workflow step ordering
    ordered_iris = extract_workflow_order(g)
    if ordered_iris:
        task_map = {t["iri"]: t for t in tasks}
        reordered = []
        for iri in ordered_iris:
            if iri in task_map:
                reordered.append(task_map.pop(iri))
        # Append remaining tasks not covered by workflow
        reordered.extend(task_map.values())
        tasks = reordered

    print(
        f"  [Extracted] {len(agents)} agents, "
        f"{len(tasks)} tasks, {len(tools)} tools"
    )
    return {"tools": tools, "agents": agents, "tasks": tasks}
