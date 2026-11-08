#!/usr/bin/env python3
"""Validate this skill's file structure and checklist CSV header. No external dependencies.

This is a structural smoke check, NOT a test of the SUT or browser integration.
"""
from pathlib import Path
import csv
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = [
    SKILL,
    ROOT / "references" / "gui-criteria.md",
    ROOT / "assets" / "checklist-template.csv",
    ROOT / "assets" / "bug-report-template.md",
    ROOT / "assets" / "execution-summary-template.md",
]
EXPECTED_HEADER = [
    "ID", "Category", "Screen", "Checkpoint", "Precondition", "Steps",
    "Expected Result", "Actual Result", "Status", "Environment",
    "Executed At", "Evidence", "Notes",
]

def main():
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
    if missing:
        print("FAIL missing files:", ", ".join(missing))
        return 1
    content = SKILL.read_text(encoding="utf-8")
    fm = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not fm:
        print("FAIL SKILL.md: missing YAML front matter")
        return 1
    fields = {}
    for line in fm.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if fields.get("name") != "gui-checklist-auditor" or not fields.get("description"):
        print("FAIL SKILL.md: name/description invalid")
        return 1
    with (ROOT / "assets" / "checklist-template.csv").open(encoding="utf-8", newline="") as f:
        header = next(csv.reader(f), [])
    if header != EXPECTED_HEADER:
        print("FAIL checklist-template.csv: unexpected header", header)
        return 1
    for word in ("design", "execute", "compare", "report"):
        if word not in content:
            print("FAIL SKILL.md: missing workflow stage", word)
            return 1
    if re.search(r"^### Stage \d+ — `explore`", content, re.M):
        print("FAIL SKILL.md: explore stage must not be present")
        return 1
    print("PASS: skill structure, front matter, 4 workflow stages, and CSV template")
    print("NOTE: no browser/SUT tests have been executed by this validator")
    return 0

if __name__ == "__main__":
    sys.exit(main())
