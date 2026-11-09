# Local build

## Build against unpublished registers

Until `bblocks-data-types`, `bblocks-data-formats` and `bblocks-generic-profiles` are published, a
build resolves them through bblocks-postprocess url-mappings, in `bblocks-config-local.yml`
(git-ignored; the postprocessor reads that exact name, not `.yaml`). Copy
`bblocks-config-local.yml.example`, then mount each local directory at the path it names
(`docker run -v <dir>:/ext/...`, or a `.volumes` file read by `build.sh`).

**Upstream builds.** Build each upstream register first, in dependency order (data-types,
data-formats, generic-profiles, process-profiles), with its **published** URL as base URL, e.g.
`--base-url https://geolabs.github.io/bblocks-data-types/`, and map that URL to the local build.
The default `--base-url http://localhost:9090/register/` of `build.sh` writes localhost URLs into
`build-local/` (a data-types build made that way holds hundreds of them), which only resolve if
that build is served on port 9090 while the downstream register builds.

**The Registered Item Model mapping (temporary).** The Activity Type Register `register.json`
served on `ogcincubator.github.io/activity-type-register` (last modified 2026-11-04) still imports
the Registered Item Model from `geonovum-labs.github.io`, while the ATR sources (commit `0c52c0e`:
`bblocks-config.yaml` and `build/register.json`) import it from `ogcincubator.github.io`. The
postprocessor loads that transitive import last, and it replaces the `ogcincubator` model for every
`ogc.rim.*` block. The example maps
`https://geonovum-labs.github.io/registered-item-model/build/` to a local copy of the
`ogcincubator` model's `build/` directory. To fetch it:

```bash
mkdir -p rim-ogc/build && cd rim-ogc
curl -sSfL -o build/register.json https://ogcincubator.github.io/registered-item-model/build/register.json
python3 - <<'PY'
import json, os, subprocess
base = "https://ogcincubator.github.io/registered-item-model/build/"
urls = set()
def walk(x):
    if isinstance(x, dict): [walk(v) for v in x.values()]
    elif isinstance(x, list): [walk(v) for v in x]
    elif isinstance(x, str) and x.startswith(base) and not x.endswith("/"): urls.add(x)
walk(json.load(open("build/register.json")))
for u in sorted(urls):
    p = "build/" + u[len(base):]
    os.makedirs(os.path.dirname(p), exist_ok=True)
    subprocess.run(["curl", "-sSfL", "-o", p, u])
PY
```

Remove this mapping once the ATR republishes its `register.json` from current sources; check it at
the end of the building-block production, before any push (decision D, 2026-11-09). Check: the build
reports name no `geonovum-labs` shape URL and the annotated `$ref`s none.
