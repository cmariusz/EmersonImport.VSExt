# Third-Party Notices

This project includes third-party components. Redistribution of this extension should preserve the applicable third-party license notices and terms.

> Informational notice: this file is a practical compliance aid and not legal advice.

## Project License

- This extension is proprietary commercial software licensed under the End User License Agreement (see `LICENSE.md`).
- The third-party components below keep their own licenses; the terms of `LICENSE.md` do not restrict your rights under them.

## Runtime dependencies (Node.js)

Bundled and minified into `out/extension.js` (esbuild) - their own `LICENSE` files are not part of the package, so their notices are reproduced in the last sections below:

- `@modelcontextprotocol/sdk` (1.32.2) — MIT — Copyright (c) 2024 Anthropic, PBC
- Transitive:
  - `@hono/node-server` (2.1.5) — MIT — Copyright (c) 2022 - present, Yusuke Wada and Hono contributors
  - `hono` (4.13.14) — MIT — Copyright (c) 2021 - present, Yusuke Wada and Hono contributors
  - `ajv` (8.20.0) — MIT — Copyright (c) 2015-2021 Evgeny Poberezkin
  - `ajv-formats` (3.0.1) — MIT — Copyright (c) 2020 Evgeny Poberezkin
  - `fast-deep-equal` (3.1.3) — MIT — Copyright (c) 2017 Evgeny Poberezkin
  - `json-schema-traverse` (1.0.0) — MIT — Copyright (c) 2017 Evgeny Poberezkin
  - `content-type` (1.0.5) — MIT — Copyright (c) 2015 Douglas Christopher Wilson
  - `zod` (4.6.7) — MIT — Copyright (c) 2025 Colin McDonnell
  - `zod-to-json-schema` (3.25.2) — ISC — Copyright (c) 2020, Stefan Terdell
  - `fast-uri` (3.1.9) — BSD-3-Clause — Copyright (c) 2011-2021, Gary Court; Copyright (c) 2021-present The Fastify team

## .NET host dependencies (NuGet)

- None is redistributed: `EmersonImportHost.exe` uses only assemblies of the .NET Framework 4.8 (`System.Management`, `System.Security`, `System.Web.Extensions`, `System.IO.Compression`, `Microsoft.CSharp`).
- `Obfuscar` — MIT — build time only, not distributed.

## Emerson PAC Machine Edition automation interface (critical)

- `CimplicityME.Application` (`FrameworX.exe`) — provided by the PAC Machine Edition installation
- `AutomationObjects.dll` and its type library — provided by the PAC Machine Edition installation
- Related Emerson libraries in the PAC Machine Edition installation directory

These components are provided by Emerson and are subject to the PAC Machine Edition end-user license agreement and/or applicable Emerson software terms. The extension binds to them at run time; *PAC Machine Edition* and *PACSystems* are trademarks of Emerson or its affiliates.

### Distribution policy for this extension

1. Do **not** redistribute PAC Machine Edition binaries (`FrameworX.exe`, `AutomationObjects.dll` or other files of the installation) as part of this extension package unless Emerson's terms explicitly allow it for your exact scenario.
2. Require end users to have their own valid PAC Machine Edition installation and license.
3. Keep Emerson package notices and terms available to recipients.
4. Verify export-control and regional restrictions where applicable.

## MIT, ISC and BSD-3-Clause components — required notices

### MIT License

Applies to `@modelcontextprotocol/sdk`, `@hono/node-server`, `hono`, `ajv`, `ajv-formats`, `fast-deep-equal`, `json-schema-traverse`, `content-type` and `zod`, each with the copyright notice listed in the table above.

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### ISC License — `zod-to-json-schema`

```text
Copyright (c) 2020, Stefan Terdell

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

### BSD 3-Clause License — `fast-uri`

```text
Copyright (c) 2011-2021, Gary Court until https://github.com/garycourt/uri-js/commit/a1acf730b4bba3f1097c9f52e7d9d3aba8cdcaae
Copyright (c) 2021-present The Fastify team <https://github.com/fastify/fastify#team>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * The names of any contributors may not be used to endorse or promote
      products derived from this software without specific prior written
      permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS AND CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The complete list of contributors can be found at:
- https://github.com/garycourt/uri-js/graphs/contributors
```

## Recommended compliance checklist

- Keep this `THIRD_PARTY_NOTICES.md` file in source and packaged artifacts.
- Preserve the project `LICENSE.md` file.
- Do not remove third-party copyright/license notices from redistributed artifacts.
- Re-run dependency license checks before each release (`npm` and `dotnet`) because dependency graphs can change: the packages above are those esbuild bundles into `out/extension.js` (its metafile), not every package in `package-lock.json`.
- Reject any new dependency under a copyleft license (GPL / LGPL / AGPL / SSPL) — it is incompatible with shipping this extension under a proprietary EULA.

## Audit basis (current snapshot, 2026-10-25)

- Node dependencies: the esbuild metafile of `out/extension.js` and the installed `node_modules` metadata (`package.json`, `LICENSE`).
- .NET dependencies from `dotnet/EmersonImportHost/EmersonImportHost.csproj` and the files of `bin/Release/net48` shipped in the VSIX (`EmersonImportHost.exe`, `EmersonImportHost.exe.config`).
