# Consumer kit: use the handbook from any application repo

Copy these files into each application repo so Copilot, Claude Code and Codex all find the handbook at the pinned commit.

| Kit file | Copy to | Used by |
| --- | --- | --- |
| `AGENTS.md.snippet` | append to `AGENTS.md` | Codex, Copilot, Claude Code (via import), others |
| `CLAUDE.md` | `CLAUDE.md` | Claude Code (`@AGENTS.md` import) |
| `copilot-instructions.md` | `.github/copilot-instructions.md` | Copilot |
| `copilot-setup-steps.yml` | `.github/workflows/copilot-setup-steps.yml` | Copilot cloud agent (checks out `.standards/`) |
| `skills/architecture-standards/` (this repo) | `.claude/skills/`, `.agents/skills/`, `.github/skills/` | on-demand routing (optional) |

Also commit `architecture-baseline.json` from the [baseline template](../templates/architecture-baseline.json) with a 40-character `standardsRevision`. See [adoption](../governance/adoption.md).

## Getting the pinned checkout into `.standards/`

Keep it inside the working tree: Claude Code asks approval for imports outside the working directory.

- **Submodule (default):** `git submodule add <standardsRepository> .standards`, then `git -C .standards checkout <standardsRevision>` and commit. Bumping the submodule pointer is the reviewed pin change. Clone with `--recurse-submodules` or run `git submodule update --init`.
- **Pinned clone:** `python scripts/fetch_standards.py` (copy it from this repo) reads the baseline and checks out the exact revision. Add `.standards/` to `.gitignore` and run it in setup/CI.

Keep `.standards/` and `architecture-baseline.json` in sync; the pin must never track `main`.

## Agent notes

- **Codex** reads `AGENTS.md` from the repo root to the working directory within a 32 KiB budget (`project_doc_max_bytes`); keep the snippet short. Cloud environments need a setup script that provides `.standards/`.
- **Claude Code** keeps files under about 200 lines; imports do not reduce context cost.
- **Copilot** does not reliably follow prose asking it to fetch other repositories; the setup-steps workflow materializes `.standards/` instead. A private standards repo needs a read-only `STANDARDS_REPO_TOKEN` secret.
- **Windows:** avoid symlinks for these files. With `core.symlinks` off, git writes a tiny text file and agents silently get no instructions.

## Smoke checks

- Codex: `codex "Summarize the current instructions."`
- Claude Code: `/context` shows `AGENTS.md` and `CLAUDE.md` loaded.
- Copilot CLI: `/instructions` lists the repo files.
- Ask any agent for the pinned revision and the first document it will read.
