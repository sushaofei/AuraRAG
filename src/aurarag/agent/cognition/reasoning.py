"""RAG reasoning module.

Responsibilities:
- organize retrieval evidence
- build context summary for generation
- provide hook point for future multi-step reasoning
"""

from __future__ import annotations

from aurarag.agent.perception.ingestion import KnowledgeUnit


class RAGReasoner:
    """Cognition-layer reasoning boundary."""

    def build_context(self, query: str, evidence: list[KnowledgeUnit]) -> str:
        if not evidence:
            return f"No evidence found for query: {query.strip()}"
        joined = "\n".join(f"- {item.content}" for item in evidence)
        return f"Query: {query.strip()}\nEvidence:\n{joined}"
