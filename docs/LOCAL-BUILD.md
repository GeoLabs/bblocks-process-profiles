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

## The KindGrove step CWL before its release (temporary)

`scripts/sources.yaml` pins the KindGrove step CWL on the GitHub Release `v0.0.2-rc2`, whose CWL
declares no `format`. The fix (GeoLabs/KindGrove `89e3d36`, branch `feature/cwl-format`, pushed: `format:
ogc:geotiff` on the GeoTIFF Files, `format: iana:application/geo+json` on the STAC Items; decision of
2026-11-10 on the formats invariant) is not released yet. Until `v0.0.2-rc3` is, the generator reads
the CWL generated locally from that commit through `scripts/sources-local.yaml` (git-ignored; copy
`scripts/sources-local.yaml.example`), and says so on stderr (`LOCAL OVERRIDE`). The committed pin
stays on rc2, so:

- the committed `_sources/kindgrove-steps/*` are those of the override: a regeneration without it
  differs, and stops on the formats rc2 does not declare (the format check of A4.3);
- the `executionUnit` links still point to the rc2 asset, whose CWL lacks the `format` lines.

To produce the CWL (the CI command of `.github/workflows/build-cwl-docker.yml`, with `--skip-build`
and the rc2 images, which the run record used):

```bash
git -C KindGrove archive 89e3d36 | tar -x -C kg && cd kg && mkdir -p myApplication/cwl_output && cd myApplication
cp ../*for_cwl.ipynb ../requirements.txt . ; cp -r ../steps ../cwl ../workflow.yml .
jupyter-repo2cwl . -o cwl_output --workflow-manifest workflow.yml \
  --docker-pull ghcr.io/geolabs/kindgrove/mangrove-cwl:v0.0.2-rc2 --per-step-images --skip-build
```

with `jupyter-repo2cwl` from `gfenoy/ipython2cwl` `5421312` (branch `feature/cwl-format`). Remove the override and update the pin
(`release`, `sha256`) once rc3 is released, and check it before any push.
