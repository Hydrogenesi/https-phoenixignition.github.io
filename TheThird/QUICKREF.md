# The Third - Quick Reference

Quick reference guide for using The Third pillar.

---

## Installation & Import

```python
# Basic imports
from TheThird.operators import bind, seal, converge, invariant, resolve
from TheThird.classes import Binder, InvariantEngine, Resolver, ConvergenceMap
```

---

## Operators Quick Reference

### bind(source, target, law=None)
**Purpose:** Establish structural relationships between pillars  
**Returns:** Dict with 'coherence', 'bound', 'law_applied'

```python
result = bind(phoenix_output, hydro_output)
# result['coherence'] → 'valid' | 'law_violation' | 'error'
```

### seal(state, invariants=None)
**Purpose:** Lock states with invariance guarantees  
**Returns:** Dict with 'seal_status', 'is_sealed', 'violations'

```python
result = seal(state, invariants=[check_func])
# result['is_sealed'] → True | False
```

### converge(*outputs, strategy="canonical")
**Purpose:** Resolve multi-pillar outputs into canonical form  
**Returns:** Dict with 'converged', 'convergence_status'  
**Strategies:** "canonical", "merge", "prioritize"

```python
result = converge(output1, output2, output3, strategy="canonical")
# result['converged'] → unified output
```

### invariant(structure, rules=None)
**Purpose:** Apply invariance rules across structures  
**Returns:** Dict with 'is_invariant', 'violations'

```python
result = invariant(structure, rules=[rule1, rule2])
# result['is_invariant'] → True | False
```

### resolve(interaction, deterministic=True)
**Purpose:** Finalize cross-pillar interactions  
**Returns:** Dict with 'resolved', 'resolution_status'

```python
interaction = {
    'pillars': ['phoenix', 'hydrogenesi'],
    'operation': 'transform',
    'inputs': {...}
}
result = resolve(interaction)
# result['resolved'] → final result
```

---

## Classes Quick Reference

### Binder
**Purpose:** Manage structural relationships with tracking

```python
binder = Binder(name="MyBinder", laws=[law_func])
result = binder.bind(source, target)
bindings = binder.get_bindings()
validation = binder.validate_all_bindings()
```

### InvariantEngine
**Purpose:** Enforce invariance with persistent rules

```python
engine = InvariantEngine(name="MyEngine")
engine.add_rule(rule_func)
result = engine.check(structure)
recursive_result = engine.check_recursive(structure, max_depth=10)
```

### Resolver
**Purpose:** Handle cross-pillar interactions with conflict detection

```python
resolver = Resolver(name="MyResolver", deterministic=True)
result = resolver.resolve(interaction)
conflicts = resolver.detect_conflicts(interaction1, interaction2)
```

### ConvergenceMap
**Purpose:** Track and analyze convergence patterns

```python
conv_map = ConvergenceMap(name="MyMap", default_strategy="canonical")
result = conv_map.converge(output1, output2, label="test")
analysis = conv_map.get_pattern_analysis()
by_strategy = conv_map.get_convergences_by_strategy("canonical")
```

---

## Common Patterns

### Pattern 1: Bind and Seal
```python
# Bind two outputs
binding = bind(phoenix_output, hydro_output)

# Seal the binding with invariants
sealed = seal(binding['bound'], invariants=[check_func])
```

### Pattern 2: Three-Pillar Convergence
```python
# Converge all three pillars
result = converge(
    phoenix_output,
    hydro_output,
    third_output,
    strategy="canonical"
)
```

### Pattern 3: Validate and Resolve
```python
# Check invariance
inv_result = invariant(structure, rules=[rule1, rule2])

# If invariant, resolve the interaction
if inv_result['is_invariant']:
    resolution = resolve(interaction, deterministic=True)
```

### Pattern 4: Full Workflow
```python
# 1. Bind
binding = bind(source, target, law=coherence_law)

# 2. Seal
sealed = seal(binding['bound'], invariants=[inv_check])

# 3. Converge
converged = converge(sealed['sealed_state'], other_output)

# 4. Validate
validated = invariant(converged['converged'], rules=[final_rule])

# 5. Resolve
if validated['is_invariant']:
    final = resolve({
        'pillars': ['phoenix', 'hydrogenesi', 'third'],
        'operation': 'finalize',
        'inputs': converged['converged']
    })
```

---

## Error Handling

All operators return status dictionaries. Check status fields:

```python
# Bind
if result['coherence'] == 'valid':
    # Success
elif result['coherence'] == 'law_violation':
    # Law was violated
    
# Seal
if result['is_sealed']:
    # Sealed successfully
else:
    # Check result['violations']
    
# Converge
if result['convergence_status'] == 'converged':
    # Converged successfully
    
# Invariant
if result['is_invariant']:
    # All rules passed
else:
    # Check result['violations']
    
# Resolve
if result['resolution_status'] == 'resolved':
    # Resolved successfully
```

---

## Validation

Run the validation suite:

```bash
python3 TheThird/validate.py
```

---

For detailed examples, see:
- `examples/binding_basic.md`
- `examples/invariance_demo.md`
- `examples/cross_pillar_resolution.md`
- `examples/convergence_flow.md`
