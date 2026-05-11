# AuraRAG

An Agentic Retrieval-Augmented Generation (RAG) project.

## Project Structure

```text
AuraRAG/
├── .github/workflows/     # CI pipeline
├── docs/                  # Documentation
├── src/aurarag/           # Application source code
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

## Usage

This repository is currently a scaffolded foundation for AuraRAG:

- Source code lives in `src/aurarag/`
- Tests live in `tests/`
- CI runs lint + format check + tests on every push and pull request

As features are added, place runtime entrypoints/scripts under `src/aurarag/` and document new commands here.
