# CMsoft Import for PAC Machine Edition

🌐 **[www.cmsoft.com.pl](https://www.cmsoft.com.pl)** — all CMsoft extensions, the shop and contact

<!-- VERSION-BADGE -->
[![Version](https://img.shields.io/badge/version-1.2.1-blue)](https://marketplace.visualstudio.com/items?itemName=MariuszCzyrnek.emerson-import)
<!-- /VERSION-BADGE -->

Import Emerson PAC Machine Edition projects into VS Code as PLCopen XML and Structured Text, edit them and export them back to PME - with Copilot tools, a chat assistant and an MCP server.

Work on your **PAC Machine Edition** (PME) PLC projects from Visual Studio Code: import the logic blocks,
data types, variables, hardware configuration and EGD of a PACSystems target into the workspace, edit them
with the tools you like — Copilot included —, export them back to PME, compile the target and read the
results in the **Problems** panel. Or let an AI agent do the round trip through the built-in Language Model
tools and MCP server.

> **Requirements:** Windows 10 or 11 and **PAC Machine Edition** (Emerson) installed and licensed — tested
> with version 10.7. The extension drives PME through its automation interface and does not replace it.
> Nothing else: no Node.js, npm or build tools — the extension comes ready to run.

## How it works with PAC Machine Edition

- **Connect** first asks which project to open — the Windows file dialog opens in your PME project store — and
  then starts PAC Machine Edition **hidden** and opens it.
  **Close PME before you connect:** its automation interface works only while no other PAC Machine Edition
  window is open — the extension tells you when one is. There is one connection at a time: while one VS Code
  window is connected, PME is not available to another one.
- Before the first export to PME of a session the extension writes a **ZIP backup** of the project into the
  backup folder of PME; every successful export is **saved** in the project (PME also saves the project before
  it compiles a target or backs the project up). **Disconnect** closes the hidden PME again.
- **Closing VS Code** (or *Reload Window*) while connected closes PME as well: the extension's background process
  quits it within about half a minute after the window is gone (the exports are saved already). A window that
  connects meanwhile waits until it has closed.
- **Open Project in PAC Machine Edition** hands the project over to you in a normal PME window — for example
  to download it to the controller — and ends the session.
- Projects the extension opens do not change the *Recent Projects* list of PME.

## Features

| | FREE | PRO |
|---|:-:|:-:|
| Connect, open projects of the PME project store or restore a project backup (.zip), browse targets, blocks and data types | ✅ | ✅ |
| Import into the workspace: logic blocks (PLCopen XML, Structured Text also as `.st`), data types, variables, hardware configuration, EGD | up to 10 objects per operation | ✅ unlimited |
| Export edited files back to PME — single files or a whole target folder | up to 10 objects per operation | ✅ unlimited |
| Next import or export | 15 minutes after the previous | ✅ at once |
| Compile a target (PME's Validate, or a rebuild of every block) — errors and warnings in the **Problems** panel | ✅ | ✅ |
| Compile after an export (`emersonImport.compileAfterExport`: ask / always) | ⛔ | ✅ |
| Back up the project (ZIP), open it in PAC Machine Edition | ✅ | ✅ |
| Copilot tools (`pme_*`), `@pme` chat participant, MCP server, CLI bridge | ⛔ | ✅ |
| Prepare Workspace — instructions for AI agents in the workspace | ⛔ | ✅ |

**FREE plan limits** — the same as in CMsoft Import for TiaPortal: one operation (one command such as importing
an item, a target or the whole project, or exporting a file or a target folder) moves at most 10 objects in
either direction — a block, a data type, the variable list, the hardware configuration and EGD count one each —,
and the next import or export is available 15 minutes after the previous one has ended, in every VS Code window
and after a restart. An operation over the limit is refused before anything is read or changed, and the dialog
says what the limit is and when the next operation is possible. PRO and the free trial have no limits.

PRO comes as a monthly or yearly subscription per seat, with a free trial — see
**CMsoft Import for PAC Machine Edition: Manage License / Subscription** and the shared **CMsoft** item in
the status bar.

## Getting started

1. Close PAC Machine Edition and open a folder in VS Code (the projects are imported into
   `<folder>/PmeImport/`).
2. Open the **CMsoft Import for PAC Machine Edition** view in the activity bar, click **Connect** and pick the
   `.SwxCF` file of the project in the dialog (it opens in the PME project store).
3. In the **Project** view, import a target (or a single block) into the workspace.
4. Edit the `.st` file of a Structured Text block (or another imported file) and right-click it →
   **Export File to PME** — or right-click the target → **Export Target Folder to PME** —, then
   **Compile Target (Validate)** — the icon in the title bar of the editor, or right-click the file or the
   target — and read the **Problems** panel.
5. **Disconnect** when you are done, or **Open Project in PAC Machine Edition** to continue in PME.

No PME at hand? Turn on `emersonImport.demoMode` and connect to a simulated project.

## Files in the workspace

```
PmeImport/<project>/<target>/
  Logic/<block>.xml        every Ladder and Structured Text block as PLCopen XML, as PME exports it - indented
  Logic/<block>.st         the Structured Text of an ST block - edit this file, the export puts it into the block
  Data Types/<type>.xml    user defined data types (PLCopen XML, indented)
  Variables.xml            the variable list (indented)
  Hardware.xml             the hardware configuration (indented)
  EGD.zip, EGD.xml         Ethernet Global Data - the archive PME reads, and its XML to read
```

PME writes these XML files on one line; the extension indents them — one element per line — so you can read,
compare and edit them. Nothing else changes: the export to PME removes the indentation again, and PME reads
exactly the file it wrote (`emersonImport.formatXml` off keeps PME's one-line files). Importing a target again
replaces these files and removes the files of blocks that no longer exist, so the folder can be kept under
version control: unchanged blocks come out byte for byte the same. Ladder (LD) blocks are imported as XML.
**Not supported:** Function Block Diagram (FBD) blocks and Sequential Function Charts (SFC — PME has them only
for Windows PC and QuickPanel Control targets, not for PACSystems), and C blocks: PME exports no XML for them.

## AI assistants

- **Copilot / VS Code chat:** the `pme_*` Language Model tools, or ask `@pme`. Exports to PME and the
  hand-over to PME ask for confirmation unless `emersonImport.lmTools.autoConfirmExports` is on.
- **MCP clients** (Claude Code, Claude Desktop, other agents): the extension runs a localhost MCP server
  (Streamable HTTP, `emersonImport.mcp.enabled`, on by default). The endpoint and its Bearer token are written
  to `.pme/mcp.json`. VS Code 1.99+ discovers it by itself. MCP clients act without confirmation dialogs.
- **Scripts** (PRO): the opt-in CLI bridge (`emersonImport.cli.enabled`), endpoint and token in
  `.pme/cli.json` — see below.
- **Prepare Workspace** (PRO) puts the instructions for AI agents into the workspace:
  `.github/instructions/emerson-import.instructions.md` (Copilot applies it to every file),
  `emerson-import-cli.instructions.md`, `Tools/pme_cli_example.py`, and a section of this extension in
  `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.gitignore` and `Tools/README.md` — next to
  the sections of the other CMsoft extensions; your own text stays.

The CLI bridge is plain HTTP, so any language works — PowerShell needs nothing else installed:

```powershell
$s = Get-Content .pme/cli.json | ConvertFrom-Json
$h = @{ Authorization = "Bearer $($s.token)" }
Invoke-RestMethod -Method Post -Uri "http://$($s.host):$($s.port)/api" -Headers $h -ContentType 'application/json' `
                  -Body '{"command":"current_project","args":{}}'
```

The extension also ships a command-line helper, which runs on the runtime built into VS Code — no Node.js
needed. Put this function into your PowerShell profile (`notepad $PROFILE`) and call it from the workspace
folder:

```powershell
function emerson-import {
    $cli = Get-ChildItem "$env:USERPROFILE\.vscode\extensions\MariuszCzyrnek.emerson-import-*\scripts\emerson-import-cli.js" |
           Sort-Object LastWriteTime | Select-Object -Last 1
    $code = Join-Path (Split-Path (Split-Path (Get-Command code).Source)) 'Code.exe'
    $env:ELECTRON_RUN_AS_NODE = '1'   # Code.exe works as Node.js while this is set
    try { & $code $cli.FullName @args | ForEach-Object { $_ } }   # the pipe makes PowerShell wait for the answer
    finally { Remove-Item Env:ELECTRON_RUN_AS_NODE }
}

emerson-import current_project --pretty
```

If VS Code was installed without *Add to PATH*, write the full path of `Code.exe` into `$code` (for an
installation for the current user `"$env:LOCALAPPDATA\Programs\Microsoft VS Code\Code.exe"`).

AI-generated changes are your responsibility: review and test them before they reach a real machine.

## Settings

| Setting | Default | |
|---|---|---|
| `emersonImport.demoMode` | `false` | simulated project instead of PME |
| `emersonImport.importFolderName` | `PmeImport` | folder in the workspace the projects are imported into |
| `emersonImport.autoConnect` | `false` | connect when a workspace opens |
| `emersonImport.formatXml` | `true` | import the XML indented (PME's one-line files when off) |
| `emersonImport.compileAfterExport` | `ask` | compile the target after an export to PME (PRO) |
| `emersonImport.lmTools.autoConfirmExports` | `false` | Copilot exports to PME without asking |
| `emersonImport.mcp.enabled` | `true` | localhost MCP server |
| `emersonImport.cli.enabled` | `false` | localhost CLI bridge (PRO) |
| `emersonImport.showDetails` | `false` | details of failed calls in the log |

## Troubleshooting

| Message | What to do |
|---|---|
| *Close PAC Machine Edition to connect* — *PAC Machine Edition is open (…)* | The connection works only while PAC Machine Edition is closed: the extension cannot connect to a PME window opened by hand. Save your work, close PME — also a window left by **Open Project in PAC Machine Edition** — and click **Connect Again**. |
| *PAC Machine Edition is already connected in another VS Code window* | PME serves one connection at a time. **Disconnect** in the other window (or close it) and click **Connect Again**. |
| *PAC Machine Edition was not found on this computer* | Install PAC Machine Edition; its setup registers the automation interface. |
| *… PAC Machine Edition showed: '…'* | PME asked a question the extension cannot answer, and the prompt was cancelled; the message quotes it. Open the project in PME to handle it there. |
| *PAC Machine Edition opens projects from its project store only* | Pick the `.SwxCF` of a project in the store, or a backup (`.zip`) — it is restored into the store. |
| Connect or Disconnect takes long | PME needs 10–35 s to start and up to half a minute to close; the notification, the **Connection** view and the status bar show the step, **Show Logs** each step with its time. |

To go back to an earlier state of a project, open one of the backups in the backup folder of PME with
**Open Project File or Backup** — a restore never overwrites a project, so rename or delete the project in PME
first.

## Support

Questions, problem reports and ideas go to the issue tracker of the public documentation repository
**[EmersonImport.VSExt](https://github.com/cmariusz/EmersonImport.VSExt/issues)** — it also holds this README,
the changelog, the license documents, the user manual and the instructions for AI assistants of every release.
An issue is public: do not attach projects, logs that name your projects or license keys — send them, and
security problems (`SECURITY.md`), by e-mail to [office@cmsoft.com.pl](mailto:office@cmsoft.com.pl).

## Privacy and licensing

The extension sends no telemetry and no project data; it works locally with PAC Machine Edition. What the
license functions send, and when, is described in the Privacy Policy (`PRIVACY.md`); the license terms are in
the End User License Agreement (`LICENSE.md`), the terms of sale in `TERMS.md`. The three ship with the
extension and the license panel opens them; how to report a vulnerability is in `SECURITY.md` in the
extension folder.

PAC Machine Edition and PACSystems are trademarks of Emerson or its affiliates. This extension is not affiliated
with or endorsed by Emerson.
