## CMsoft Import for PAC Machine Edition

PAC Machine Edition projects are imported into `PmeImport/` and exported back to PME with the **CMsoft Import for PAC Machine
Edition** VS Code extension. Read before working with these files:

- [.github/instructions/emerson-import.instructions.md](.github/instructions/emerson-import.instructions.md) — the workflow,
  the `pme_*` tools and the rules;
- [.github/instructions/emerson-import-cli.instructions.md](.github/instructions/emerson-import-cli.instructions.md) — the
  MCP server (`.pme/mcp.json`) and the CLI bridge for scripts and agents.

Conventions:

- Do not edit what the extension regenerates (its cache, the state files in `.pme/`).
- Keep changes scoped to the requested blocks; edit Structured Text in the `.st` files; after an export to
  PME always compile (`pme_compile`) and read the problems (`pme_get_problems`).
- PAC Machine Edition must be closed while the extension is connected — ask the user to close it, never end
  its processes.
- Never bypass a confirmation dialog.
