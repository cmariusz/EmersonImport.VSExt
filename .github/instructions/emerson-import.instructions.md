---
applyTo: "**"
description: "CMsoft Import for PAC Machine Edition - PAC Machine Edition project files in the workspace: workflow, pme_* tools and rules"
---
<!-- cmsoft:managed emerson-import - Prepare Workspace of CMsoft Import for PAC Machine Edition updates this file; delete this line to keep your own version -->
# CMsoft Import for PAC Machine Edition — Workspace Instructions

The **CMsoft Import for PAC Machine Edition** VS Code extension imports Emerson PAC Machine Edition (PME) projects of
PACSystems controllers into this workspace and exports edited files back to PME. It drives PME through its automation
interface: PME runs **hidden** while the extension is connected, and **no other PME window may be open** then.
Words: **import** = PME → workspace, **export** = workspace → PME.

## Project Description

The file `.github/ProjectDescription.md` describes the automation project of this workspace. It is shared with the
other CMsoft add-ons of the workspace — keep their parts.

**Rule:** When a change affects the structure of the project (blocks added, removed or renamed, communication,
data flow), **always** update `.github/ProjectDescription.md`.

**Rule:** If `.github/ProjectDescription.md` is empty, still the template text or does not exist, and you analyze
the project, **always** fill it in before proceeding — with **Mermaid diagrams** of the structure, the
communication and the data flow.

## Workspace layout

| Path | Content |
| --- | --- |
| `PmeImport/<project>/<target>/Logic/<block>.xml` | Every logic block as PLCopen XML (TC6), as PME exports it — indented, one element per line: the interface (parameters, local variables), vendor data (`<addData name="www.ge-ip.com">`) and the body. |
| `PmeImport/<project>/<target>/Logic/<block>.st` | The Structured Text of an ST block as plain text — **the file to edit** for ST logic. |
| `PmeImport/<project>/<target>/Data Types/<type>.xml` | User defined data types (PLCopen `<dataTypes>`). |
| `PmeImport/<project>/<target>/Variables.xml` | The variable list of the target (`<Variables><Variable>` with name, data type, address, description, …). |
| `PmeImport/<project>/<target>/Hardware.xml` | The hardware configuration (racks, slots, modules, parameters). |
| `PmeImport/<project>/<target>/EGD.zip`, `EGD.xml` | Ethernet Global Data: the archive PME reads and its XML. |
| `.pme/` | State files of the MCP server and the CLI bridge (port, token) — never commit them. |
| `Tools/`, `UserFiles/` | Your scripts and their output (`UserFiles/` is git-ignored). |

`PmeImport` is the default of the setting `emersonImport.importFolderName`. Importing a target again replaces its
files and removes the files of blocks that no longer exist; unchanged blocks come out byte for byte the same, so the
folder can be kept under version control. PME writes its XML on one line: the extension indents the blocks, data
types, `Variables.xml` and `Hardware.xml` (setting `emersonImport.formatXml`) and removes that indentation again when
it exports a file to PME.

## Workflow

1. **Connect**: `pme_connect` (with `projectName`), or `pme_connect`, `pme_list_projects`, `pme_select_project`.
   The connection works only while PAC Machine Edition is closed: if it answers that *PAC Machine Edition is open*,
   ask the user to save their work and close PME, then connect again — never end PME processes yourself.
   There is one connection at a time: `pme_connect` while connected keeps it and opens `projectName` in it; if it
   answers that PAC Machine Edition is connected in another VS Code window, ask the user to disconnect there.
2. **Inspect**: `pme_list_devices` (targets; import and export work with `plc` targets), `pme_list_items`
   (blocks with their language, data types, Variables, Hardware, EGD).
3. **Import** into the workspace: `pme_import_device` (a whole target), `pme_import_item` (one item),
   `pme_import_project` (every PLC target).
4. **Edit** the imported files — see the rules below.
5. **Export** back to PME: `pme_export_file` (one file) or `pme_export_folder` (a target folder: data types →
   variables → blocks; hardware and EGD only when `parts` names them). The extension backs the project up (ZIP in
   the backup folder of PME) before the first export of a session and saves the project after every export.
6. **Compile**: `pme_compile` (PME's Validate — it compiles what changed since the last build; `rebuild: true`
   compiles every block again), then `pme_get_problems` — problems of ST blocks point to lines of the `.st` file,
   problems of LD blocks name the rung. It compiles the project in PME: export the edited files first. Fix and
   repeat until there are no errors.
7. **Finish**: `pme_disconnect` (the user can open PME again), or `pme_open_in_pme` when the user wants to continue
   in PAC Machine Edition — for example to download the project to the controller.

## Rules for the files

- **Structured Text:** edit the `.st` file, never the `<body><st>` of the `.xml` (PME stores it doubly encoded;
  the export puts the text of the `.st` into the block). The `.st` holds the body only — parameters and local
  variables are in the `<interface>` of the block's `.xml`.
- **Structured Text of PAC Machine Edition 10.7:** a BOOL takes `1` / `0` — `TRUE`, `FALSE` and `ON` are reported as
  *Error 8004: Unknown variable* by the validation. A block is called as `Name();`, a function block instance as
  `Instance(In := x, …);`, and its outputs are read as `Instance.Out`.
- **A variable the code uses must exist:** a global one in `Variables.xml` (export the variables before the
  blocks — `pme_export_folder` does it in this order) or in the `<globalVars>` of the `<interface>` of the block's
  `.xml` (PME creates it with the block), a parameter or local variable in the `<interface>` of the block. A block
  export keeps the definition PME already has of a variable of the same name.
- **Elements in `Variables.xml`:** the elements of a structured variable or a function block instance (`Pump1.Cmd`,
  nested in their variable) are not exported — PME creates them with their variable. Change them in PME or in the
  data type.
- **A new ST block:** copy the `.xml` and `.st` of a similar block, rename both files and the `pou name` inside the
  `.xml`, adapt the `<interface>`, then export the `.st`. Afterwards `pme_refresh`.
- **Ladder, FBD and IL blocks** are XML with the graphical layout: read them to understand the logic; change them
  only when the user asks for it, in small steps, and validate each one.
- **XML layout:** the whitespace between elements does not matter — the export to PME removes it. The whitespace
  inside an element that holds text is its value: never wrap or indent the text of an element (`<st>`, `<Name>`,
  `<Description>`, `<documentation>` …) onto lines of its own, and never re-encode a file. Keep the file names — the
  file name is the block or type name (names are case-insensitive in PME).
- `Hardware.xml` and `EGD` change the controller configuration: export them only when the user asks for it.
- `pme_export_folder` with `deleteMissing` deletes the blocks that have no `.xml` in `Logic/` (never `_MAIN`; it needs
  the part `blocks`, and an empty `Logic/` deletes nothing): use it only when the user asks for blocks to be removed.
- `pme_export_folder` takes the folder of a target (`PmeImport/<project>/<target>`), not `Logic/` below it.

## Rules

- Always connect first; after every export compile (`pme_compile`) and read the problems (`pme_get_problems`).
- Never bypass a confirmation dialog and never delete or move user files unless asked.
- After changes made directly in PME, import again (or `pme_refresh`) before you edit: ids from before may be
  stale.
- The extension does not download to a controller: the user compiles and downloads in PME — a change reaches a
  real machine only after the user has reviewed and tested it.
