"""RAG retrieval module.

Responsibilities:
- query understanding and retrieval boundary
- select candidate evidence from retrievable units
- expose consistent retrieval output for reasoning
"""

from __future__ import annotations

from aurarag.agent.perception.ingestion import KnowledgeUnit


class RAGRetriever:
    """Cognition-layer retrieval boundary.

    Placeholder implementation performs simple keyword filtering to keep
    architecture executable without introducing external dependencies.
    """

    def retrieve(self, query: str, units: list[KnowledgeUnit]) -> list[KnowledgeUnit]:
        query_text = query.strip().lower()
        if not query_text:
            return units
        return [unit for unit in units if query_text in unit.content.lower()]
