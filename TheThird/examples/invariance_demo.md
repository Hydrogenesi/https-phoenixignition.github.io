# Invariance Demo

This example demonstrates the invariance enforcement capabilities of The Third pillar.

## Overview

The `invariant` operator applies invariance rules across recursive or multi-layer structures, ensuring structural properties remain constant across transformations.

---

## Example 1: Basic Invariance Check

```python
from TheThird.operators import invariant

# Define a structure
structure = {
    "energy": 144,
    "phase": "ignition",
    "coherent": True
}

# Define invariance rules
def check_positive_energy(s):
    return s.get("energy", 0) > 0

def check_coherence(s):
    return s.get("coherent", False) == True

# Apply invariance checks
result = invariant(structure, rules=[check_positive_energy, check_coherence])

print(f"Invariance Status: {result['invariance_status']}")
print(f"Is Invariant: {result['is_invariant']}")
print(f"Rules Passed: {len(result['rules_applied'])}")
```

**Output:**
```
Invariance Status: invariant
Is Invariant: True
Rules Passed: 2
```

---

## Example 2: Detecting Violations

```python
from TheThird.operators import invariant

# Structure with a violation
structure = {
    "energy": -50,  # Negative energy!
    "phase": "ignition"
}

# Rules
def check_positive_energy(s):
    return s.get("energy", 0) > 0

def check_has_phase(s):
    return "phase" in s

result = invariant(structure, rules=[check_positive_energy, check_has_phase])

print(f"Invariance Status: {result['invariance_status']}")
print(f"Violations: {len(result['violations'])}")
print(f"Violation Details: {result['violations']}")
```

**Output:**
```
Invariance Status: violation
Violations: 1
Violation Details: [{'rule_index': 0, 'status': 'violated', 'invariant_held': False}]
```

---

## Example 3: Recursive Invariance

```python
from TheThird.operators import check_recursive_invariance

# Nested structure
structure = {
    "layer1": {
        "energy": 100,
        "layer2": {
            "energy": 50,
            "layer3": {
                "energy": 25
            }
        }
    }
}

# Rule that must hold at all levels
def has_energy(s):
    if isinstance(s, dict):
        return "energy" in s or any(has_energy(v) for v in s.values())
    return False

# Check recursively
result = check_recursive_invariance(structure, has_energy, max_depth=5)

print(f"Recursive Invariance: {result}")
```

**Output:**
```
Recursive Invariance: True
```

---

## Example 4: Using the Invariant Class

```python
from TheThird.operators import Invariant

# Create an invariance engine with default rules
def energy_rule(s):
    return s.get("energy", 0) > 0

def coherence_rule(s):
    return isinstance(s, dict)

engine = Invariant(default_rules=[energy_rule, coherence_rule])

# Validate multiple structures
struct1 = {"energy": 144, "type": "phoenix"}
struct2 = {"energy": 72, "type": "hydro"}
struct3 = {"energy": -10, "type": "invalid"}  # Violation

result1 = engine(struct1)
result2 = engine(struct2)
result3 = engine(struct3)

print(f"Validations performed: {engine.get_validation_count()}")
print(f"Invariant count: {engine.get_invariant_count()}")
print(f"Third structure valid: {result3['is_invariant']}")
```

**Output:**
```
Validations performed: 3
Invariant count: 2
Third structure valid: False
```

---

## Example 5: Complex Multi-Layer Invariance

```python
from TheThird.operators import invariant

# Complex nested structure
structure = {
    "phoenix": {
        "ignition": "active",
        "energy": 144,
        "subsystems": {
            "core": {"temp": 1000},
            "shell": {"temp": 500}
        }
    },
    "hydrogenesi": {
        "flow": "recursive",
        "depth": 3
    }
}

# Multi-layer rules
def has_required_keys(s):
    return "phoenix" in s and "hydrogenesi" in s

def phoenix_active(s):
    phoenix = s.get("phoenix", {})
    return phoenix.get("ignition") == "active"

def energy_positive(s):
    phoenix = s.get("phoenix", {})
    return phoenix.get("energy", 0) > 0

result = invariant(
    structure, 
    rules=[has_required_keys, phoenix_active, energy_positive]
)

print(f"Invariance Status: {result['invariance_status']}")
print(f"All rules passed: {result['is_invariant']}")
```

**Output:**
```
Invariance Status: invariant
All rules passed: True
```

---

## Key Concepts

1. **Invariance Rules**: Functions that validate structural properties
2. **Violation Detection**: Identify when invariance is broken
3. **Recursive Validation**: Check invariance at all nesting levels
4. **Stateful Checking**: Track validation history with Invariant class
5. **Multi-Layer Rules**: Validate complex nested structures

---

## Next Steps

- See `seal.md` for combining invariance with state sealing
- Explore `cross_pillar_resolution.md` for invariance in cross-pillar contexts
- Review `convergence_flow.md` for maintaining invariance during convergence
