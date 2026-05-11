# AGENTS.md

This document defines repository-level operating rules for Codex in this repo.

## Required SOP For Issue-Driven Work

When a task is related to a GitHub Issue (new feature, fix, refactor, chore), Codex must follow this exact sequence by default:

1. Read Issue
2. Create Branch
3. Implement
4. Test
5. Commit
6. Open PR
7. Link and Close Issue

Do not skip or reorder steps unless the user explicitly asks to do so.

## Step Details

### 1) Read Issue

- Identify the target issue number and full content (title, description, checklist, comments).
- Extract acceptance criteria and constraints before coding.
- If requirements are ambiguous, ask concise clarifying questions before implementation.

### 2) Create Branch

- Create a dedicated branch before code changes.
- Branch naming convention:
  - `codex/issue-<number>-<short-slug>`
  - Example: `codex/issue-12-init-project-structure`
- If the user requires a different branch name, follow the user.

### 3) Implement

- Implement only the scope required by the issue (avoid unrelated refactors).
- Keep changes minimal, readable, and consistent with current project structure.
- Update docs/config/tests as needed to keep the change self-contained.

### 4) Test

- Run relevant automated checks locally whenever possible (tests, lint, format checks).
- If a required tool is unavailable, report exactly what could not be run and why.
- Do not claim success without real command results.

### 5) Commit

- Create an intentional commit with a clear message.
- Prefer referencing the issue in the commit body, for example:
  - `Refs #<number>` for partial work
  - `Closes #<number>` only when the change fully resolves the issue

### 6) Open PR

- Push branch and open a PR against the correct base branch.
- PR title/body should include:
  - What changed
  - Why
  - Test evidence
  - Issue reference (`Closes #<number>` when applicable)

### 7) Link and Close Issue

- Ensure the PR is linked to the issue via GitHub keywords (`Closes #<number>`).
- If work is complete, mark issue checklist items done and close the issue.
- If partially complete, keep issue open and document remaining scope clearly.

## Default Enforcement Rules

- For issue-related requests, Codex should proactively execute the SOP without waiting for the user to restate it.
- If the user asks only to "fix issue #X", Codex still follows full SOP end-to-end.
- If a step cannot be completed (for example, no GitHub permission), Codex must:
  1. state the blocker,
  2. provide exact next command/action for the user,
  3. continue from the next feasible step.

## Non-Issue Tasks

For tasks not tied to a GitHub issue, Codex may use a simplified flow, but should still prefer:

- small scoped changes,
- local verification,
- clear commit/PR hygiene when requested.

