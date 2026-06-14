"""
CrewAI Pipeline: KG (.ttl) → SPARQL → Pydantic → YAML + Python (Jinja2)

Three-layer conversion pipeline:
  Layer 1 – SPARQL extraction (rdflib)
  Layer 2 – Pydantic intermediate representation
  Layer 3 – File generation (PyYAML + Jinja2)
"""
