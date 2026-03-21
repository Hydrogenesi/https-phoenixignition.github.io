# TUA-OP-001: Bind Pillar to Knot

<!--
ORIGIN: ORIGIN_CVN_ATUAM
CANON: 6.0
SCALE_BAND: squad
CANON_RELATIONSHIP: compatible
CEREMONY: N/A
LINEAGE: root
-->

## Identity

**Operator ID:** TUA-OP-001  
**Short Name:** bind-pillar-knot  
**Knot Phase Step:** B

## Description

Bind first pillar to Knot. This operator establishes the initial structural
link between the first pillar and the Knot, anchoring the sequence and
providing the foundational attachment point for subsequent cross-pillar
operations.

## Inputs

| Input | Type | Description |
|---|---|---|
| `pillar` | artifact | The first pillar artifact to be bound |
| `knot` | reference | The target Knot structure |

## Outputs

| Output | Type | Description |
|---|---|---|
| `binding` | record | The established pillar-to-Knot link |
| `anchor_id` | string | Unique identifier for the binding anchor |

## Invariants

1. The first pillar must be declared and non-null before binding.
2. The Knot must be initialized before the binding operation.
3. The resulting binding record is immutable after this step completes.

## Failure Modes

- `PILLAR_UNDEFINED` — Raised when the first pillar is not declared.
- `KNOT_UNINITIALIZED` — Raised when the Knot has not been established.
- `BINDING_CONFLICT` — Raised when a binding to the same anchor already exists.

## Canon 6.0 Notes

This operator acts at `squad` scale. To apply at `unit` or `network` scale,
declare a Canon extension per `CANON/canon_6.0_reference.md`.
