# quiz-generator

An AI-powered quiz generator that creates multiple-choice questions from study passages, validates each question automatically, and evaluates the generator on a golden set. Built in experiment > validate > evaluate loops.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- An [Anthropic API key](https://console.anthropic.com/)

## Getting started

**1. Clone and install dependencies**

```bash
git clone <repo-url>
cd quiz-generator
uv sync
```

**2. Install git hooks**

```bash
uv run pre-commit install
```

**3. Set up your environment**

```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

**4. Generate a quiz**

Pass a study passage as an argument:

```bash
uv run generate-quiz path/to/passage.md
```

To run on the included sample:

```bash
uv run generate-quiz data/samples/01-git-tags-explainer.md
```

Output is written to `data/output/output-quiz-<timestamp>.md`.

## Progress log with evals

> Note: Eval columns to be added.

| Tag | Changes |
|---|---|
| v0.0.1 | **Basic quiz generation via Claude Messages API:** plain-text response written to `data/output/output-quiz-<timestamp>.md`. <br><br> **Repo housekeeping setup:** `uv` project setup with `.env` config and sample passage; added Ruff (linter + formatter) and pre-commit hooks; trimmed `.gitignore` to project-specific entries. <br><br> **Entry point:** `generate-quiz` CLI entry point added via `pyproject.toml` `[project.scripts]`. |
