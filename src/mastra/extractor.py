"""
Layer 1 – SPARQL-based Data Extraction for Mastra AI

Loads a Mastra KG (.ttl) file via rdflib, runs SPARQL queries aligned
to the agentO ontology, and populates Pydantic IR models (Layer 2).

Extraction strategy:
  1. Team / System metadata
  2. LanguageModel individuals  
  3. Tool individuals (with schema parsing from descriptions + storage-tool detection)
  4. Agent individuals — Mastra pattern:
       instructions → :agentPrompt → :promptInstruction
       model        → :useLanguageModel → model router string
       memory       → :hasKnowledge → :Memory
  5. Workflow patterns (Milestone 2)
  6. Memory configs (Milestone 3)
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Set, Tuple

from rdflib import Graph

from .models import (
    ConfigModel,
    ControlFlowType,
    LanguageModelModel,
    MastraAgentModel,
    MastraProject,
    MastraToolModel,
    MemoryModel,
    StepModel,
    ToolConfigModel,
    WorkflowModel,
)


# ─────────────────────── Helpers ───────────────────────

def _s(val: Any) -> str:
    """Convert rdflib term to stripped str."""
    return str(val).strip() if val else ""


def _safe_var(iri: str, naming_style: str = "camel") -> str:
    """
    IRI fragment → valid TypeScript variable name.
    
    Args:
        iri: Full IRI or fragment
        naming_style: 'camel' for camelCase (default), 'kebab' for kebab-case
    
    Examples:
        camel: "http://…/onto#CatOneAgent" → "catOneAgent"
        kebab: "http://…/onto#QuickStart" → "quick-start"
    """
    if not iri:
        return "unnamed"
    
    # Extract fragment
    name = iri.split("/")[-1].split("#")[-1]
    
    # Clean non-alphanumeric
    name = re.sub(r"[^a-zA-Z0-9_-]", "", name)
    
    if naming_style == "kebab":
        # Insert hyphens before uppercase runs: "QuickStart" → "Quick-Start"
        name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"-\1", name)
        name = re.sub(r"(?<=[A-Z])([A-Z][a-z])", r"-\1", name)
        name = re.sub(r"[-_]+", "-", name).strip("-").lower()
    else:  # camelCase
        # Insert underscores first
        name = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name)
        name = re.sub(r"(?<=[A-Z])([A-Z][a-z])", r"_\1", name)
        name = re.sub(r"[_-]+", "_", name).strip("_")
        
        # Convert to camelCase
        parts = name.split("_")
        if parts:
            name = parts[0].lower() + "".join(p.capitalize() for p in parts[1:])
    
    if not name:
        return "unnamed"
    
    # Ensure starts with letter (TypeScript requirement)
    if name[0].isdigit():
        name = f"_{name}" if naming_style == "camel" else f"item-{name}"
    
    return name


def _pascal_case(s: str) -> str:
    """Convert string to PascalCase: 'quick-start' → 'QuickStart'."""
    s = s.replace("-", "_").replace(" ", "_")
    return "".join(w.capitalize() for w in s.split("_"))


def load_graph(file_path: str) -> Graph:
    """Parse a Turtle (.ttl) file into an rdflib Graph."""
    g = Graph()
    g.parse(file_path, format="turtle")
    return g


# ─────────────────────── SPARQL Queries ───────────────────────

PREFIXES = """\
PREFIX : <http://www.w3id.org/agentic-ai/onto#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
PREFIX beam:    <http://w3id.org/beam/core#>
"""

# ── Team / System ──

TEAM_QUERY = PREFIXES + """
SELECT ?team ?label ?title ?desc
WHERE {
    ?team a :Team .
    OPTIONAL { ?team rdfs:label ?label }
    OPTIONAL { ?team dcterms:title ?title }
    OPTIONAL { ?team dcterms:description ?desc }
}
"""

SYSTEM_CONFIG_QUERY = PREFIXES + """
SELECT ?team ?key ?value
WHERE {
    ?team a :Team ;
          :hasSystemConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
}
"""

# ── Language Models ──

LLM_QUERY = PREFIXES + """
SELECT DISTINCT ?lm ?label ?title ?desc
WHERE {
    ?lm a :LanguageModel .
    OPTIONAL { ?lm rdfs:label ?label }
    OPTIONAL { ?lm dcterms:title ?title }
    OPTIONAL { ?lm dcterms:description ?desc }
}
"""

# ── Tools ──

TOOLS_QUERY = PREFIXES + """
SELECT DISTINCT ?tool ?label ?title ?desc ?comment
WHERE {
    ?tool a :Tool .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
    OPTIONAL { ?tool rdfs:label ?label }
    OPTIONAL { ?tool dcterms:title ?title }
    OPTIONAL { ?tool dcterms:description ?desc }
    OPTIONAL { ?tool rdfs:comment ?comment }
}
"""

TOOL_CONFIGS_QUERY = PREFIXES + """
SELECT ?tool ?key ?value
WHERE {
    ?tool a :Tool ;
          :hasToolConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
}
"""

# ── Agents ──

# Mastra agents use :agentPrompt → Prompt → :promptInstruction (not role/goal/backstory)
AGENTS_QUERY = PREFIXES + """
SELECT DISTINCT ?agent ?agentID ?label ?title ?desc
WHERE {
    ?agent a :LLMAgent .
    OPTIONAL { ?agent :agentID ?agentID }
    OPTIONAL { ?agent rdfs:label ?label }
    OPTIONAL { ?agent dcterms:title ?title }
    OPTIONAL { ?agent dcterms:description ?desc }
}
"""

AGENT_INSTRUCTIONS_QUERY = PREFIXES + """
SELECT ?agent ?instruction
WHERE {
    ?agent a :LLMAgent ;
           :agentPrompt ?prompt .
    ?prompt :promptInstruction ?instruction .
}
"""

AGENT_TOOLS_QUERY = PREFIXES + """
SELECT DISTINCT ?agent ?tool
WHERE {
    ?agent a :LLMAgent ;
           :agentToolUsage ?tool .
    ?tool a :Tool .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
}
"""

AGENT_LLM_QUERY = PREFIXES + """
SELECT DISTINCT ?agent ?lm
WHERE {
    ?agent a :LLMAgent ;
           :useLanguageModel ?lm .
}
"""

AGENT_MEMORY_QUERY = PREFIXES + """
SELECT DISTINCT ?agent ?mem
WHERE {
    ?agent a :LLMAgent ;
           :hasKnowledge ?mem .
    ?mem a :Memory .
}
"""

AGENT_CONFIGS_QUERY = PREFIXES + """
SELECT ?agent ?key ?value
WHERE {
    ?agent a :LLMAgent ;
           :hasAgentConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
}
"""

# ── Workflows ──

WORKFLOW_PATTERN_QUERY = PREFIXES + """
SELECT ?wp ?label ?title ?desc
WHERE {
    ?wp a :WorkflowPattern .
    OPTIONAL { ?wp rdfs:label ?label }
    OPTIONAL { ?wp dcterms:title ?title }
    OPTIONAL { ?wp dcterms:description ?desc }
}
"""

WORKFLOW_STEPS_QUERY = PREFIXES + """
SELECT ?wp ?step
WHERE {
    ?wp a :WorkflowPattern ;
        :hasWorkflowStep ?step .
}
"""

# Also catch :StartStep, :EndStep (subtypes used in some KGs)
STEP_DETAILS_QUERY = PREFIXES + """
SELECT ?step ?label ?title ?desc ?order
WHERE {
    { ?step a :WorkflowStep } UNION { ?step a :StartStep } UNION { ?step a :EndStep }
    OPTIONAL { ?step rdfs:label ?label }
    OPTIONAL { ?step dcterms:title ?title }
    OPTIONAL { ?step dcterms:description ?desc }
    OPTIONAL { ?step :stepOrder ?order }
}
"""

STEP_TASK_QUERY = PREFIXES + """
SELECT ?step ?task
WHERE {
    ?step :hasAssociatedTask ?task .
}
"""

# Step-level prompt schemas via Task → Prompt
STEP_SCHEMA_QUERY = PREFIXES + """
SELECT ?task ?inputData ?outputIndicator ?instruction ?context
WHERE {
    ?task a :Task .
    {
        { ?task :taskPrompt ?prompt }
        UNION
        { ?task :hasPrompt ?prompt }
    }
    OPTIONAL { ?prompt :promptInputData ?inputData }
    OPTIONAL { ?prompt :promptOutputIndicator ?outputIndicator }
    OPTIONAL { ?prompt :promptInstruction ?instruction }
    OPTIONAL { ?prompt :promptContext ?context }
}
"""

# Step-level prompt schemas via WorkflowStep → :taskPrompt (direct link)
STEP_DIRECT_PROMPT_QUERY = PREFIXES + """
SELECT ?step ?inputData ?outputIndicator ?instruction
WHERE {
    ?step :taskPrompt ?prompt .
    OPTIONAL { ?prompt :promptInputData ?inputData }
    OPTIONAL { ?prompt :promptOutputIndicator ?outputIndicator }
    OPTIONAL { ?prompt :promptInstruction ?instruction }
}
"""

# Step-level schemas from Config individuals (used in inline-steps KGs)
STEP_CONFIG_SCHEMA_QUERY = PREFIXES + """
SELECT ?task ?key ?value
WHERE {
    ?task a :Task ;
          :hasConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
    FILTER(CONTAINS(LCASE(?key), "schema"))
}
"""

# Step → Agent association (via Task :performedByAgent)
STEP_TASK_AGENT_QUERY = PREFIXES + """
SELECT ?task ?agent
WHERE {
    ?task a :Task ;
          :performedByAgent ?agent .
    ?agent a :LLMAgent .
}
"""

# Step → Agent association (directly on WorkflowStep :performedByAgent)
STEP_DIRECT_AGENT_QUERY = PREFIXES + """
SELECT ?step ?agent
WHERE {
    ?step :performedByAgent ?agent .
    ?agent a :LLMAgent .
}
"""

# Step → Tool association (via Task :performedBy)
STEP_TASK_TOOL_QUERY = PREFIXES + """
SELECT ?task ?tool
WHERE {
    ?task a :Task ;
          :performedBy ?tool .
    ?tool a :Tool .
    FILTER NOT EXISTS { ?tool a :LLMAgent }
}
"""

# Workflow-level input schema from :hasPrompt on WorkflowPattern
WORKFLOW_INPUT_SCHEMA_QUERY = PREFIXES + """
SELECT ?wp ?inputData
WHERE {
    ?wp a :WorkflowPattern ;
        :hasPrompt ?prompt .
    ?prompt :promptInputData ?inputData .
}
"""

# Workflow-level schema from Config (triggerSchema key)
WORKFLOW_CONFIG_SCHEMA_QUERY = PREFIXES + """
SELECT ?wp ?value
WHERE {
    ?wp a :WorkflowPattern ;
        :hasConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
    FILTER(CONTAINS(LCASE(?key), "triggerschema") || CONTAINS(LCASE(?key), "inputschema"))
}
"""

# Task descriptions (for schema parsing fallback)
TASK_DESCRIPTION_QUERY = PREFIXES + """
SELECT ?task ?desc
WHERE {
    ?task a :Task .
    ?task dcterms:description ?desc .
}
"""

# ── Milestone 4: Complex Workflows ──

# Step → nextStep directed edges (branching topology)
STEP_NEXT_STEP_QUERY = PREFIXES + """
SELECT ?step ?nextStep
WHERE {
    ?step :nextStep ?nextStep .
}
"""

# WorkflowPattern → sub-pattern (nested workflow invocation)
WORKFLOW_SUB_PATTERN_QUERY = PREFIXES + """
SELECT ?wp ?sub
WHERE {
    ?wp :hasSubPattern ?sub .
    ?sub a :WorkflowPattern .
}
"""

# Prompt context text on tasks (for suspend/resume schema JSON)
TASK_PROMPT_CONTEXT_QUERY = PREFIXES + """
SELECT ?task ?context
WHERE {
    ?task a :Task .
    {
        { ?task :taskPrompt ?prompt }
        UNION
        { ?task :hasPrompt ?prompt }
    }
    ?prompt :promptContext ?context .
}
"""

# Step descriptions that hint at control flow conditions (via rdfs:comment)
STEP_COMMENT_QUERY = PREFIXES + """
SELECT ?step ?comment
WHERE {
    { ?step a :WorkflowStep } UNION { ?step a :StartStep } UNION { ?step a :EndStep }
    ?step rdfs:comment ?comment .
}
"""



MEMORY_QUERY = PREFIXES + """
SELECT ?mem ?label ?title ?desc
WHERE {
    ?mem a :Memory .
    OPTIONAL { ?mem rdfs:label ?label }
    OPTIONAL { ?mem dcterms:title ?title }
    OPTIONAL { ?mem dcterms:description ?desc }
}
"""

MEMORY_CONFIG_QUERY = PREFIXES + """
SELECT ?mem ?key ?value
WHERE {
    ?mem a :Memory ;
         :hasConfig ?cfg .
    ?cfg :configKey ?key ;
         :configValue ?value .
}
"""

# ── Environment Variables ──

ENV_CONFIG_QUERY = PREFIXES + """
SELECT ?key ?value
WHERE {
    ?cfg a :Config ;
         :configKey ?key ;
         :configValue ?value .
    FILTER(CONTAINS(LCASE(?key), "api_key") || 
           CONTAINS(LCASE(?key), "key") ||
           CONTAINS(LCASE(?key), "token"))
}
"""


# ─────────────────────── Schema Parsing ───────────────────────

def _parse_schema_from_description(desc: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse input/output schemas from tool/step descriptions.
    
    KG stores schemas as text like:
      "Input schema: { city: string }"
      "Input schema (Zod): { resumeText: string }"
      "Output: { temperature: number, ... }"
      "Output schema (Zod): { candidateName: string, isTechnical: boolean }"
      "Trigger schema (Zod): { resumeText: string }"
      
    Returns:
        (input_schema_zod, output_schema_zod)
    """
    input_schema = None
    output_schema = None
    
    # Normalize multiline to single line for regex
    single_line = re.sub(r'\s+', ' ', desc)
    
    # Pattern: "Input schema (...): { ... }" or "inputSchema: { ... }" or "Trigger schema: { ... }"
    input_match = re.search(
        r'(?:input\s*schema|inputSchema|trigger\s*schema)\s*(?:\([^)]*\))?\s*:?\s*(\{[^}]+\})',
        single_line,
        re.IGNORECASE
    )
    if input_match:
        input_schema = _convert_to_zod(input_match.group(1))
    
    # Pattern: "Output (...): { ... }" or "outputSchema (...): { ... }"
    output_match = re.search(
        r'(?:output\s*schema|outputSchema|output)\s*(?:\([^)]*\))?\s*:?\s*(\{[^}]+\})',
        single_line,
        re.IGNORECASE
    )
    if output_match:
        output_schema = _convert_to_zod(output_match.group(1))
    
    return input_schema, output_schema


def _convert_to_zod(schema_str: str) -> str:
    """
    Convert simple schema object to Zod schema string.
    
    Examples:
        "{ city: string }" → "z.object({ city: z.string() })"
        "{ count: number, active: boolean }" → 
            "z.object({ count: z.number(), active: z.boolean() })"
    """
    # Remove outer braces
    schema_str = schema_str.strip()
    if schema_str.startswith("{") and schema_str.endswith("}"):
        schema_str = schema_str[1:-1].strip()
    
    # Parse key: type pairs
    fields = []
    for pair in schema_str.split(","):
        pair = pair.strip()
        if ":" in pair:
            key, typ = pair.split(":", 1)
            key = key.strip().strip("'\"")
            typ = typ.strip().strip("'\"").lower()
            
            # Map types to Zod
            zod_type = {
                "string": "z.string()",
                "number": "z.number()",
                "boolean": "z.boolean()",
                "array": "z.array(z.any())",
                "object": "z.object({})",
            }.get(typ, "z.any()")
            
            fields.append(f"{key}: {zod_type}")
    
    if not fields:
        return "z.object({})"
    
    return f"z.object({{ {', '.join(fields)} }})"


def _parse_json_schema_to_zod(json_str: str) -> Optional[str]:
    """
    Convert JSON schema string (from some KGs) to Zod schema string.

    Handles several encoding patterns found in Mastra KGs:

    1. Full JSON Schema:
       '{"type":"object","properties":{"inputValue":{"type":"number"}}}'

    2. Simple key:type notation:
       '{"inputValue":"number"}'

    3. Wrapped notation (common in Mastra KGs — promptInputData/promptOutputIndicator):
       '{"inputSchema": {"inputValue":"number"}, "example": {...}}'
       '{"outputSchema": {"doubledValue":"number"}, "examples": {...}}'
       '{"triggerSchema": {"resumeText":"string"}}'
       → unwrap the schema key and recurse
    """
    if not json_str or not json_str.strip():
        return None

    json_str = json_str.strip()

    import json
    try:
        parsed = json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        # Not valid JSON — try as simple { key: type } notation
        if json_str.startswith("{") and json_str.endswith("}"):
            return _convert_to_zod(json_str)
        return None

    if not isinstance(parsed, dict):
        return None

    # ── Pattern 3: Unwrap schema wrapper keys ───────────────────────────────
    # KGs often store: {"inputSchema": {...actual schema...}, "example": {...}}
    _WRAPPER_KEYS = frozenset(["inputSchema", "outputSchema", "triggerSchema",
                                "inputschema", "outputschema"])
    for wk in _WRAPPER_KEYS:
        if wk in parsed and isinstance(parsed[wk], dict):
            inner = parsed[wk]
            if inner:  # non-empty → recurse
                return _parse_json_schema_to_zod(json.dumps(inner))
            # empty dict → fall through to check other keys or return z.object({})

    # ── Pattern 1: Full JSON schema ──────────────────────────────────────────
    if "properties" in parsed:
        props = parsed["properties"]
        fields = []
        for key, val in props.items():
            if isinstance(val, dict) and "type" in val:
                zod_type = {
                    "string": "z.string()",
                    "number": "z.number()",
                    "boolean": "z.boolean()",
                    "array": "z.array(z.any())",
                    "object": "z.object({})",
                    "integer": "z.number()",
                }.get(val["type"], "z.any()")
                fields.append(f"{key}: {zod_type}")
            else:
                fields.append(f"{key}: z.any()")
        if not fields:
            return "z.object({})"
        return f"z.object({{ {', '.join(fields)} }})"

    # ── Pattern 2: Simple key:type notation ─────────────────────────────────
    fields = []
    for key, val in parsed.items():
        if isinstance(val, str):
            zod_type = {
                "string": "z.string()",
                "number": "z.number()",
                "boolean": "z.boolean()",
                "array": "z.array(z.any())",
                "object": "z.object({})",
                "integer": "z.number()",
            }.get(val.lower(), "z.any()")
            fields.append(f"{key}: {zod_type}")

    if not fields:
        return None
    return f"z.object({{ {', '.join(fields)} }})"


def _normalize_schema_string(raw: str) -> Optional[str]:
    """
    Attempt to convert a raw schema string (from any source) into Zod.
    
    Tries multiple strategies:
      1. JSON schema format
      2. Simple { key: type } notation
      3. Fall back to None if unparseable
    """
    if not raw or not raw.strip():
        return None
    
    raw = raw.strip()
    
    # Strategy 1: JSON schema
    result = _parse_json_schema_to_zod(raw)
    if result and result != "z.object({})":
        return result
    
    # Strategy 2: Simple { key: type } notation
    if raw.startswith("{") and raw.endswith("}"):
        result = _convert_to_zod(raw)
        if result and result != "z.object({})":
            return result
    
    return None


def _infer_model_router_string(label: str, description: str = "") -> Tuple[str, str, str]:
    """
    Convert LanguageModel rdfs:label to Mastra model router format.
    
    Returns:
        (provider, model_name, router_string)
        
    Examples:
        "openai:gpt-4o" → ("openai", "gpt-4o", "openai/gpt-4o")
        "anthropic:claude-3-5-sonnet" → ("anthropic", "claude-3-5-sonnet", "anthropic/claude-3-5-sonnet")
        "gpt-4o" → ("openai", "gpt-4o", "openai/gpt-4o")
    """
    label = label.strip()
    
    # Already in router format
    if "/" in label:
        parts = label.split("/", 1)
        return parts[0], parts[1], label
    
    # Provider:model format
    if ":" in label:
        provider, model = label.split(":", 1)
        return provider.strip(), model.strip(), f"{provider}/{model}"
    
    # Infer provider from model name
    label_lower = label.lower()
    if "gpt" in label_lower or "openai" in label_lower:
        return "openai", label, f"openai/{label}"
    elif "claude" in label_lower or "anthropic" in label_lower:
        return "anthropic", label, f"anthropic/{label}"
    elif "gemini" in label_lower or "google" in label_lower:
        return "google", label, f"google/{label}"
    elif "llama" in label_lower:
        return "ollama", label, f"ollama/{label}"
    
    # Default to openai
    return "openai", label, f"openai/{label}"


# ─────────────────────── Extraction Functions ───────────────────────

def _extract_team(g: Graph) -> Tuple[str, str, str]:
    """Extract team/system name and description."""
    project_name = "MastraProject"
    project_var_name = "mastra-project"
    description = ""
    
    results = list(g.query(TEAM_QUERY))
    if results:
        row = results[0]
        # Prefer title > label > "Mastra"
        name = _s(row.title) or _s(row.label) or "Mastra"
        
        # Clean to PascalCase for project_name
        project_name = _pascal_case(name)
        if not project_name:
            project_name = "MastraProject"
        
        # Convert to kebab-case for directory name
        project_var_name = _safe_var(name, naming_style="kebab")
        
        description = _s(row.desc)
    
    return project_name, project_var_name, description


def _extract_language_models(g: Graph) -> Dict[str, LanguageModelModel]:
    """Extract all LanguageModel individuals."""
    models = {}
    
    for row in g.query(LLM_QUERY):
        iri = _s(row.lm)
        label = _s(row.title) or _s(row.label) or ""
        desc = _s(row.desc)
        
        provider, model_name, _ = _infer_model_router_string(label, desc)
        
        models[iri] = LanguageModelModel(
            iri=iri,
            name=label,
            description=desc,
            provider=provider,
            model_name=model_name,
        )
    
    return models


def _extract_tools(g: Graph) -> Dict[str, MastraToolModel]:
    """Extract all Tool individuals."""
    tools = {}
    
    # Get basic tool info
    for row in g.query(TOOLS_QUERY):
        iri = _s(row.tool)
        label = _s(row.title) or _s(row.label) or ""
        desc = _s(row.desc) or _s(row.comment) or ""
        
        # Parse schemas from description
        input_schema, output_schema = _parse_schema_from_description(desc)
        
        # Generate var_name and tool_id
        var_name = _safe_var(iri, naming_style="camel")
        tool_id = label or var_name
        
        # Extract execution description (first sentence or paragraph)
        execute_desc = desc.split("\n")[0] if desc else f"TODO: Implement {tool_id}"
        
        tools[iri] = MastraToolModel(
            iri=iri,
            var_name=var_name,
            tool_id=tool_id,
            description=desc,
            input_schema=input_schema,
            output_schema=output_schema,
            execute_description=execute_desc,
            configs=[],
            is_custom=True,
        )
    
    # Add tool configs
    for row in g.query(TOOL_CONFIGS_QUERY):
        iri = _s(row.tool)
        if iri in tools:
            tools[iri].configs.append(
                ToolConfigModel(key=_s(row.key), value=_s(row.value))
            )
    
    return tools


def _extract_agents(
    g: Graph,
    tools_map: Dict[str, MastraToolModel],
    llm_map: Dict[str, LanguageModelModel],
) -> Dict[str, MastraAgentModel]:
    """Extract all LLMAgent individuals."""
    agents = {}
    
    # Get basic agent info
    for row in g.query(AGENTS_QUERY):
        iri = _s(row.agent)
        agent_id = _s(row.agentID) or _safe_var(iri, naming_style="kebab")
        name = _s(row.title) or _s(row.label) or agent_id
        desc = _s(row.desc)
        
        var_name = _safe_var(iri, naming_style="camel")
        
        agents[iri] = MastraAgentModel(
            iri=iri,
            var_name=var_name,
            agent_id=agent_id,
            name=name,
            instructions="",  # Will be filled next
            model="openai/gpt-4o",  # Default
        )
    
    # Get instructions
    for row in g.query(AGENT_INSTRUCTIONS_QUERY):
        iri = _s(row.agent)
        if iri in agents:
            agents[iri].instructions = _s(row.instruction)
    
    # Get agent tools
    for row in g.query(AGENT_TOOLS_QUERY):
        agent_iri = _s(row.agent)
        tool_iri = _s(row.tool)
        if agent_iri in agents and tool_iri in tools_map:
            agents[agent_iri].tool_var_names.append(tools_map[tool_iri].var_name)
    
    # Get agent LLM
    for row in g.query(AGENT_LLM_QUERY):
        agent_iri = _s(row.agent)
        lm_iri = _s(row.lm)
        if agent_iri in agents and lm_iri in llm_map:
            llm = llm_map[lm_iri]
            agents[agent_iri].llm = llm
            agents[agent_iri].model = llm.model_router_string
    
    # Get agent configs (like maxRetries)
    for row in g.query(AGENT_CONFIGS_QUERY):
        agent_iri = _s(row.agent)
        key = _s(row.key)
        value = _s(row.value)
        
        if agent_iri in agents:
            if key.lower() in ("maxretries", "max_retries"):
                try:
                    agents[agent_iri].max_retries = int(value)
                except ValueError:
                    pass
    
    return agents


# ─────────────────────── Complex Workflow Helpers (Milestone 4) ────────────────

# Keywords that signal suspend/resume behaviour in a description
_SUSPEND_KEYWORDS = frozenset([
    "suspend", "resume", "resumedata", "context?.workflow?.suspend",
    "await suspend", "workflow.suspend",
])

# Keywords in workflow / step descriptions that signal each control flow type
_PARALLEL_KEYWORDS = frozenset(["parallel", "concurrently", "simultaneously", "at the same time"])
_BRANCH_KEYWORDS = frozenset([
    "branch", "conditional", "condition", "when ", "if ", "isTechnical",
    "branching", "based on", "depending on", "fork",
])
_LOOP_KEYWORDS = frozenset(["loop", "cyclical", "repeat", "doUntil", "dountil", "iterate", "until"])


def _detect_suspend_resume_from_text(execute_desc: str, prompt_context: str) -> bool:
    """
    Return True if a step involves suspend/resume behaviour.

    Detection sources (KG-derived):
      1. execute_description contains suspend-related keywords
      2. promptContext JSON contains "suspendSchema" or "resumeSchema" keys
    """
    combined = (execute_desc + " " + prompt_context).lower()
    if any(kw in combined for kw in _SUSPEND_KEYWORDS):
        return True
    # Also check for the JSON key names in promptContext
    if '"suspendschema"' in combined or '"resumeschema"' in combined:
        return True
    return False


def _extract_suspend_resume_schemas(
    prompt_context: str,
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Parse suspend/resume schemas and suspend message from promptContext JSON.

    KG encodes this as:
      '{"suspendSchema": {}, "resumeSchema": {"extraNumber": "number"},
        "suspendBehavior": "..."}'

    Returns:
        (suspend_schema_zod, resume_schema_zod, suspend_message)
    """
    import json as _json

    if not prompt_context or not prompt_context.strip():
        return None, None, None

    pc = prompt_context.strip()
    # Try to extract the JSON portion from the context string
    # Some contexts mix JSON with prose text
    json_match = re.search(r'\{.*\}', pc, re.DOTALL)
    if not json_match:
        return None, None, None

    try:
        parsed = _json.loads(json_match.group(0))
    except (_json.JSONDecodeError, ValueError):
        return None, None, None

    if not isinstance(parsed, dict):
        return None, None, None

    # Case-insensitive lookup for schema keys
    lower_parsed = {k.lower(): v for k, v in parsed.items()}

    suspend_schema: Optional[str] = None
    resume_schema: Optional[str] = None
    suspend_message: Optional[str] = None

    if "suspendschema" in lower_parsed:
        raw = lower_parsed["suspendschema"]
        if isinstance(raw, dict):
            suspend_schema = _parse_json_schema_to_zod(_json.dumps(raw)) or "z.object({})"
        elif isinstance(raw, str):
            suspend_schema = _normalize_schema_string(raw) or "z.object({})"

    if "resumeschema" in lower_parsed:
        raw = lower_parsed["resumeschema"]
        if isinstance(raw, dict):
            resume_schema = _parse_json_schema_to_zod(_json.dumps(raw)) or "z.object({})"
        elif isinstance(raw, str):
            resume_schema = _normalize_schema_string(raw) or "z.object({})"

    # Extract suspend message from "message", "suspendBehavior", "suspendMessage"
    for mk in ("message", "suspendbehavior", "suspendmessage"):
        if mk in lower_parsed and isinstance(lower_parsed[mk], str):
            text = lower_parsed[mk].strip()
            if text:
                # Take first sentence only
                suspend_message = text.split(".")[0].strip()[:120]
            break

    return suspend_schema, resume_schema, suspend_message


def _extract_branch_condition(step_desc: str, step_comment: str = "") -> Optional[str]:
    """
    Extract a branch condition expression from a step description.

    Patterns recognised:
      "Conditional step executed when gatherCandidateInfo.isTechnical == true"
      "Branch step executed when text length <= 10"
      "when: { 'gatherCandidateInfo.isTechnical': true }"
    """
    combined = step_desc + " " + step_comment
    # Pattern: "when X == Y" / "when X != Y" / "when X <= Y" etc.
    m = re.search(
        r'\bwhen\s+([\w\.\[\]]+(?:\.[a-zA-Z_]\w*)*\s*(?:==|!=|<=|>=|<|>|is\s+true|is\s+false)\s*\S+)',
        combined, re.IGNORECASE
    )
    if m:
        return m.group(1).strip().rstrip(".")

    # Pattern: isTechnical == true / isTechnical == false
    m = re.search(
        r'([\w\.\[\]]+(?:\.[a-zA-Z_]\w*)*\s*(?:==|!=|is\s+true|is\s+false)\s*(?:true|false|\d+|"[^"]*"))',
        combined, re.IGNORECASE
    )
    if m:
        return m.group(1).strip()

    return None


def _detect_control_flow(wf_desc: str, steps: List) -> ControlFlowType:
    """
    Infer workflow control flow type from description and step conditions.

    Priority order: LOOP > PARALLEL > BRANCHING > SEQUENTIAL
    """
    desc_lower = (wf_desc or "").lower()

    if any(kw in desc_lower for kw in _LOOP_KEYWORDS):
        return ControlFlowType.LOOP

    if any(kw in desc_lower for kw in _PARALLEL_KEYWORDS):
        return ControlFlowType.PARALLEL

    if any(kw in desc_lower for kw in _BRANCH_KEYWORDS):
        return ControlFlowType.BRANCHING

    # Inspect step conditions
    if any(getattr(s, "condition", None) for s in steps):
        return ControlFlowType.BRANCHING

    return ControlFlowType.SEQUENTIAL


# ─────────────────────── Memory Extraction ───────────────────────

# Storage-related tool label keywords — tools matching these are storage backends
_STORAGE_TOOL_KEYWORDS = frozenset([
    "store", "vector", "storage", "mongodb", "postgres", "libsql",
    "upstash", "pgvector", "mongodbvector", "sqlite",
])


def _is_storage_tool(label: str) -> bool:
    """Return True if tool label suggests it is a storage/vector backend (not a real tool)."""
    label_lower = label.lower()
    return any(kw in label_lower for kw in _STORAGE_TOOL_KEYWORDS)


def _parse_memory_from_configs(
    configs: List[Tuple[str, str]],
    description: str,
) -> "MemoryModel":  # forward ref — resolved at runtime
    """
    Parse a list of (configKey, configValue) pairs into a structured MemoryModel.

    Handles four KG encoding patterns found in the wild:
      1. Simple keys: "lastMessages" = "10"
      2. Namespaced keys: "memory.options.lastMessages" = "10"
      3. Storage adapter type: "memory.storage.adapter" = "UpstashStore"
      4. Inline JSON-like options: "memory.options.default" = "{ lastMessages:1, ... }"
    """
    storage_type = "libsql"         # default
    storage_config: List[ConfigModel] = []
    vector_type: Optional[str] = None
    vector_config: List[ConfigModel] = []

    last_messages: Optional[int] = None
    semantic_recall_top_k: Optional[int] = None
    semantic_recall_message_range: Optional[int] = None
    semantic_recall_enabled: bool = True
    working_memory_enabled: bool = False
    working_memory_template: Optional[str] = None
    working_memory_scope: Optional[str] = None
    embedder_model: Optional[str] = None
    token_limit: Optional[int] = None

    def _try_int(v: str) -> Optional[int]:
        try:
            return int(v)
        except (ValueError, TypeError):
            return None

    def _parse_inline_options(value: str) -> None:
        """Parse options from inline JSON-like string, e.g. '{ lastMessages: 1, ... }'."""
        nonlocal last_messages, semantic_recall_top_k, semantic_recall_message_range

        m = re.search(r'lastMessages\s*:\s*(\d+)', value, re.IGNORECASE)
        if m:
            last_messages = int(m.group(1))

        m = re.search(r'topK\s*:\s*(\d+)', value, re.IGNORECASE)
        if m:
            semantic_recall_top_k = int(m.group(1))

        m = re.search(r'messageRange\s*:\s*(\d+)', value, re.IGNORECASE)
        if m:
            semantic_recall_message_range = int(m.group(1))

    for raw_key, value in configs:
        # Normalise key: strip namespace prefixes and lowercase for comparison
        key = raw_key.strip()
        kl = key.lower()

        # ── Storage type detection ──────────────────────────────────
        if "storage.adapter" in kl or kl == "adapter":
            vl = value.lower()
            if "upstash" in vl:
                storage_type = "upstash"
            elif "mongodb" in vl:
                storage_type = "mongodb"
            elif "postgres" in vl or "pg" in vl:
                storage_type = "pg"
            elif "libsql" in vl or "sqlite" in vl:
                storage_type = "libsql"

        # ── PG storage host/port/user/database/password ────────────
        elif re.search(r'storage\.host$', kl):
            storage_type = "pg"
            storage_config.append(ConfigModel(key="host", value=value))
        elif re.search(r'storage\.port$', kl):
            storage_config.append(ConfigModel(key="port", value=value))
        elif re.search(r'storage\.user$', kl):
            storage_config.append(ConfigModel(key="user", value=value))
        elif re.search(r'storage\.database$', kl):
            storage_config.append(ConfigModel(key="database", value=value))
        elif re.search(r'storage\.password$', kl):
            storage_config.append(ConfigModel(key="password", value=value))

        # ── Vector store config ─────────────────────────────────────
        elif "vector.connectionstring" in kl or "vector.connection" in kl:
            vl = value.lower()
            if "postgresql" in vl or "postgres" in vl:
                vector_type = "pgvector"
            else:
                vector_type = "pgvector"  # default if we see vector.connectionString
            vector_config.append(ConfigModel(key="connectionString", value=value))

        # ── URL / URI → detect storage type + record config ────────
        elif kl in ("url", "uri", "storage.url"):
            vl = value.lower()
            if "mongodb" in vl or "process.env.mongodb" in vl:
                storage_type = "mongodb"
            elif ("postgresql" in vl or "postgres" in vl) and storage_type == "libsql":
                storage_type = "pg"
            elif "file:" in vl or "libsql" in vl:
                storage_type = "libsql"
            # Upstash: localhost:8089 or upstash.io URLs
            elif "upstash" in vl or (
                re.search(r'localhost:\d{4}', vl) and storage_type == "libsql"
            ):
                storage_type = "upstash"
            storage_config.append(ConfigModel(key="url", value=value))

        elif kl in ("dbname", "db_name"):
            storage_config.append(ConfigModel(key="dbName", value=value))
        elif kl == "token":
            storage_config.append(ConfigModel(key="token", value=value))
        elif kl == "authtoken":
            storage_config.append(ConfigModel(key="authToken", value=value))
        elif kl in ("connectionstring", "connection_string", "storage.connectionstring"):
            storage_config.append(ConfigModel(key="connectionString", value=value))
            if ("postgresql" in value.lower() or "postgres" in value.lower()) and storage_type == "libsql":
                storage_type = "pg"

        # ── Memory options ─────────────────────────────────────────
        elif kl in ("lastmessages", "memory.options.lastmessages", "last_messages"):
            last_messages = _try_int(value)

        elif kl in ("semanticrecall.topk", "memory.options.semanticrecall.topk"):
            semantic_recall_top_k = _try_int(value)

        elif kl in ("semanticrecall.messagerange", "memory.options.semanticrecall.messagerange"):
            semantic_recall_message_range = _try_int(value)

        elif kl in ("semanticrecall", "memory.options.semanticrecall"):
            if value.strip().lower() == "false":
                semantic_recall_enabled = False
            else:
                # Could be a topK integer
                v = _try_int(value)
                if v is not None:
                    semantic_recall_top_k = v

        elif kl in ("workingmemory.enabled", "memory.options.workingmemory.enabled"):
            working_memory_enabled = value.strip().lower() in ("true", "1", "yes")

        elif kl in ("workingmemory.template", "memory.options.workingmemory.template"):
            working_memory_template = value

        elif kl in ("workingmemory.scope", "memory.options.workingmemory.scope"):
            working_memory_scope = value.strip()

        elif kl in ("embedder", "memory.embedder", "memory.embedder.model"):
            embedder_model = value.strip()

        elif kl == "tokenlimiter":
            token_limit = _try_int(value)

        # ── Inline options blob ─────────────────────────────────────
        elif "options.default" in kl or kl == "options":
            _parse_inline_options(value)

    # ── Fallback: detect storage from description text ──────────────
    if storage_type == "libsql":
        desc_lower = (description or "").lower()
        if "mongodb" in desc_lower or "mongodbstore" in desc_lower:
            storage_type = "mongodb"
        elif "postgresstore" in desc_lower or "postgresql" in desc_lower:
            storage_type = "pg"
        elif "upstash" in desc_lower or "upstashstore" in desc_lower:
            storage_type = "upstash"
        # libsql stays as default

    # ── Build semantic_recall dict for backwards compat ─────────────
    semantic_recall_dict: Optional[Dict[str, int]] = None
    if semantic_recall_enabled and (
        semantic_recall_top_k is not None or semantic_recall_message_range is not None
    ):
        semantic_recall_dict = {}
        if semantic_recall_top_k is not None:
            semantic_recall_dict["topK"] = semantic_recall_top_k
        if semantic_recall_message_range is not None:
            semantic_recall_dict["messageRange"] = semantic_recall_message_range

    return MemoryModel(
        iri="",           # filled in by caller
        var_name="",      # filled in by caller
        label="",
        description="",
        storage_type=storage_type,
        storage_config=storage_config,
        vector_type=vector_type,
        vector_config=vector_config,
        embedder_model=embedder_model,
        last_messages=last_messages,
        semantic_recall_enabled=semantic_recall_enabled,
        semantic_recall_top_k=semantic_recall_top_k,
        semantic_recall_message_range=semantic_recall_message_range,
        semantic_recall=semantic_recall_dict,
        working_memory_enabled=working_memory_enabled,
        working_memory_template=working_memory_template,
        working_memory_scope=working_memory_scope,
        token_limit=token_limit,
    )


def _extract_memory(g: Graph) -> Dict[str, MemoryModel]:
    """
    Extract all :Memory instances from the KG and build MemoryModel objects.

    Returns dict keyed by memory IRI.
    """
    memories: Dict[str, dict] = {}

    # Collect basic memory metadata
    for row in g.query(MEMORY_QUERY):
        iri = _s(row.mem)
        label = _s(row.title) or _s(row.label) or ""
        desc = _s(row.desc)
        memories[iri] = {
            "label": label,
            "desc": desc,
            "configs": [],
        }

    if not memories:
        return {}

    # Collect config key-value pairs per memory
    for row in g.query(MEMORY_CONFIG_QUERY):
        mem_iri = _s(row.mem)
        key = _s(row.key)
        value = _s(row.value)
        if mem_iri in memories and key:
            memories[mem_iri]["configs"].append((key, value))

    # Parse into MemoryModel
    result: Dict[str, MemoryModel] = {}
    for iri, data in memories.items():
        model = _parse_memory_from_configs(data["configs"], data["desc"])
        model.iri = iri
        model.var_name = _safe_var(iri, naming_style="camel")
        model.label = data["label"]
        model.description = data["desc"]
        result[iri] = model

    return result


# ─────────────────────── Workflow Extraction ───────────────────────

def _extract_workflows(
    g: Graph,
    agents_map: Dict[str, MastraAgentModel],
    tools_map: Dict[str, MastraToolModel],
) -> List[WorkflowModel]:
    """
    Extract WorkflowPattern + WorkflowStep data from KG.

    Multi-source schema extraction strategy:
      1. Prompt :promptInputData / :promptOutputIndicator (via Task)
      2. Prompt directly on WorkflowStep (:taskPrompt)
      3. Config individuals with schema keys (on Task)
      4. Task dcterms:description text parsing (fallback)

    Milestone 4 additions:
      - Suspend/resume detection (from execute_description + promptContext)
      - Branch condition extraction (from step descriptions)
      - Control flow type detection (SEQUENTIAL / BRANCHING / PARALLEL / LOOP)
      - Nested sub-workflow detection (via :hasSubPattern)
      - Schema JSON unwrapping (remove inputSchema/outputSchema wrappers)

    Returns ordered list of WorkflowModel with populated StepModel entries.
    """
    # ── Step 1: Extract all workflow patterns ──
    workflow_patterns: Dict[str, dict] = {}
    for row in g.query(WORKFLOW_PATTERN_QUERY):
        iri = _s(row.wp)
        label = _s(row.title) or _s(row.label) or ""
        desc = _s(row.desc)
        workflow_patterns[iri] = {
            "label": label,
            "desc": desc,
        }

    if not workflow_patterns:
        return []

    # ── Step 2: Map workflow → step IRIs ──
    wf_to_steps: Dict[str, Set[str]] = {iri: set() for iri in workflow_patterns}
    for row in g.query(WORKFLOW_STEPS_QUERY):
        wp_iri = _s(row.wp)
        step_iri = _s(row.step)
        if wp_iri in wf_to_steps:
            wf_to_steps[wp_iri].add(step_iri)

    # ── Step 3: Extract step details ──
    step_details: Dict[str, dict] = {}
    for row in g.query(STEP_DETAILS_QUERY):
        iri = _s(row.step)
        label = _s(row.title) or _s(row.label) or ""
        desc = _s(row.desc)
        order = None
        if row.order is not None:
            try:
                order = int(row.order)
            except (ValueError, TypeError):
                pass
        step_details[iri] = {
            "label": label,
            "desc": desc,
            "order": order,
            "comment": "",
        }

    # Step comments (additional descriptions for conditions)
    for row in g.query(STEP_COMMENT_QUERY):
        iri = _s(row.step)
        if iri in step_details:
            step_details[iri]["comment"] = _s(row.comment)

    # ── Step 4: Map step → task ──
    step_to_task: Dict[str, str] = {}
    for row in g.query(STEP_TASK_QUERY):
        step_iri = _s(row.step)
        task_iri = _s(row.task)
        step_to_task[step_iri] = task_iri

    # ── Step 5: Extract task schemas from Prompts ──
    # task_iri → {inputData, outputIndicator, instruction, context}
    task_schemas: Dict[str, dict] = {}
    for row in g.query(STEP_SCHEMA_QUERY):
        task_iri = _s(row.task)
        if task_iri not in task_schemas:
            task_schemas[task_iri] = {
                "inputData": "", "outputIndicator": "",
                "instruction": "", "context": "",
            }
        # Accumulate (some tasks have multiple prompts)
        if _s(row.inputData):
            task_schemas[task_iri]["inputData"] = _s(row.inputData)
        if _s(row.outputIndicator):
            task_schemas[task_iri]["outputIndicator"] = _s(row.outputIndicator)
        if _s(row.instruction):
            task_schemas[task_iri]["instruction"] = _s(row.instruction)
        if _s(row.context):
            task_schemas[task_iri]["context"] = _s(row.context)

    # ── Step 5b: Extract schemas from Prompts directly on WorkflowStep ──
    step_direct_schemas: Dict[str, dict] = {}
    for row in g.query(STEP_DIRECT_PROMPT_QUERY):
        step_iri = _s(row.step)
        if step_iri not in step_direct_schemas:
            step_direct_schemas[step_iri] = {
                "inputData": "", "outputIndicator": "", "instruction": "",
            }
        if _s(row.inputData):
            step_direct_schemas[step_iri]["inputData"] = _s(row.inputData)
        if _s(row.outputIndicator):
            step_direct_schemas[step_iri]["outputIndicator"] = _s(row.outputIndicator)
        if _s(row.instruction):
            step_direct_schemas[step_iri]["instruction"] = _s(row.instruction)

    # ── Step 5c: Extract promptContext per task (for suspend/resume) ──
    task_prompt_contexts: Dict[str, str] = {}
    for row in g.query(TASK_PROMPT_CONTEXT_QUERY):
        task_iri = _s(row.task)
        ctx = _s(row.context)
        if ctx:
            task_prompt_contexts[task_iri] = ctx

    # ── Step 6: Extract schemas from Config individuals (on Task) ──
    task_config_schemas: Dict[str, dict] = {}
    for row in g.query(STEP_CONFIG_SCHEMA_QUERY):
        task_iri = _s(row.task)
        key = _s(row.key).lower()
        value = _s(row.value)
        if task_iri not in task_config_schemas:
            task_config_schemas[task_iri] = {"input": "", "output": ""}
        if "input" in key:
            task_config_schemas[task_iri]["input"] = value
        elif "output" in key:
            task_config_schemas[task_iri]["output"] = value

    # ── Step 7: Extract task descriptions (for schema parsing fallback) ──
    task_descriptions: Dict[str, str] = {}
    for row in g.query(TASK_DESCRIPTION_QUERY):
        task_iri = _s(row.task)
        task_descriptions[task_iri] = _s(row.desc)

    # ── Step 8: Extract step→agent associations ──
    task_to_agent: Dict[str, str] = {}
    for row in g.query(STEP_TASK_AGENT_QUERY):
        task_iri = _s(row.task)
        agent_iri = _s(row.agent)
        task_to_agent[task_iri] = agent_iri

    step_to_agent: Dict[str, str] = {}
    for row in g.query(STEP_DIRECT_AGENT_QUERY):
        step_iri = _s(row.step)
        agent_iri = _s(row.agent)
        step_to_agent[step_iri] = agent_iri

    # ── Step 9: Extract step→tool associations ──
    task_to_tool: Dict[str, str] = {}
    for row in g.query(STEP_TASK_TOOL_QUERY):
        task_iri = _s(row.task)
        tool_iri = _s(row.tool)
        task_to_tool[task_iri] = tool_iri

    # ── Step 10: Extract workflow input schemas ──
    wf_input_schemas: Dict[str, str] = {}
    for row in g.query(WORKFLOW_INPUT_SCHEMA_QUERY):
        wp_iri = _s(row.wp)
        input_data = _s(row.inputData)
        if wp_iri not in wf_input_schemas and input_data:
            wf_input_schemas[wp_iri] = input_data

    for row in g.query(WORKFLOW_CONFIG_SCHEMA_QUERY):
        wp_iri = _s(row.wp)
        value = _s(row.value)
        if wp_iri not in wf_input_schemas and value:
            wf_input_schemas[wp_iri] = value

    # ── Milestone 4: Extract step :nextStep topology (branching) ──
    step_next_steps: Dict[str, Set[str]] = {}  # step_iri → set of next step IRIs
    for row in g.query(STEP_NEXT_STEP_QUERY):
        step_iri = _s(row.step)
        next_iri = _s(row.nextStep)
        step_next_steps.setdefault(step_iri, set()).add(next_iri)

    # ── Milestone 4: Extract sub-patterns (nested workflows) ──
    wf_sub_patterns: Dict[str, Set[str]] = {}  # parent_wp_iri → set of sub_wp_iri
    for row in g.query(WORKFLOW_SUB_PATTERN_QUERY):
        wp_iri = _s(row.wp)
        sub_iri = _s(row.sub)
        wf_sub_patterns.setdefault(wp_iri, set()).add(sub_iri)

    # Compute reverse map: sub-workflow → var_name (for nested workflow references)
    sub_wf_var_names: Dict[str, str] = {}
    for wf_iri, info in workflow_patterns.items():
        sub_wf_var_names[wf_iri] = _safe_var(wf_iri, naming_style="camel")

    # Build agent/tool IRI reverse lookups
    agent_iri_to_var: Dict[str, str] = {a.iri: a.var_name for a in agents_map.values()}
    tool_iri_to_var: Dict[str, str] = {t.iri: t.var_name for t in tools_map.values()}

    # ── Assemble WorkflowModel list ──
    workflows: List[WorkflowModel] = []

    for wf_iri, wf_info in workflow_patterns.items():
        step_iris = wf_to_steps.get(wf_iri, set())

        # Build StepModel list for this workflow
        steps: List[StepModel] = []
        fallback_order = 0

        for step_iri in step_iris:
            details = step_details.get(step_iri, {"label": "", "desc": "", "order": None, "comment": ""})
            task_iri = step_to_task.get(step_iri, "")

            # Step ID and var_name
            step_label = details["label"]
            step_id = step_label or _safe_var(step_iri, naming_style="kebab")
            var_name = _safe_var(step_iri, naming_style="camel")

            # Step order
            order = details.get("order")
            if order is None:
                fallback_order += 1
                order = fallback_order

            step_desc = details.get("desc", "")
            step_comment = details.get("comment", "")

            # ── Schema extraction (multi-source) ──────────────────────────────
            input_schema = None
            output_schema = None
            execute_desc = ""
            prompt_context_str = ""

            # Source 1: Task prompt schemas (+ context for suspend/resume)
            if task_iri and task_iri in task_schemas:
                ts = task_schemas[task_iri]
                if ts["inputData"]:
                    input_schema = _normalize_schema_string(ts["inputData"])
                if ts["outputIndicator"]:
                    output_schema = _normalize_schema_string(ts["outputIndicator"])
                if ts["instruction"]:
                    execute_desc = ts["instruction"]
                if ts["context"]:
                    prompt_context_str = ts["context"]

            # Source 1b: Direct prompt on step
            if step_iri in step_direct_schemas:
                ds = step_direct_schemas[step_iri]
                if ds["inputData"] and not input_schema:
                    input_schema = _normalize_schema_string(ds["inputData"])
                if ds["outputIndicator"] and not output_schema:
                    output_schema = _normalize_schema_string(ds["outputIndicator"])
                if ds["instruction"] and not execute_desc:
                    execute_desc = ds["instruction"]

            # Source 1c: Task promptContext (separate query, may have richer data)
            if task_iri and task_iri in task_prompt_contexts:
                pc = task_prompt_contexts[task_iri]
                if pc and not prompt_context_str:
                    prompt_context_str = pc

            # Source 2: Config schemas on task
            if task_iri and task_iri in task_config_schemas:
                cs = task_config_schemas[task_iri]
                if cs["input"] and not input_schema:
                    input_schema = _normalize_schema_string(cs["input"])
                if cs["output"] and not output_schema:
                    output_schema = _normalize_schema_string(cs["output"])

            # Source 3: Parse from task description
            if task_iri and task_iri in task_descriptions:
                task_desc = task_descriptions[task_iri]
                if not input_schema or not output_schema:
                    desc_in, desc_out = _parse_schema_from_description(task_desc)
                    if desc_in and not input_schema:
                        input_schema = desc_in
                    if desc_out and not output_schema:
                        output_schema = desc_out
                if not execute_desc:
                    execute_desc = task_desc.split("\n")[0]

            # Source 4: Parse from step description (last resort)
            if not input_schema or not output_schema:
                desc_in, desc_out = _parse_schema_from_description(step_desc)
                if desc_in and not input_schema:
                    input_schema = desc_in
                if desc_out and not output_schema:
                    output_schema = desc_out

            if not execute_desc and step_desc:
                execute_desc = step_desc.split("\n")[0]

            # ── Milestone 4: Suspend/resume detection ─────────────────────────
            is_suspend = _detect_suspend_resume_from_text(execute_desc, prompt_context_str)
            sus_schema, res_schema, sus_msg = None, None, None
            if is_suspend:
                sus_schema, res_schema, sus_msg = _extract_suspend_resume_schemas(prompt_context_str)

            # ── Milestone 4: Branch condition extraction ──────────────────────
            condition = _extract_branch_condition(step_desc, step_comment)

            # ── Agent/Tool association ─────────────────────────────────────────
            agent_var = None
            tool_var = None

            if task_iri and task_iri in task_to_agent:
                agent_iri = task_to_agent[task_iri]
                agent_var = agent_iri_to_var.get(agent_iri)
            if step_iri in step_to_agent:
                agent_iri = step_to_agent[step_iri]
                agent_var = agent_iri_to_var.get(agent_iri, agent_var)
            if task_iri and task_iri in task_to_tool:
                tool_iri = task_to_tool[task_iri]
                tool_var = tool_iri_to_var.get(tool_iri)

            steps.append(StepModel(
                iri=step_iri,
                var_name=var_name,
                step_id=step_id,
                step_order=order,
                description=step_desc,
                input_schema=input_schema,
                output_schema=output_schema,
                execute_description=execute_desc,
                agent_var_name=agent_var,
                tool_var_name=tool_var,
                is_suspend_resume=is_suspend,
                suspend_schema=sus_schema,
                resume_schema=res_schema,
                suspend_message=sus_msg,
                condition=condition,
                after_step_var_name=None,  # populated below
            ))

        # Sort steps by order
        steps.sort(key=lambda s: s.step_order)

        # ── Milestone 4: Determine .after() relationships for branching ─────
        # Build step_iri → StepModel for this workflow
        step_iri_to_model: Dict[str, StepModel] = {s.iri: s for s in steps}

        # For each step that has :nextStep pointing to multiple targets,
        # the second+ branch targets need .after(sourceStep)
        for src_iri, next_iris in step_next_steps.items():
            if src_iri not in step_iri_to_model:
                continue
            if len(next_iris) <= 1:
                continue  # not a branch source
            src_model = step_iri_to_model[src_iri]
            # Find all steps in THIS workflow that are in next_iris
            targets = [
                step_iri_to_model[ni] for ni in next_iris
                if ni in step_iri_to_model
            ]
            # Sort by step_order so first target stays as .then(), rest get .after()
            targets.sort(key=lambda s: s.step_order)
            for i, target in enumerate(targets[1:], 1):
                target.after_step_var_name = src_model.var_name

        # ── Workflow-level schema ──────────────────────────────────────────────
        wf_input_schema = None
        wf_raw = wf_input_schemas.get(wf_iri, "")
        if wf_raw:
            wf_input_schema = _normalize_schema_string(wf_raw)

        if not wf_input_schema and wf_info["desc"]:
            desc_in, _ = _parse_schema_from_description(wf_info["desc"])
            if desc_in:
                wf_input_schema = desc_in

        # ── Workflow ID and var_name ───────────────────────────────────────────
        wf_label = wf_info["label"]
        wf_id = wf_label or _safe_var(wf_iri, naming_style="kebab")
        wf_var = _safe_var(wf_iri, naming_style="camel")

        # ── Milestone 4: Control flow detection ──────────────────────────────
        control_flow = _detect_control_flow(wf_info["desc"], steps)

        # ── Milestone 4: Nested sub-workflows ─────────────────────────────────
        nested_var_names = [
            sub_wf_var_names[sub_iri]
            for sub_iri in wf_sub_patterns.get(wf_iri, set())
            if sub_iri in sub_wf_var_names
        ]

        workflows.append(WorkflowModel(
            iri=wf_iri,
            var_name=wf_var,
            workflow_id=wf_id,
            description=wf_info["desc"],
            input_schema=wf_input_schema,
            output_schema=None,
            steps=steps,
            control_flow=control_flow,
            nested_workflow_var_names=nested_var_names,
        ))
    
    return workflows


# ─────────────────────── Main Extraction Function ───────────────────────

def extract_mastra_project(ttl_path: str) -> MastraProject:
    """
    Main extraction function: KG (.ttl) → MastraProject IR.

    Extracts:
      - Team/System
      - LanguageModels
      - Tools (including storage-tool detection)
      - Agents (with memory linkage)
      - Workflows with steps (Milestone 2)
      - Memory instances with storage/options config (Milestone 3)
    """
    g = load_graph(ttl_path)

    # Extract team info
    project_name, project_var_name, description = _extract_team(g)

    # Extract language models
    llm_map = _extract_language_models(g)

    # Extract tools
    tools_map = _extract_tools(g)

    # Extract agents
    agents_map = _extract_agents(g, tools_map, llm_map)

    # ── Milestone 3: Extract memory instances ──────────────────────
    memories_map = _extract_memory(g)

    # Link agents to memory via :hasKnowledge
    if memories_map:
        for row in g.query(AGENT_MEMORY_QUERY):
            agent_iri = _s(row.agent)
            mem_iri = _s(row.mem)
            if agent_iri in agents_map and mem_iri in memories_map:
                agents_map[agent_iri].memory_var_name = memories_map[mem_iri].var_name

    # Mark storage-backend tools so the generator can skip createTool() for them.
    # A tool is a storage tool when:
    #   (a) its label matches storage keywords, AND
    #   (b) no agent uses it via :agentToolUsage
    all_agent_tool_var_names: set = {
        tv for a in agents_map.values() for tv in a.tool_var_names
    }
    for tool in tools_map.values():
        if (
            _is_storage_tool(tool.tool_id)
            and tool.var_name not in all_agent_tool_var_names
        ):
            tool.is_storage_tool = True

    # Extract workflows (Milestone 2)
    workflows = _extract_workflows(g, agents_map, tools_map)

    # Build project
    project = MastraProject(
        project_name=project_name,
        project_var_name=project_var_name,
        description=description,
        agents=list(agents_map.values()),
        tools=list(tools_map.values()),
        language_models=list(llm_map.values()),
        workflows=workflows,
        memory_configs=list(memories_map.values()),
        env_vars=[],
        system_configs=[],
    )

    return project
