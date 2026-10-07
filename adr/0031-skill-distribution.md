# ADR-0031: Distribute handbooks as agent skills through a marketplace

Status: Accepted

Date: 2026-10-06

Owner: @Slight76

## Context

ADR-0011 required agents to consume the standards through a pinned checkout and a bootstrap snippet. v0.3.0 also tracked byte-identical copies of one skill under `.agents/skills/`, `.claude/skills/`, and `.github/skills/`, kept in sync by `sync_skills.py`. Copilot CLI, the Copilot cloud agent, Claude Code, Codex, and `gh skill` each discover skills differently, and the team wants every agent to pull the handbooks without per-repository hand wiring.

## Decision

- Every handbook is an **Agent Plugins 1.0** plugin: `plugin.json` at the root plus one skill at `skills/<repo-name>/SKILL.md` with `references/` (task map, catalog digest). The skill name equals the repository name. No mirrored skill directories; `sync_skills.py` is deleted.
- `standards-marketplace/.claude-plugin/marketplace.json` (`name: slight76-standards`) lists the five plugins as `github` sources pinned by `ref` (tag) and `sha`. Copilot CLI and Claude Code add this marketplace and install by `<name>@slight76-standards`.
- `gh skill install Slight76/<repo> <repo> --scope user --pin v1.0.0` serves any agent that reads `.agents/skills` or `~/.copilot/skills`.
- The Copilot cloud agent gets skills from the consumer kit's `copilot-setup-steps.yml`, which checks out each pinned handbook into `.standards/` and copies `skills/*` into `.agents/skills/`.
- Consumers may commit `.github/copilot/settings.json` with `enabledPlugins` so every Copilot CLI user in that repository gets the handbooks.
- Skill descriptions are trigger-rich (what tasks they serve) and `SKILL.md` stays under 500 lines; detail goes in `references/`.

## Alternatives

- Keep mirrored skill directories in each repository: rejected; three copies to sync and still nothing for marketplace or `gh skill` users.
- One combined "all standards" skill: rejected; it reintroduces the oversized skill the split removed. The marketplace skill routes instead.
- Publish to a third-party registry: rejected; GitHub-native mechanisms cover every agent in use.

## Consequences

Releasing a handbook means tagging it and updating `sha` in the marketplace manifest. Skill content must stay accurate to `docs/` and `catalog/` (the digest is generated). Agents that cannot install skills still work through the pinned checkout path from ADR-0011.

## Traceability

ADR-0011; ADR-0024 (rule-scoped agent execution); [ADR-0029](0029-split-into-domain-handbooks.md); standards-marketplace README "Install the handbooks as agent skills".

## Verification

`copilot plugin marketplace add Slight76/standards-marketplace` and `copilot plugin install <name>@slight76-standards` succeed for all five; `gh skill preview Slight76/<repo>` lists the skill; Claude Code `/plugin install` succeeds; validator checks skill name, description length, and line count.

## Approval

@Slight76, 2026-10-06, planning session ("find a way to have all our agents pull skills from them").
