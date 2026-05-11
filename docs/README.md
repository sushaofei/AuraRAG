# Docs

## Agentic RAG Three-Layer Architecture

The project uses a scaffolded three-layer architecture under `src/aurarag/agent/`.

- Perception (`perception/ingestion.py`): ingest and normalize raw knowledge inputs.
- Cognition (`cognition/retrieval.py`, `cognition/reasoning.py`): retrieve evidence and build reasoning context.
- Action (`action/generation.py`, `action/tool_use.py`, `action/loop.py`): generate outputs, define tool boundary, and orchestrate the main loop.

Current scope provides executable interfaces and module boundaries only, aligned with issue #4 non-goals.
