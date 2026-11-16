# Local build

## Default: published registers

Since 2026-11-12, `bblocks-data-types`, `bblocks-data-formats`, `bblocks-generic-profiles` and
`bblocks-process-profiles` are published on `geolabs.github.io`. `./build.sh` resolves every import
from its published `build/register.json`: no local configuration is needed.

A `bblocks-config-local.yml` left over from before that date maps those URLs to local builds that
may now be stale: delete it, or the build silently uses the old content.

## Testing an unpublished upstream change

To build against a change that is not yet published in an upstream register, map that register's
published URL to a local build with bblocks-postprocess url-mappings, in `bblocks-config-local.yml`
(git-ignored; the postprocessor reads that exact name, not `.yaml`). Copy
`bblocks-config-local.yml.example`, keep only the registers you changed, then mount each local
directory at the path it names (`docker run -v <dir>:/ext/...`, or a `.volumes` file read by
`build.sh`). Delete the file once the change is published.

**Upstream builds.** Build each changed upstream register first, in dependency order (data-types,
data-formats, generic-profiles, process-profiles), with its **published** URL as base URL, e.g.
`--base-url https://geolabs.github.io/bblocks-data-types/`, and map that URL to the local build.
The default `--base-url http://localhost:9090/register/` of `build.sh` writes localhost URLs into
`build-local/` (a data-types build made that way holds hundreds of them), which only resolve if
that build is served on port 9090 while the downstream register builds.

**The Registered Item Model mapping (removed 2026-11-12).** Until 2026-11-12 the Activity Type Register
`register.json` served on `ogcincubator.github.io/activity-type-register` imported the Registered Item Model
from `geonovum-labs.github.io`, and a local url-mapping replaced it with the `ogcincubator` model. The ATR
republished on 2026-11-12 (commit `4805673`) and now imports `ogcincubator.github.io/registered-item-model`,
so the mapping is gone. Check after any build: the reports name no `geonovum-labs` URL.
