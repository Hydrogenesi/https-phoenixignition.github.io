# TUA-OP-005: Stability Knot

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: network
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: TUA-OP-004-apex-knot
-->

## Identity

**Operator ID:** TUA-OP-005  
**Short Name:** stability-knot  
**Knot Phase Step:** S

## Description

Stability Knot; enforce stability band. This operator concludes the
knot_phase sequence by enforcing a defined stability band around the locked
triadic structure. The stability band defines the permissible perturbation
range; any external force that would move the Knot outside this band is
rejected. This is the final sealing step of the knot_phase.

## Inputs

| Input | Type | Description |
|---|---|---|
| `locked_knot` | record | Apex-locked knot from TUA-OP-004 |
| `stability_band` | range | Permissible perturbation range `[lower, upper]` |

## Outputs

| Output | Type | Description |
|---|---|---|
| `stable_knot` | record | Knot sealed within its stability band |
| `band_enforced` | boolean | True when the stability band is active |
| `knot_phase_complete` | boolean | True when the full B→C→T→A→S sequence is verified |

## Invariants

1. The locked knot (apex fixed) must be present before the stability band
   is applied.
2. The stability band must be non-degenerate (`lower < upper`).
3. `knot_phase_complete` is set to `true` only when all prior steps
   (B, C, T, A) have been successfully recorded.
4. The `stable_knot` artifact is append-only after sealing.

## Failure Modes

- `KNOT_NOT_LOCKED` — Raised when the apex has not been fixed by TUA-OP-004.
- `DEGENERATE_BAND` — Raised when `lower >= upper` in the stability band.
- `SEQUENCE_INCOMPLETE` — Raised when one or more of steps B, C, T, or A
  has not completed successfully.

## Canon 6.0 Notes

This operator acts at `network` scale because the stability guarantee
must hold across all scale bands. It is the capstone operator of the
knot_phase and its output must be logged per `PHOENIX/logs/` conventions
and badged per `PHOENIX/badges/` requirements before the knot_phase is
considered canonical.
