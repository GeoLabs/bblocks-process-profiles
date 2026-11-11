#!/usr/bin/env python3
"""Check that every change to a process-type entry since a base commit is described by an action.

Decision Q3 of 2026-11-11. For each process profile, compare its `examples/process-type.json` and its
processDescription files (`processDescription.json`, `.raw.json`, `.inherited.json`, together the
field `processDescription`) between `--since` (default `ea01115`) and `--to` (default: the working
tree). A top-level field of the entry (other than `hasAction`) whose value differs is a changed
field. Its change date is the date of the last commit between the two that changed it (today for an
uncommitted change). The field is covered when the entry has a `pp:amendmentAction` dated on or after
that date whose description names the field (`usedEntityType` and `generatedEntityType` are also
named by "entity type"). Prints each changed field with the actions that cover it, then the number
of changed fields that no action covers; exits 1 when that number is not 0.

    python3 scripts/check_actions.py [--since ea01115] [--to HEAD] [--json]
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"^_sources/[^/]+/[^/]+/examples/(process-type\.json|processDescription(\.raw|\.inherited)?\.json)$")
AMENDMENT = "https://geolabs.github.io/bblocks-process-profiles/def/amendmentAction"
ALIASES = {"usedEntityType": ["entity type"], "generatedEntityType": ["entity type"]}
WORKTREE = "WORKTREE"


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def snapshot(ref):
    """{entry dir: {field: value}} at a commit, or in the working tree."""
    if ref == WORKTREE:
        files = {str(p.relative_to(ROOT)): p.read_text() for p in ROOT.glob("_sources/*/*/examples/*.json")
                 if PATTERN.match(str(p.relative_to(ROOT)))}
    else:
        names = [n for n in git("ls-tree", "-r", "--name-only", ref, "_sources").split("\n") if PATTERN.match(n)]
        batch = subprocess.run(["git", "-C", str(ROOT), "cat-file", "--batch"],
                               input="".join(f"{ref}:{n}\n" for n in names).encode(),
                               capture_output=True, check=True).stdout
        files, pos = {}, 0
        for n in names:
            header_end = batch.index(b"\n", pos)
            size = int(batch[pos:header_end].split()[2])
            files[n] = batch[header_end + 1:header_end + 1 + size].decode()
            pos = header_end + 1 + size + 1
    out = {}
    for name, text in files.items():
        entry, file = name.rsplit("/examples/", 1)
        fields = out.setdefault(entry, {})
        data = json.loads(text)
        if file == "process-type.json":
            for k, v in data.items():
                if k != "hasAction":
                    fields[k] = v
            fields["__actions__"] = data.get("hasAction", [])
        else:
            fields.setdefault("processDescription", {})[file] = data
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", default="ea01115")
    ap.add_argument("--to", default=WORKTREE, help="a commit, or WORKTREE (default)")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    a = ap.parse_args()

    commits = git("rev-list", "--reverse", f"{a.since}..{'HEAD' if a.to == WORKTREE else a.to}").split()
    states = [(a.since, None)]
    states += [(c, git("log", "-1", "--format=%cd", "--date=short", c).strip()) for c in commits]
    if a.to == WORKTREE:
        states.append((WORKTREE, datetime.date.today().isoformat()))
    snaps = [(ref, date, snapshot(ref)) for ref, date in states]
    base, target = snaps[0][2], snaps[-1][2]

    rows, uncovered = [], 0
    for entry in sorted(target):
        new, old = target[entry], base.get(entry, {})
        actions = [x for x in new.get("__actions__", []) if x.get("actionType") == AMENDMENT]
        for field in sorted(k for k in set(new) | set(old) if k != "__actions__" and new.get(k) != old.get(k)):
            dates = [date for (_, _, prev), (_, date, cur) in zip(snaps, snaps[1:])
                     if prev.get(entry, {}).get(field) != cur.get(entry, {}).get(field)]
            changed_on = max(dates)
            names = [field] + ALIASES.get(field, [])
            covering = [x["id"].rsplit("/", 1)[-1] + f" ({x.get('changeClassification')}, {x['startedAtTime'][:10]})"
                        for x in actions
                        if x["startedAtTime"][:10] >= changed_on
                        and any(re.search(r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])", x.get("description", ""))
                                for n in names)]
            uncovered += not covering
            rows.append({"entry": entry.replace("_sources/", ""), "field": field, "changed_on": changed_on,
                         "change": "added" if field not in old else "removed" if field not in new else "changed",
                         "actions": covering})
    if a.json:
        print(json.dumps({"since": a.since, "to": a.to, "changed_fields": len(rows), "uncovered": uncovered,
                          "rows": rows}, indent=2))
    else:
        for r in rows:
            print(f"{r['entry']:48s} {r['field']:22s} {r['change']:8s} {r['changed_on']}  "
                  + (", ".join(r["actions"]) or "NO ACTION"))
        print(f"\n{len(rows)} changed fields since {a.since}; {uncovered} with no action")
    return 1 if uncovered else 0


if __name__ == "__main__":
    sys.exit(main())
