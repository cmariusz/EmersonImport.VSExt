#!/usr/bin/env python3
# cmsoft:managed emerson-import - Prepare Workspace of CMsoft Import for PAC Machine Edition updates this file; delete this line to keep your own version
"""Minimal example client for the CLI bridge of CMsoft Import for PAC Machine Edition."""

import json
import pathlib
import urllib.request
from typing import Optional


def read_state(workspace: pathlib.Path) -> dict:
    state_path = workspace / ".pme" / "cli.json"
    if not state_path.exists():
        raise SystemExit(f"{state_path} not found - enable the CLI bridge (emersonImport.cli.enabled) in VS Code.")
    with state_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def api_call(state: dict, command: str, args: Optional[dict] = None) -> dict:
    url = f"http://{state['host']}:{state['port']}/api"
    payload = json.dumps({"command": command, "args": args or {}}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {state['token']}"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    # Adjust if your workspace is elsewhere.
    workspace = pathlib.Path(__file__).resolve().parent.parent
    state = read_state(workspace)

    print("Current project:")
    print(json.dumps(api_call(state, "current_project"), indent=2))

    devices = api_call(state, "list_devices")
    if not devices.get("success"):
        raise SystemExit(devices.get("error") or "Not connected - connect to PAC Machine Edition first.")
    plcs = [device for device in devices["data"] if device["kind"] == "plc"]
    if not plcs:
        raise SystemExit("The project has no PLC target.")

    print(f"\nItems of the target {plcs[0]['name']}:")
    items = api_call(state, "list_items", {"device": plcs[0]["name"]})
    for item in items.get("items", []):
        print(f"  {item['groupPath']:<12} {item['name']:<32} {item['language']}")


if __name__ == "__main__":
    main()
