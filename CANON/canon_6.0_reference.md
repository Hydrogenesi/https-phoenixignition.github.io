# Canon 6.0 Reference

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
CEREMONY: N/A (reference artifact)
LINEAGE: root
-->

## Overview

Canon 6.0 defines the scaling laws and operator constraints governing all artifacts
in the CVN·A_TUA_M system. Every artifact must declare conformance to Canon 6.0.

## Scale Bands

| Band | Scope |
|---|---|
| individual | Single operator or contributor |
| squad | Small team (2–12) |
| unit | Organizational unit (13–100) |
| network | Cross-unit or public (100+) |

## Canon Relationships

| Relationship | Meaning |
|---|---|
| compatible | Artifact uses Canon 6.0 without modification |
| extended | Artifact adds to Canon 6.0; extensions are declared |
| forked | Artifact diverges from Canon 6.0; divergence is declared |

## Scaling Invariants

1. An operator declared at `squad` scale may not act at `network` scale without
   explicit Canon extension.
2. Ceremonies may not mutate artifacts beyond their declared scale band.
3. All scale transitions must be logged and badged.

## Operator Constraints

- Operators must declare their scale band.
- Operators must declare their Canon relationship.
- Operators that violate scaling invariants are non-canonical.

## Artifact Header Template

Every canonical artifact must include the following metadata header:

```
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: <individual|squad|unit|network>
CANON_RELATIONSHIP: <compatible|extended|forked>
CEREMONY: <ceremony ID or N/A>
LINEAGE: <parent artifact(s) or root>
```
