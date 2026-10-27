# Changelog

## [1.3.0] - 2026-10-27

- **Exporting the variable list no longer changes the project**: `Variables.xml` goes to PAC Machine Edition without the
  elements of structured variables and function block instances (`Pump1.Cmd`, `Pump1Ctl.Reset`) and without the variables
  of function block types (`PumpFB.LastContactor`) — PAC Machine Edition creates them together with their variable. Before,
  it rejected some of them and created a global variable (`Pump1_Cmd`, …) for each of the others. **Variables** is no
  longer ticked by default in **Export Target Folder to PME**.
- **Export Target Folder to PME** on `Logic` or `Data Types` exports from the folder of the target with only that part
  ticked. On any other folder it says that the folder holds nothing to export and changes nothing; the AI tools and the CLI
  answer the same (*Nothing to export*).
- **Deleting blocks without a file**: the confirmation names the blocks that will be deleted; the option without **Logic
  blocks** is refused with a message instead of doing nothing; an empty `Logic` folder never deletes a block.
- **Clearer messages**: the confirmation of a folder export names the parts in words (*data types and logic blocks*);
  **Export File to PME** shows its result (*LevelControl.st exported to Target1 - 0 created, 1 updated*); the question after
  an export reads *compile Target1 now?* for a file and a folder alike.
- **Auto Confirm Exports** no longer skips the confirmation when an AI assistant hands the project over to a PAC Machine
  Edition window (`pme_open_in_pme`).
- **Walkthrough**: *Get Started with CMsoft Import for PAC Machine Edition* (**Welcome: Open Walkthrough…**) — seven steps
  with links into the manual.
- **Better instructions for AI assistants** (**Prepare Workspace**): Structured Text of PAC Machine Edition 10.7 has no
  `TRUE` / `FALSE` (a BOOL is `1` / `0`), how a block declares a new variable, and the rules of the folder export.
- **Log**: a compilation that found errors is no longer reported as a failed call, and a refusal of the FREE plan is
  logged once.

## [1.1.0] - 2026-10-26

- **User manual in the extension**: **Open User Manual** and **Search the User Manual** show the complete manual in VS
  Code's Markdown preview — installation, what PAC Machine Edition needs, connecting, import, export (a file, a target
  folder, new blocks, deleting blocks, hardware and EGD, the FREE limits), compiling and the **Problems** panel, a worked
  example from the import to a tested change, the Copilot tools and `@pme`, the MCP server, the CLI bridge, settings,
  license and troubleshooting.

## [1.0.0] - 2026-10-26

- **First version**: work on Emerson PAC Machine Edition 10.x projects of PACSystems controllers from VS Code. The
  extension drives PAC Machine Edition through its automation interface and starts it hidden; PAC Machine Edition must be
  closed while the extension is connected.
- **Import** into the workspace: logic blocks as PLCopen XML as PME exports them, Structured Text also as a plain `.st`
  file, user defined data types, the variable list, the hardware configuration and Ethernet Global Data (`EGD.zip` and its
  `EGD.xml`) — one item, a target or every PLC target of the project. The `Logic` and `Data Types` folders mirror the
  project; unchanged blocks come out byte for byte the same, so the folder can be kept under version control.
- **Readable XML**: PME writes blocks, data types, `Variables.xml` and `Hardware.xml` on one line — the import indents
  them, one element per line (setting `emersonImport.formatXml`, on by default). The export to PME removes the indentation
  again, so PME reads exactly the file it wrote.
- **Export** back to PME: a single file — an edited `.st` is merged into its block — or a whole target folder (data types →
  variables → blocks, each block after the function blocks it uses; hardware and EGD on request; optional deletion of
  blocks without a file, never `_MAIN`). A ZIP backup of the project is written before the first export of a session, and
  the project is saved after every export. When PME refuses a new block, the empty block it leaves behind is removed and
  the message says why (for example a function block that is not in the project yet).
- **Compile Target (Validate)** checks the target and builds what changed since the last build; **Rebuild Target (Compile
  All Blocks)** compiles every block again, like *Clean Build Folders* + *Validate* in PME. Both from the **Project** view,
  the Explorer and the editor of an imported file, and for AI agents (`pme_compile`). PME's errors and warnings appear in
  the **Problems** panel — a click opens the `.st` of an ST block at the line PME reports, the `.xml` of an LD block (the
  rung is in the message), `Hardware.xml`, `EGD.xml` or the file of a function block that differs from the Toolchest.
- **Connect** asks for the project first — the file dialog opens in the PME project store: the `.SwxCF` of a project or a
  project backup (`.zip`) — and only then starts PAC Machine Edition; nothing starts when the dialog is cancelled.
  **Select Project** and **Open Project File or Backup** use the same dialog.
- **One connection at a time**: clicking Connect again while PME starts, opens a project or closes starts no second
  session; a second VS Code window is told that PAC Machine Edition is connected in another window and offered **Connect
  Again**.
- **Progress**: Connect, opening a project and Disconnect show a notification with a progress bar and the current step,
  and a spinner in the **Connection** view, the **Project** view and the status bar.
- **Closing VS Code closes PME**: closing the window (or *Reload Window*) while connected also closes the hidden PAC Machine
  Edition, within about half a minute; a window that connects meanwhile waits until it has closed.
- **Back Up Project (ZIP)**, **Open Project File or Backup** (a backup is restored into the project store, never over a
  project) and **Open Project in PAC Machine Edition** (hands the project over to a PME window and ends the session).
- **PME stays usable**: the connection works only while PAC Machine Edition is closed — the **Project** view says so, and
  Connect asks to close an open PME window and offers **Connect Again**; Disconnect closes PME; a hidden PME left by an
  earlier session is ended; prompts of PME that would block are answered or cancelled; PME's *Recent Projects* list is not
  changed.
- **AI assistants (PRO)**: Copilot Language Model tools (`pme_*`), the `@pme` chat participant, a localhost MCP server and
  an opt-in CLI bridge; **Prepare Workspace** writes the instructions for AI agents — the PME file formats and rules — into
  the workspace.
- **FREE plan: 10 objects per import or export, 15 minutes between operations.** One operation (Import to Workspace,
  Import Target, Import Entire Project, Export File or Export Target Folder to PME) moves at most 10 objects in either
  direction: a block counts one (a block file with several POUs counts each), a data type one, the variable list, the
  hardware configuration and EGD one each. The next import or export is possible 15 minutes after the previous one has
  ended — in every VS Code window and after a restart. An operation over the limit is refused before anything is read or
  changed, and the dialog says what the limit is and when the next operation is possible. PRO and the free trial have no
  limits, demo mode neither.
- **Compile after an export is PRO**: in the FREE plan the setting `emersonImport.compileAfterExport` acts as `never`; the
  first export of a session says so once, with **Compile Target (Validate)** and **Buy License**. Compile Target (Validate),
  Rebuild Target and `pme_compile` stay FREE.
- **License**: FREE and PRO, a 14-day trial, monthly or yearly subscriptions; licenses are issued to the company and
  country named in the order. The End User License Agreement, the Terms of Sale and the Privacy Policy (`LICENSE.md`,
  `TERMS.md`, `PRIVACY.md`) ship with the extension and open from the license panel.
