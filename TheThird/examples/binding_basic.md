# Binding Basic Example

This example demonstrates the basic binding operations of The Third pillar.

## Overview

The `bind` operator establishes structural relationships between Phoenix and Hydrogenesi outputs, ensuring cross-pillar coherence.

---

## Example 1: Simple Binding

```python
from TheThird.operators import bind

# Phoenix output
phoenix_output = {
    "ignition": "active",
    "energy": 144,
    "phase": "ascent"
}

# Hydrogenesi output
hydro_output = {
    "flow": "recursive",
    "depth": 3,
    "pattern": "spiral"
}

# Bind them together
result = bind(phoenix_output, hydro_output)

print(f"Binding Status: {result['coherence']}")
print(f"Bound Structure: {result['bound']}")
```

**Output:**
```
Binding Status: valid
Bound Structure: {
    'phoenix_source': {'ignition': 'active', 'energy': 144, 'phase': 'ascent'},
    'hydrogenesi_target': {'flow': 'recursive', 'depth': 3, 'pattern': 'spiral'},
    'binding_type': 'cross_pillar',
    'timestamp': 'sealed'
}
```

---

## Example 2: Binding with Law Enforcement

```python
from TheThird.operators import bind

# Define a law: energy must be positive
def energy_law(source, target):
    return source.get('energy', 0) > 0

phoenix_output = {"ignition": "active", "energy": 144}
hydro_output = {"flow": "recursive", "depth": 3}

# Bind with law enforcement
result = bind(phoenix_output, hydro_output, law=energy_law)

print(f"Law Applied: {result['law_applied']}")
print(f"Coherence: {result['coherence']}")
```

**Output:**
```
Law Applied: True
Coherence: valid
```

---

## Example 3: Using the Bind Class

```python
from TheThird.operators import Bind

# Create a Binder with a default law
def coherence_law(source, target):
    # Both must be dictionaries
    return isinstance(source, dict) and isinstance(target, dict)

binder = Bind(law=coherence_law)

# Perform multiple bindings
result1 = binder({"a": 1}, {"b": 2})
result2 = binder({"c": 3}, {"d": 4})

print(f"Bindings created: {len(binder.get_bindings())}")
print(f"First binding coherence: {result1['coherence']}")
```

**Output:**
```
Bindings created: 2
First binding coherence: valid
```

---

## Example 4: Law Violation

```python
from TheThird.operators import bind

# Define a strict law
def strict_energy_law(source, target):
    return source.get('energy', 0) >= 1000  # Very high threshold

phoenix_output = {"energy": 144}  # Too low
hydro_output = {"flow": "recursive"}

result = bind(phoenix_output, hydro_output, law=strict_energy_law)

print(f"Coherence: {result['coherence']}")
print(f"Error: {result.get('error', 'N/A')}")
```

**Output:**
```
Coherence: law_violation
Error: Law enforcement failed
```

---

## Key Concepts

1. **Basic Binding**: Connect outputs from different pillars
2. **Law Enforcement**: Apply rules during binding
3. **Coherence Checking**: Validate binding validity
4. **Stateful Binding**: Track multiple bindings with the Bind class

---

## Next Steps

- Explore `seal.py` for state sealing
- See `cross_pillar_resolution.md` for complex binding scenarios
- Review `converge.py` for multi-output convergence
