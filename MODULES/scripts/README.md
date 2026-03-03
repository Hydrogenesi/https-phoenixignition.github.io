# Modules — Scripts

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: network
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: root
-->

This directory contains enforcement scripts that automate ceremony and continuity
checks.

## Script Inventory

| Script | Purpose |
|---|---|
| `ceremony_runner` | Runs the four-phase Phoenix Quantumonix ceremony |
| `origin_check` | Pre-commit check: verifies origin anchor in changed artifacts |
| `canon_check` | Pre-commit check: verifies Canon 6.0 metadata in changed artifacts |
| `continuity_validator` | CI check: verifies lineage integrity across the repository |
| `badge_issuer` | Issues badges upon ceremony seal |

## Usage

```
./scripts/ceremony_runner --tension TENSION-YYYY-MM-DD-<name>.md
./scripts/origin_check
./scripts/canon_check
./scripts/continuity_validator
```

All scripts exit non-zero on failure to integrate with CI pipelines.
