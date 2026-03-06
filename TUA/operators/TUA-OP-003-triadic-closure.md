# TUA-OP-003: Triadic Closure

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: unit
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: TUA-OP-002-cross-pillar-bind
-->

## Identity

**Operator ID:** TUA-OP-003  
**Short Name:** triadic-closure  
**Knot Phase Step:** T

## Description

Triadic Closure; enforce 120° symmetry and maximum contraction. This
operator closes the three-pillar structure by enforcing equal angular
distribution (120° between each pillar axis) and driving the knot to
maximum contraction, producing a stable triadic configuration.

## Inputs

| Input | Type | Description |
|---|---|---|
| `dual_binding` | record | Output from TUA-OP-002 |
| `third_pillar` | artifact | The third pillar completing the triad |
| `target_angle_deg` | number | Target symmetry angle; must equal 120 |

## Outputs

| Output | Type | Description |
|---|---|---|
| `triadic_knot` | record | Fully closed triadic structure |
| `symmetry_verified` | boolean | True when 120° symmetry is confirmed |
| `contraction_maximum` | boolean | True when maximum contraction is achieved |

## Verification Schema

<!-- anchor: verification-schema -->

| Field | Expected Value | Enforcement |
|---|---|---|
| `target_angle_deg` | `120` | Must equal exactly 120° |
| `symmetry_verified` | `true` | All three inter-pillar angles ≤ ±2° of 120° |
| `contraction_maximum` | `true` | Contraction factor reaches defined maximum |
| `pillar_count` | `3` | Exactly three pillars must be present |

## Invariants

1. Exactly three pillars must participate; no more, no fewer.
2. All inter-pillar angles must equal 120° (±2° tolerance).
3. Contraction must reach the maximum value defined by the Knot configuration.
4. This step is irreversible once `triadic_knot` is sealed.

## Failure Modes

- `WRONG_PILLAR_COUNT` — Raised when the triad does not have exactly three pillars.
- `SYMMETRY_VIOLATION` — Raised when any inter-pillar angle deviates beyond ±2°.
- `CONTRACTION_INCOMPLETE` — Raised when maximum contraction is not reached.
- `PRIOR_BINDING_INVALID` — Raised when the dual_binding input is malformed.

## Canon 6.0 Notes

This operator acts at `unit` scale due to the three-pillar coordination
requirement. Squad-scale applications require a declared Canon extension.
