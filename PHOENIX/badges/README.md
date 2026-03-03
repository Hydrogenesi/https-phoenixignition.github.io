# Phoenix Badges

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: network
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: root
-->

This directory contains machine-readable badge artifacts issued by the ceremony runner.

## Badge Types

| Badge | Meaning |
|---|---|
| `ORIGIN_ANCHORED` | Artifact declares valid origin |
| `CANON_6_COMPLIANT` | Artifact satisfies Canon 6.0 constraints |
| `CEREMONY_COMPLETE` | Artifact was produced or updated through a complete ceremony |
| `CONTINUITY_VERIFIED` | Lineage is intact and auditable |

## Naming Convention

`BADGE-<type>-<artifact-id>-<date>.md`

## Required Metadata

Every badge must include the canonical header (see `CANON/canon_6.0_reference.md`).

## Merge Requirement

All four badge types are required before a PR may be merged.
