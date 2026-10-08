# Contributing

Thanks for helping students prepare better. This is a Claude skill made of markdown files, so most contributions are content fixes and additions. There is no build or test step.

## Ways to help

- **Fix a mistake**: wrong complexity, wrong answer, outdated fact, broken link. These are the most valuable PRs.
- **Add questions**: company-wise interview questions, more practice problems, more worked examples.
- **Improve a pattern entry**: the pattern, idea and complexity per Striver problem live in `references/striver/*.md`.
- **Add a topic**: new subject or reference file (see the checklist below).
- **Report an issue**: wrong behaviour of the skill in a chat (tell us the prompt you used).

## Ground rules for content

- Accuracy first. Do not invent problem names, links, numbers or complexities. If unsure, say so or leave it out.
- Keep it compact: bullets, tables, one line per item. Interview-oriented: definition, how it works, example, follow-up questions.
- Plain ASCII where possible. Do not paste copyrighted text (full problem statements, book or course material). Link or name the source instead.
- `SKILL.md` only routes and defines behaviour; detail lives in `references/`. Keep `SKILL.md` under about 500 lines and its `description` under 1024 characters.
- Never commit secrets, personal data or large raw dumps (for example the full GSoC JSON).

## Adding a new reference file (checklist)

1. Create `references/<topic>.md` (or a folder if it is large).
2. Add a row for it in the routing table in `SKILL.md` so Claude knows when to load it.
3. Add it to the file tree and feature table in `README.md`.
4. If it is useful for quick revision, add a short section to `WARP.md`.
5. Check that every file path mentioned in `SKILL.md` exists.

## Striver sheet files

Each problem line in `references/striver/*.md` must keep the sheet's global number and exact title, in this format:

```
N. Title [B|P] | Pattern: <name> | Idea: <short insight> | TC O(..) SC O(..)
```

Do not add, remove or reorder problems. If you change a pattern name, update the Pattern Playbook table at the top of that file and the pattern map in `WARP.md` if it is listed there.

## GSoC data

Files in `references/gsoc/` are generated. Do not edit them by hand. To refresh them:

```bash
python -I scripts/build_gsoc.py
```

It downloads from `api.gsocorganizations.dev`. Run it once a year after the new GSoC organizations are announced, and commit the regenerated files.

## Commits and pull requests

- One logical change per commit, short imperative subject, for example `docs: fix Banker's algorithm example`.
- Open the PR against `main` and say what changed and how you checked it (source, calculation, or a run of the code).
- For code or SQL snippets, run them and mention the result in the PR.

## Working with Claude Code

If you use Claude Code on this repo, read `CLAUDE.md`. It describes the Opus (plan and review) and Sonnet (write) split and the commit rules used here.

## Code of conduct

Be kind and constructive. Students of all levels use this project.
