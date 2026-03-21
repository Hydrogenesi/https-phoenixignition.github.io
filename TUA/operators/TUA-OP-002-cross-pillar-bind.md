# TUA-OP-002: Cross-Pillar Bind

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: squad
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: TUA-OP-001-bind-pillar-knot
-->

## Identity

**Operator ID:** TUA-OP-002  
**Short Name:** cross-pillar-bind  
**Knot Phase Step:** C

## Description

Cross-pillar binding; ensure dual-corridor contraction. This operator
extends the initial pillar-Knot binding established in step B across a
second corridor, enforcing symmetric contraction along both binding paths.
The dual-corridor pattern guarantees structural coherence between the two
active pillars.

## Inputs

| Input | Type | Description |
|---|---|---|
| `binding` | record | Output binding record from TUA-OP-001 |
| `second_pillar` | artifact | The second pillar to bind across |
| `contraction_factor` | number | Symmetric contraction coefficient (0 < f ≤ 1) |

## Outputs

| Output | Type | Description |
|---|---|---|
| `dual_binding` | record | Cross-pillar binding spanning both corridors |
| `contraction_state` | record | Measured contraction along each corridor |

## Invariants

1. The binding record from TUA-OP-001 must be present and valid.
2. Both corridors must contract by equal magnitude (symmetric contraction).
3. Contraction factor must be strictly positive and no greater than 1.

## Failure Modes

- `PRIOR_BINDING_MISSING` — Raised when TUA-OP-001 binding is absent.
- `ASYMMETRIC_CONTRACTION` — Raised when corridor contraction magnitudes differ.
- `INVALID_CONTRACTION_FACTOR` — Raised when `contraction_factor` is out of range.

## Canon 6.0 Notes

This operator acts at `squad` scale. Cross-unit applications require an
explicit scale transition log and badge per the scaling invariants in
`CANON/canon_6.0_reference.md`.
