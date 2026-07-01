"""
LangGraph Pipeline: KG (.ttl) → SPARQL → Pydantic → Python (Jinja2)

Three-layer conversion pipeline:
  Layer 1 – SPARQL extraction  (rdflib)   → src/core/extractor.py
  Layer 2 – Pydantic IR        (models)   → src/core/models.py + src/langgraph/models.py
  Layer 3 – File generation    (Jinja2)   → src/langgraph/generator.py

Supported graph patterns:
  linear       – single agent, no tools
  tool_calling – single agent with bound tools
  supervisor   – multi-agent with supervisor router

Key models:
  Canonical IR                  → src/core/models.py
  LangGraph-specific IR         → src/langgraph/models.py
  LangGraphProject      – top-level IR passed between layers
  LangGraphAgentModel   – agent → node function in graph.py
  LangGraphToolModel    – tool  → @tool stub in graph.py
  LangGraphNodeModel    – step  → StateGraph.add_node()
  LangGraphEdgeModel    – link  → StateGraph.add_edge()

Key functions (defined in src/core/extractor.py):
  extract_project(file_path) + adapter.adapt(project) → LangGraphProject
"""
