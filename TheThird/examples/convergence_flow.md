# Convergence Flow Example

This example demonstrates convergence operations using The Third pillar.

## Overview

The `converge` operator resolves multi-pillar outputs into a single canonical form. This ensures that disparate outputs from Phoenix, Hydrogenesi, and other sources are unified into a coherent result.

---

## Example 1: Basic Canonical Convergence

```python
from TheThird.operators import converge

# Outputs from different pillars
phoenix_output = {
    "type": "ignition",
    "energy": 144,
    "phase": "ascent"
}

hydro_output = {
    "type": "flow",
    "depth": 3,
    "pattern": "recursive"
}

# Converge into canonical form
result = converge(phoenix_output, hydro_output, strategy="canonical")

print(f"Convergence Status: {result['convergence_status']}")
print(f"Strategy Used: {result['strategy']}")
print(f"Converged Output: {result['converged']}")
```

**Output:**
```
Convergence Status: converged
Strategy Used: canonical
Converged Output: {
    'canonical_form': True,
    'pillar_count': 2,
    'unified_output': {
        'pillar_0': {'type': 'ignition', 'energy': 144, 'phase': 'ascent'},
        'pillar_1': {'type': 'flow', 'depth': 3, 'pattern': 'recursive'}
    }
}
```

---

## Example 2: Merge Strategy

```python
from TheThird.operators import converge

# Multiple outputs to merge
output1 = {"energy": 144, "source": "phoenix"}
output2 = {"depth": 3, "source": "hydrogenesi"}
output3 = {"sealed": True, "source": "third"}

# Merge all outputs
result = converge(output1, output2, output3, strategy="merge")

print(f"Merged Result: {result['converged']}")
print(f"Source Count: {result['sources']}")
```

**Output:**
```
Merged Result: {
    'energy': 144,
    'depth': 3,
    'sealed': True,
    'source': 'third'  # Last value wins in merge
}
Source Count: 3
```

---

## Example 3: Prioritize Strategy

```python
from TheThird.operators import converge

# Primary output (takes priority)
primary = {
    "energy": 144,
    "phase": "ignition",
    "priority": 1
}

# Supplementary outputs
supplement1 = {
    "depth": 3,
    "flow": "recursive"
}

supplement2 = {
    "seal": "active",
    "invariance": True
}

# Prioritize primary, supplement with others
result = converge(primary, supplement1, supplement2, strategy="prioritize")

print(f"Prioritized Result: {result['converged']}")
```

**Output:**
```
Prioritized Result: {
    'energy': 144,
    'phase': 'ignition',
    'priority': 1,
    'depth': 3,
    'flow': 'recursive',
    'seal': 'active',
    'invariance': True
}
```

---

## Example 4: Using the Converge Class

```python
from TheThird.operators import Converge

# Create a convergence operator
converger = Converge(default_strategy="canonical")

# Perform multiple convergences
result1 = converger({"a": 1}, {"b": 2})
result2 = converger({"c": 3}, {"d": 4}, {"e": 5})
result3 = converger({"f": 6}, {"g": 7}, strategy="merge")

print(f"Convergences performed: {converger.get_convergence_count()}")
print(f"Successful: {len(converger.get_successful_convergences())}")
```

**Output:**
```
Convergences performed: 3
Successful: 3
```

---

## Example 5: Three-Pillar Convergence

```python
from TheThird.operators import converge

# Complete three-pillar convergence
phoenix = {
    "pillar": "phoenix",
    "operation": "ignition",
    "energy": 144
}

hydrogenesi = {
    "pillar": "hydrogenesi",
    "operation": "recursion",
    "depth": 3
}

third = {
    "pillar": "third",
    "operation": "binding",
    "sealed": True
}

# Converge all three pillars
result = converge(phoenix, hydrogenesi, third, strategy="canonical")

print(f"Triad Convergence Complete")
print(f"Pillar Count: {result['converged']['pillar_count']}")
print(f"Canonical Form: {result['converged']['canonical_form']}")
```

**Output:**
```
Triad Convergence Complete
Pillar Count: 3
Canonical Form: True
```

---

## Example 6: ConvergenceMap with Pattern Analysis

```python
from TheThird.classes import ConvergenceMap

# Create a convergence map for tracking
conv_map = ConvergenceMap(name="TriadMap", default_strategy="canonical")

# Perform various convergences
conv_map.converge({"a": 1}, {"b": 2}, label="test1")
conv_map.converge({"c": 3}, {"d": 4}, strategy="merge", label="test2")
conv_map.converge({"e": 5}, {"f": 6}, {"g": 7}, label="test3")

# Analyze patterns
analysis = conv_map.get_pattern_analysis()

print(f"Total Convergences: {analysis['total_convergences']}")
print(f"Strategies Used: {analysis['strategies_used']}")
print(f"Patterns: {analysis['patterns']}")
```

**Output:**
```
Total Convergences: 3
Strategies Used: ['canonical', 'merge']
Patterns: {
    'canonical_2': 1,
    'merge_2': 1,
    'canonical_3': 1
}
```

---

## Example 7: Convergence Flow with Binding and Sealing

```python
from TheThird.operators import bind, seal, converge

# Step 1: Bind Phoenix and Hydrogenesi
phoenix = {"energy": 144}
hydro = {"depth": 3}
binding = bind(phoenix, hydro)

# Step 2: Seal the binding
sealed = seal(binding['bound'], invariants=[lambda s: s is not None])

# Step 3: Converge with Third pillar output
third_output = {"finalized": True}

result = converge(
    sealed['sealed_state'],
    third_output,
    strategy="canonical"
)

print(f"Complete Flow Status: {result['convergence_status']}")
print(f"Final Form: {result['converged']['canonical_form']}")
```

**Output:**
```
Complete Flow Status: converged
Final Form: True
```

---

## Example 8: Numeric Convergence

```python
from TheThird.classes import ConvergenceMap

# Create convergence map with average strategy
conv_map = ConvergenceMap(default_strategy="average")

# Converge numeric values
result = conv_map.converge(100, 200, 300, strategy="average")

print(f"Average: {result['converged']['average']}")
print(f"Count: {result['converged']['count']}")
```

**Output:**
```
Average: 200.0
Count: 3
```

---

## Convergence Strategies

### Canonical
- Creates structured form with all inputs preserved
- Best for: Complete record keeping, full traceability

### Merge
- Combines all dictionary outputs
- Best for: Unified state, consolidated data

### Prioritize
- First input takes priority, others supplement
- Best for: Hierarchical data, default values

### Average
- Averages numeric values
- Best for: Statistical aggregation, numeric synthesis

---

## Key Concepts

1. **Multi-Source Convergence**: Unifying outputs from multiple pillars
2. **Strategy Selection**: Different approaches for different needs
3. **Canonical Form**: Standard representation of converged data
4. **Pattern Tracking**: Analyzing convergence patterns over time
5. **Labeled Convergence**: Organizing convergences by purpose

---

## Convergence Flow Patterns

```
Phoenix Output ─┐
                ├─> Converge ─> Canonical Form
Hydro Output  ──┤
                │
Third Output  ──┘
```

---

## Next Steps

- Review `binding_basic.md` for binding fundamentals
- See `cross_pillar_resolution.md` for resolution patterns
- Explore `invariance_demo.md` for maintaining invariance
- Study the operator implementations for advanced patterns
