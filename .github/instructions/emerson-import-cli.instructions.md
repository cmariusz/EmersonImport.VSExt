---
applyTo: "Tools/**"
description: "CMsoft Import for PAC Machine Edition - the MCP server and the CLI bridge for scripts and agents"
---
<!-- cmsoft:managed emerson-import - Prepare Workspace of CMsoft Import for PAC Machine Edition updates this file; delete this line to keep your own version -->
# CMsoft Import for PAC Machine Edition — MCP Server and CLI Bridge

The extension exposes its `pme_*` tools to agents and scripts outside VS Code in two ways, both localhost-only
and protected by a per-session token. Both need a PRO license; without it every tool answers `LICENSE_REQUIRED`.
Inside VS Code use the Language Model Tools or `@pme` instead.

## MCP server (preferred for MCP-capable agents)

Enabled by default (`emersonImport.mcp.enabled`). While it runs, the extension writes `.pme/mcp.json` — in
its own storage and, while the workspace is used with the extension, also in the workspace (unless
`emersonImport.mcp.writeWorkspaceStateFile` is `false`):

```json
{ "version": 1, "host": "127.0.0.1", "port": 58470, "token": "...", "endpoint": "/mcp", "transport": "streamable-http" }
```

1. Read `.pme/mcp.json` before every session — never hard-code or commit the port or token.
2. Connect your MCP client to `http://<host>:<port>/mcp` with `Authorization: Bearer <token>`.
3. `tools/list`, then `tools/call` — start with `pme_connect`.
4. `GET /health` (no token) checks the server and lists the tools.

## CLI bridge

Opt-in (`emersonImport.cli.enabled`, or *Toggle CLI Bridge*). While it runs, the extension writes
`.pme/cli.json` (`{ version, host, port, token }`).

- `POST /api` with `Authorization: Bearer <token>`: `{ "command": "list_items", "args": {} }`.
- `GET /health` lists the commands without a token.
- Commands: the tool names with or without the `pme_` prefix, plus `current_project` and `get_logs`.
- Nothing has to be installed to call it: PowerShell `Invoke-RestMethod` or the Python standard library
  (`Tools/pme_cli_example.py` is an example). Never assume Node.js is installed.
- The extension also ships a client, `scripts/emerson-import-cli.js` in its installation folder. It runs on the runtime of
  VS Code: the `emerson-import` PowerShell function of the README starts `Code.exe` with `ELECTRON_RUN_AS_NODE=1` and pipes
  the output into `ForEach-Object` (PowerShell does not wait for a Windows program otherwise).

## Safety

- Both servers bind only to `127.0.0.1`; every request needs the per-session token.
- Over MCP and the CLI the tools run without confirmation dialogs: enabling them is the opt-in.
- Do not commit `.pme/`.
