from aurarag.agent import (
    AgentLoopController,
    RAGGenerator,
    RAGIngestion,
    RAGReasoner,
    RAGRetriever,
    ToolExecutor,
)


def test_agent_modules_are_importable() -> None:
    assert RAGIngestion is not None
    assert RAGRetriever is not None
    assert RAGReasoner is not None
    assert RAGGenerator is not None
    assert ToolExecutor is not None
    assert AgentLoopController is not None


def test_layer_flow_perception_to_cognition_to_action() -> None:
    controller = AgentLoopController()

    result = controller.run_once(
        query="rag",
        raw_text="Agentic RAG architecture baseline.",
        source_type="markdown",
    )

    assert isinstance(result, str)
    assert "Answer Draft:" in result
    assert "Evidence:" in result
