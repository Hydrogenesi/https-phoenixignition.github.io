# TUA-OP-004: Apex Knot

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: unit
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: TUA-OP-003-triadic-closure
-->

## Identity

**Operator ID:** TUA-OP-004  
**Short Name:** apex-knot  
**Knot Phase Step:** A

## Description

Apex Knot; lock fixed point. This operator designates and seals the apex
of the triadic structure as a fixed point, preventing further structural
mutation. Once the apex is locked, the Knot topology becomes invariant and
all subsequent operations must treat the apex as a reference anchor.

## Inputs

| Input | Type | Description |
|---|---|---|
| `triadic_knot` | record | Closed triadic structure from TUA-OP-003 |
| `apex_candidate` | reference | The pillar or intersection designated as apex |

## Outputs

| Output | Type | Description |
|---|---|---|
| `locked_knot` | record | Triadic knot with apex fixed and sealed |
| `fixed_point_id` | string | Identifier of the locked apex |

## Invariants

1. The triadic structure must be fully closed (TUA-OP-003 complete) before
   apex locking.
2. The apex candidate must be one of the three pillars or their intersection.
3. Once locked, the fixed point cannot be reassigned without a new ceremony.

## Failure Modes

- `TRIAD_OPEN` — Raised when triadic closure has not been verified.
- `INVALID_APEX` — Raised when the apex candidate is not part of the triad.
- `APEX_ALREADY_LOCKED` — Raised when a fixed point is already present.

## Canon 6.0 Notes

This operator acts at `unit` scale. The fixed-point lock is a state-sealing
action; any attempt to reverse it at `squad` scale without a Canon extension
is non-canonical.
