# CLAUDE.md

Project: `placement-prep`, a Claude skill (SKILL.md + references/*.md) for BTech CSE placement prep. Content is markdown only; there is no build or test step.

## Model roles: Opus orchestrates, Sonnet codes

- **Opus (orchestrator)**: plans the work, decides file structure and routing, splits tasks, reviews diffs and decides what ships. Does not hand-write bulk content or scripts itself.
- **Sonnet (implementer)**: writes the content and code. Delegate with the Agent tool and `model: "sonnet"`: generating reference files, parsing/scraping scripts, bulk edits, formatting passes.
- Run independent Sonnet tasks in parallel (one message, several Agent calls). Give each a self-contained prompt: goal, exact file paths, format rules, and what to return.
- Opus verifies every Sonnet result before committing: read the output, spot-check facts, check size and format rules below.

## Commits

- Commit after each logical change, one concern per commit, so any step can be rolled back with `git revert`.
- Short imperative subject (e.g. `docs: add Striver A2Z sheet reference`). Never bundle unrelated changes.
- Do not push or open PRs unless asked.

## Content rules

- Keep reference files compact: bullet points, tables, one line per item. SKILL.md only routes; detail lives in `references/`.
- When adding a reference file, also update the routing table in `SKILL.md`, the structure tree in `README.md` and `WARP.md` if relevant.
- Follow the existing style: plain ASCII where possible, no filler, interview-oriented (definition, mechanism, example, follow-ups).
- Facts must be accurate. Do not invent problem names, links or complexities; derive from a source or state uncertainty.
