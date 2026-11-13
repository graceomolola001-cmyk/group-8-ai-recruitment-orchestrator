#!/usr/bin/env python3
"""Structural checks for publicly shared, sanitized n8n workflows."""
from pathlib import Path
import json
import sys

ERRORS = []
FORBIDDEN = {"credentials", "webhookId", "pinData", "staticData", "executionData"}

def walk(value, location):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in FORBIDDEN:
                ERRORS.append(f"{location}: disallowed field {key}")
            walk(item, f"{location}.{key}")
    elif isinstance(value, list):
        for number, item in enumerate(value):
            walk(item, f"{location}[{number}]")

files = sorted(Path("workflows").glob("*.json"))
if not files:
    ERRORS.append("No workflow JSON files found")
for file in files:
    try:
        data = json.loads(file.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("Workflow is not a JSON object")
        if not isinstance(data.get("nodes"), list):
            raise ValueError("Missing nodes array")
        if not isinstance(data.get("connections"), dict):
            raise ValueError("Missing connections object")
        if data.get("active") is not False:
            ERRORS.append(f"{file}: public templates must be inactive")
        walk(data, str(file))
        print(f"Checked {file}: {len(data['nodes'])} nodes")
    except (ValueError, OSError) as error:
        ERRORS.append(f"{file}: {error}")

for problem in ERRORS:
    print("FAIL:", problem, file=sys.stderr)
sys.exit(1 if ERRORS else 0)
