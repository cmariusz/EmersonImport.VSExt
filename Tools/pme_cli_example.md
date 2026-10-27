<!-- cmsoft:managed emerson-import - Prepare Workspace of CMsoft Import for PAC Machine Edition updates this file; delete this line to keep your own version -->
# CLI Example — CMsoft Import for PAC Machine Edition

`pme_cli_example.py` is a minimal Python client for the CLI bridge of CMsoft Import for PAC Machine Edition.

## Requirements

- Python 3.8+ and a PRO license of CMsoft Import for PAC Machine Edition.
- The CLI bridge enabled in VS Code (`emersonImport.cli.enabled` or *Toggle CLI Bridge*).

## What it does

1. Reads the port and token from `.pme/cli.json` in the workspace.
2. Calls `current_project` — the connection and the selected project.
3. Calls `list_devices` and `list_items` — the blocks, data types and other items of the first PLC target.

## Usage

```powershell
python Tools/pme_cli_example.py
```

## Safety

- The bridge binds only to `127.0.0.1`; read `.pme/cli.json` at runtime — never hard-code the token.
- Do not commit `.pme/`.
