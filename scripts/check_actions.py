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

Decision R2 of 2026-11-12 adds, still commit by commit from `--since`:

- an entry removed: an entry of `--since` whose `process-type.json` is gone at `--to` fails, since no
  action can describe it any more;
- an action rewritten or removed: every action (`hasAction`, all types) is compared with its first
  recorded content in each commit; one whose content differs in any commit, even if reverted later, is
  rewritten, and one absent at `--to` is removed; both fail. An action absent in some commits and back
  with the same content is listed as restored, not failing (crop, absent in 632b881, back in 753b96d);
- a stricter match for every change made in a commit dated on or after STRICT_FROM (2026-11-12, and
  the working tree): each such commit that changes a field needs its own action, dated the day of
  that commit and naming the field; an action covers one change of a field only, so a second change
  of the field on the same day needs a second action;
- for every change, an action covers it only if it is not dated after the commit that adds it.

Remaining limit: before STRICT_FROM, an action dated on or after the last change of the field still
covers it (the rule of decision Q3). The stricter match cannot hold there without rewriting actions:
measured on 2026-11-12 (HEAD 3adbf2e), it would fail 24 of the 88 changed fields since ea01115. Five
changed only on 2026-11-10 and are described by the actions plan-2026-11-11, dated on the day of the
pin (the processDescription of estimate-biomass, export-stac, reproject-band and detect-water-body, the
assumedFormatGaps of reproject-band); 19 changed in more commits of a day than there are actions of
that day naming them. The classification of an action is not compared with the table of
pp:specification.

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
STRICT_FROM = "2026-11-12"   # decision R2: changes from this day on need an action of their own day


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

    # Entries removed since the base (decision R2): an entry whose process-type.json is gone.
    removed_entries = sorted(e.replace("_sources/", "") for e in base
                             if "__actions__" in base[e] and "__actions__" not in target.get(e, {}))

    # Actions rewritten or removed (decision R2), commit by commit; and the day each action is added.
    first, added_on, rewritten, restored, present = {}, {}, [], [], set()
    for ref, date, snap in snaps:
        now = {}
        for entry, fields in snap.items():
            for x in fields.get("__actions__", []):
                now[x["id"]] = (entry, json.dumps(x, sort_keys=True))
        for aid, (entry, content) in now.items():
            if aid not in first:
                first[aid] = (entry, content, ref)
                added_on[aid] = date
            elif content != first[aid][1] and aid not in {r["action"] for r in rewritten}:
                rewritten.append({"action": aid, "first_in": first[aid][2][:7], "rewritten_in": ref[:7]})
            elif aid not in present and ref != a.since:
                restored.append({"action": aid, "restored_in": ref[:7]})
        present = set(now)
    removed_actions = sorted(aid for aid in first if aid not in present)

    def names_field(x, field):
        return any(re.search(r"(?<![A-Za-z])" + re.escape(n) + r"(?![A-Za-z])", x.get("description", ""))
                   for n in [field] + ALIASES.get(field, []))

    def label(x):
        return x["id"].rsplit("/", 1)[-1] + f" ({x.get('changeClassification')}, {x['startedAtTime'][:10]})"

    rows, uncovered = [], 0
    for entry in sorted(target):
        new, old = target[entry], base.get(entry, {})
        # an action is not dated after the commit that adds it (added_on None: present at the base)
        actions = [x for x in new.get("__actions__", []) if x.get("actionType") == AMENDMENT
                   and (added_on.get(x["id"]) is None or x["startedAtTime"][:10] <= added_on[x["id"]])]
        for field in sorted(k for k in set(new) | set(old) if k != "__actions__" and new.get(k) != old.get(k)):
            dates = [date for (_, _, prev), (_, date, cur) in zip(snaps, snaps[1:])
                     if prev.get(entry, {}).get(field) != cur.get(entry, {}).get(field)]
            changed_on = max(dates)
            naming = [x for x in actions if names_field(x, field)]
            covering, missing = [], []
            # Before STRICT_FROM (decision Q3): one action dated on or after the last change.
            before = [d for d in dates if d < STRICT_FROM]
            if before:
                found = [x for x in naming if x["startedAtTime"][:10] >= max(before)]
                covering += [label(x) for x in found]
                if not found:
                    missing.append(f"{max(before)} (any action dated on or after)")
            # From STRICT_FROM (decision R2): each change its own action, dated that day.
            used = set()
            for d in (d for d in dates if d >= STRICT_FROM):
                found = next((x for x in naming if x["startedAtTime"][:10] == d and x["id"] not in used), None)
                if found:
                    used.add(found["id"])
                    covering.append(label(found))
                else:
                    missing.append(f"{d} (an action of its own, dated that day)")
            uncovered += bool(missing)
            rows.append({"entry": entry.replace("_sources/", ""), "field": field, "changed_on": changed_on,
                         "change": "added" if field not in old else "removed" if field not in new else "changed",
                         "changes": dates, "actions": sorted(set(covering)), "missing": missing})
    failed = uncovered + len(removed_entries) + len(rewritten) + len(removed_actions)
    if a.json:
        print(json.dumps({"since": a.since, "to": a.to, "strict_from": STRICT_FROM, "changed_fields": len(rows),
                          "uncovered": uncovered, "removed_entries": removed_entries, "rewritten_actions": rewritten,
                          "removed_actions": removed_actions, "restored_actions": restored, "rows": rows}, indent=2))
    else:
        for r in rows:
            print(f"{r['entry']:48s} {r['field']:22s} {r['change']:8s} {r['changed_on']}  "
                  + (", ".join(r["actions"]) or "NO ACTION")
                  + ("  MISSING " + "; ".join(r["missing"]) if r["missing"] and r["actions"] else ""))
        for e in removed_entries:
            print(f"ENTRY REMOVED {e}")
        for r in rewritten:
            print(f"ACTION REWRITTEN {r['action']} (first in {r['first_in']}, rewritten in {r['rewritten_in']})")
        for aid in removed_actions:
            print(f"ACTION REMOVED {aid}")
        for r in restored:
            print(f"action restored unchanged {r['action']} (in {r['restored_in']})")
        print(f"\n{len(rows)} changed fields since {a.since}; {uncovered} with no action; "
              f"{len(removed_entries)} entries removed; {len(rewritten)} actions rewritten; "
              f"{len(removed_actions)} actions removed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
