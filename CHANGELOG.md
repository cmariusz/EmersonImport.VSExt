# Changelog

## [1.2.1] - 2026-10-27

- **Public documentation repository** [EmersonImport.VSExt](https://github.com/cmariusz/EmersonImport.VSExt): its issue
  tracker is where questions and problem reports go — the *Q&A* and *Report Issue* links of the Marketplace page lead there
  (before, they led to a repository that is not public). Every release copies into it the README, this changelog, the
  license documents, the user manual with its screenshots and the instructions for AI assistants that **Prepare
  Workspace** writes.
- The README and the manual say which blocks are supported: Ladder (LD) and Structured Text (ST). Function Block
  Diagram (FBD) blocks and Sequential Function Charts (SFC) are not supported, and C blocks cannot be imported — PAC
  Machine Edition exports no XML for them.

## [1.2.0] - 2026-10-27

- **The variable list round-trips**: an export of `Variables.xml` leaves out the elements of structured variables and
  function block instances (`Pump1.Cmd`, `Pump1Ctl.Reset`) and the variables of function block types (`PumpFB.LastContactor`):
  PAC Machine Edition creates them with their variable. Up to 1.1 PAC Machine Edition rejected some of them and created a
  global variable for every other one (`Pump1_Cmd`, …): an unchanged list changed the project. Tested on copies of two
  projects (620 and 3590 elements left out, the list read back unchanged). **Variables** is no longer ticked by default in
  **Export Target Folder to PME**.
- **Export Target Folder to PME** on `Logic` or `Data Types` exports from the folder of the target with that part ticked; on
  any other folder it says that the folder holds nothing to export (before, it ended with *0 created, 0 updated* and wrote a
  backup). `pme_export_folder` / `export_folder` refuse such a folder with *Nothing to export* - nothing is changed.
- **Deleting blocks without a file**: the confirmation names the blocks it deletes; the option alone (without **Logic blocks**)
  is refused instead of doing nothing; an empty `Logic` folder never deletes a block. The confirmation names the parts in
  words (*data types and logic blocks*).
- **Export File to PME** shows its result (*LevelControl.st exported to Target1 - 0 created, 1 updated*); the question after an
  export reads *compile Target1 now?* for a file and a folder alike.
- **Auto Confirm Exports** no longer skips the confirmation of the hand-over to a PAC Machine Edition window (`pme_open_in_pme`).
- A walkthrough, **Get Started with CMsoft Import for PAC Machine Edition** (**Welcome: Open Walkthrough…**), with seven steps
  and links into the manual.
- The instructions of **Prepare Workspace** tell AI assistants that Structured Text of PAC Machine Edition 10.7 has no `TRUE` /
  `FALSE` (a BOOL is `1` / `0`), how a block declares a new variable, and the rules of the folder export.
- The log: a compilation that found errors no longer adds *Bridge Compile failed … unknown error*; a refusal of the FREE plan is
  logged once.

## [1.1.0] - 2026-10-26

- **User manual in the extension**: **Open User Manual** and **Search the User Manual** show the complete manual in VS Code's
  Markdown preview — 16 chapters and 6 appendices with 82 screenshots: installation, what PAC Machine Edition needs,
  connecting, import, export (a file, a target folder, new blocks, deleting blocks, hardware and EGD, the FREE limits),
  compiling and the **Problems** panel, a complete worked example from the import to a tested change, the Copilot tools
  and `@pme`, the MCP server (with Claude Code), the CLI bridge, settings, license and troubleshooting. Every example was run
  against a demo project in PAC Machine Edition 10.7. The VSIX of 1.0.0 held only the screenshots.
- The release builds the manual, and the VSIX check refuses a package without the manual of its version or with screenshots it
  does not link; a test checks every help topic against the headings of the shipped manual (two unused topics, `export` and
  `tutorial`, named headings that do not exist and were corrected).

## [1.0.0] - 2026-10-26

- First version: **CMsoft Import for PAC Machine Edition** works on Emerson PAC Machine Edition 10.x projects of
  PACSystems controllers from VS Code, through the automation interface of PME (`CimplicityME.Application`, started
  hidden; PME must be closed while the extension is connected).
- **Import** into the workspace (FREE, within the FREE plan limits): logic blocks as PLCopen XML as PME exports them, Structured Text also as
  a plain `.st` file, user defined data types, the variable list, the hardware configuration and Ethernet Global Data
  (`EGD.zip` and its `EGD.xml`) — one item, a target or every PLC target of the project. The `Logic` and `Data Types`
  folders mirror the project; unchanged blocks come out byte for byte the same.
- **Readable XML**: PME writes blocks, data types, `Variables.xml` and `Hardware.xml` on one line — the import indents
  them, one element per line (setting `emersonImport.formatXml`, on by default). Only the whitespace between elements
  is added: the export to PME removes it again, so PME reads exactly the file it wrote. Tested on PME 10.7 with two
  real projects: every indented file equals PME's export without the indentation; indented LD blocks, a data type, the
  variable list and the hardware configuration exported to PME and imported again come back unchanged.
- **Export** back to PME (FREE, within the FREE plan limits): a single file — an edited `.st` is merged into its block — or a whole target folder
  (data types → variables → blocks, each block after the function blocks it uses, hardware and EGD on request,
  optional deletion of blocks without a file, never `_MAIN`). A ZIP backup of the project before the first export of
  a session, the project saved after every export. When PME refuses a new block, the empty block it leaves behind is
  removed and the message says why (for example a function block that is not in the project yet).
- **Compile Target (Validate)** — PME's compiler: it checks the target and builds what changed since the last build;
  **Rebuild Target (Compile All Blocks)** does what *Clean Build Folders* + *Validate* do in PME (every block is
  compiled again; the compiled code stays the same). From the **Project** view (the icon of a target, right-click a
  target, a group or an item), the Explorer and the editor of an imported file (icon in the title bar, right-click),
  `pme_compile` (`rebuild`) for AI agents. Errors and warnings of PME in the **Problems** panel — a click opens the
  `.st` of an ST block at the line PME reports (PME writes `[ST block,'X': Line n]`; tested with errors on line 192
  and 794), the `.xml` of an LD block (the rung is in the message), `Hardware.xml`, `EGD.xml`, and the file of a
  function block that differs from the Toolchest; the log records how long the compilation took.
- **Connect** asks for the project first: the Windows file dialog opens in the PME project store — the `.SwxCF` of a
  project, or a project backup (`.zip`) — and only then PAC Machine Edition starts and opens it; nothing starts when the
  dialog is cancelled. **Select Project** and **Open Project File or Backup** use the same dialog.
- One connection at a time: Connect clicked again while PME starts, opens a project or closes starts no second
  session; connected already, the connection is kept (`pme_connect` opens `projectName` in it); a second VS Code window
  is told that PAC Machine Edition is connected in another window and offered **Connect Again**.
- Connect, opening a project and Disconnect show a notification with a progress bar and the current step, and a spinner
  in the **Connection** view, the **Project** view and the status bar item; the log records when each of them starts and
  how long it took.
- **Closing VS Code closes PME**: closing the window (or *Reload Window*) while connected quits the hidden PAC Machine
  Edition — the .NET host outlives VS Code, finishes the call in progress and quits PME (about 20 s); a window that
  connects meanwhile waits for it instead of reporting PME as busy. Before, VS Code ended the extension host 5 s after
  the window closed and the host with it, which left PME running hidden until the next Connect ended it. Tested by
  closing a VS Code window connected to a copy of a real project: host and PME gone after 21 s.
- **Back Up Project (ZIP)**, **Open Project File or Backup** (a backup is restored into the project store, never over
  a project), **Open Project in PAC Machine Edition** (hands the project over in a PME window and ends the session).
- The automation session keeps PME usable: the connection works only while PAC Machine Edition is closed — the
  Project view says so, and Connect asks to close an open PME window and offers **Connect Again** —, quits PME on disconnect,
  ends an orphaned automation instance of an earlier session, answers or cancels modal PME prompts (they would block
  for ever), restores the *Recent Projects* list of PME.
- Copilot Language Model tools (`pme_*`), the `@pme` chat participant, a localhost MCP server and an opt-in CLI bridge
  (PRO); **Prepare Workspace** (PRO) writes the instructions for AI agents — the PME file formats and rules — into the
  workspace.
- **FREE plan: 10 objects per import or export, 15 minutes between operations** — the same limits as in CMsoft Import
  for TiaPortal. In the FREE plan one operation (one command such as Import to Workspace, Import Target, Import Entire
  Project, Export File or Export Target Folder to PME) moves at most 10 objects in either direction (the AI tools are
  PRO): a block counts one (a block file with several POUs each), a data type one, the variable list, the
  hardware configuration and EGD one each. The next import or export is available 15 minutes after the previous one
  has ended, in every VS Code window and after a restart. An operation over the limit is refused before anything is
  read or changed — the .NET host checks every call, also of a folder export —, and the dialog says what the limit
  is and when the next operation is possible. The export to PME, PRO only before, is free within these limits; PRO
  and the free trial have no limits, demo mode neither.
- **Compile after an export is PRO**, as in CMsoft Import for TiaPortal: in the FREE plan the setting
  `emersonImport.compileAfterExport` acts as `never`; the first export of a session says so once, with **Compile Target
  (Validate)** (compiles the target now) and **Buy License**. Compile Target (Validate), Rebuild Target and `pme_compile`
  stay FREE; the license panel shows the row *Compile after an export*.
- CMsoft licensing (FREE / PRO, 14-day trial, monthly or yearly subscription), obfuscated .NET host (net48, x86).
- Legal documents, shipped with the extension and opened from the license panel: **End User License Agreement 1.0**,
  **Terms of Sale 1.0** and **Privacy Policy 1.0** (`LICENSE.md`, `TERMS.md`, `PRIVACY.md`), modelled on those of
  CMsoft Import for TiaPortal; licenses are issued to the company and country named in the order.
- Documentation of the detected PME automation API for developers (`Documentation/PME-Automation-API.md`, not part of
  the extension package).
- Created with the CMsoft `cmsoft-addon-create` skill (TIA Import architecture), without a GitHub workflow: no tests
  run on GitHub after a push, as in the other CMsoft add-ons — `npm run package` and `npm run release:vsix` run them on
  the developer machine.
