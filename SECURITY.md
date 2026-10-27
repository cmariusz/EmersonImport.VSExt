# Security Policy

**Product:** CMsoft Import for PAC Machine Edition — Visual Studio Code extension (`MariuszCzyrnek.emerson-import`)
**Manufacturer:** Mariusz Czyrnek CM-SOFT, trading as CMsoft, Kornatka 23, 32-410 Dobczyce, Poland, NIP (VAT-ID) PL 894-253-07-59
**Version:** 1.0 — 2026-10-25

This policy describes how CMsoft handles security vulnerabilities in the
Software, in line with the vulnerability-handling requirements of Regulation
(EU) 2024/2847 (Cyber Resilience Act).

## 1. Reporting a vulnerability

Send reports **confidentially** by e-mail to `office@cmsoft.com.pl` with the
subject starting with `[SECURITY]`. Please do not open a public issue for
security problems.

A useful report contains the affected extension version and the
PME / VS Code / Windows versions, a description of the problem
and its impact, steps to reproduce, whether you know of active exploitation,
and how you would like to be credited. Do not include real customer projects,
controller programs or credentials — a minimal reproduction is enough.

## 2. What happens next

| Step | Target |
| --- | --- |
| Acknowledgement of receipt | within **5 business days** |
| Initial assessment | within **15 business days** |
| Fix for a confirmed vulnerability | as soon as possible, normally within **90 days** |

If a fix depends on a third party (for example Emerson, Microsoft or an
open-source component), we agree an extended timeline with the reporter.

## 3. Scope

The extension code, its .NET host and the local servers it opens (MCP server
and CLI bridge: localhost only, random port, Bearer token). PAC Machine Edition itself
is out of scope — report its vulnerabilities to Emerson.
