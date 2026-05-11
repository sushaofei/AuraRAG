# AuraRAG

An Agentic Retrieval-Augmented Generation (RAG) project.

## Project Structure

```text
AuraRAG/
├── .github/workflows/     # CI pipeline
├── docs/                  # Documentation
├── src/aurarag/           # Application source code
│   └── agent/             # Three-layer agent architecture scaffold
├── tests/                 # Test suite
├── LICENSE
├── README.md
└── pyproject.toml         # Project, formatter, linter, and test config
```

## Requirements

- Conda (Miniconda or Anaconda)

## Installation

1. Create the Conda environment:

```bash
conda env create -f environment.yml
```

2. Activate the environment:

```bash
conda activate aura-rag
```

3. If dependencies change later, update environment:

```bash
conda env update -f environment.yml --prune
```

## Development Commands

Run from project root:

```bash
pytest -q
ruff check .
ruff format --check .
```

## Architecture Overview

Three-layer scaffold is located at `src/aurarag/agent/`:

- Perception Layer: `perception/ingestion.py`
- Cognition Layer: `cognition/retrieval.py`, `cognition/reasoning.py`
- Action Layer: `action/generation.py`, `action/tool_use.py`, `action/loop.py`

`AgentLoopController` in `action/loop.py` provides a minimal one-turn pipeline that expresses:
Perception -> Cognition -> Action.

## Usage

This repository currently provides architecture scaffolding and importable interfaces.
Future work will plug in full parsers, vector stores, LLM calls, and tool execution engines.
