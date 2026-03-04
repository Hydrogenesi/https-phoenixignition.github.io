"""
invariant.py - The Invariance Operator

Applies invariance rules across recursive or multi-layer structures.
Ensures structural properties remain constant across transformations.
"""

from typing import Any, Optional, List, Dict, Callable


def invariant(structure: Any, rules: Optional[List[Callable]] = None) -> Dict[str, Any]:
    """
    Apply invariance rules to a structure.
    
    The invariant operator validates that a structure maintains specified
    invariance properties across all layers and transformations.
    
    Parameters:
    -----------
    structure : Any
        The structure to validate
    rules : Optional[List[Callable]]
        List of invariance rule functions
        Each function should accept the structure and return bool
        
    Returns:
    --------
    Dict[str, Any]
        An invariance result containing:
        - structure: The validated structure
        - rules_applied: List of applied rules
        - invariance_status: Overall status
        - violations: Any rule violations
    
    Examples:
    ---------
    >>> struct = {"layers": [1, 2, 3], "coherent": True}
    >>> def check_coherence(s): return s.get("coherent", False)
    >>> result = invariant(struct, rules=[check_coherence])
    >>> result['invariance_status']
    'invariant'
    """
    if rules is None:
        rules = []
    
    rules_applied = []
    violations = []
    
    # Apply each invariance rule
    for i, rule in enumerate(rules):
        try:
            if rule(structure):
                rules_applied.append({
                    'rule_index': i,
                    'status': 'valid',
                    'invariant_held': True
                })
            else:
                violations.append({
                    'rule_index': i,
                    'status': 'violated',
                    'invariant_held': False
                })
        except Exception as e:
            violations.append({
                'rule_index': i,
                'status': 'error',
                'error': str(e),
                'invariant_held': False
            })
    
    # Determine overall status
    if violations:
        invariance_status = 'violation'
    elif not rules:
        invariance_status = 'no_rules'
    else:
        invariance_status = 'invariant'
    
    return {
        'structure': structure,
        'rules_applied': rules_applied,
        'invariance_status': invariance_status,
        'violations': violations,
        'is_invariant': len(violations) == 0 and len(rules) > 0
    }


def check_recursive_invariance(structure: Any, rule: Callable, max_depth: int = 10) -> bool:
    """
    Check if a rule holds recursively through a nested structure.
    
    Parameters:
    -----------
    structure : Any
        Structure to check
    rule : Callable
        Rule to apply recursively
    max_depth : int
        Maximum recursion depth
        
    Returns:
    --------
    bool
        True if rule holds at all levels
    """
    def _check_recursive(struct, depth=0):
        if depth > max_depth:
            return True
        
        # Check current level
        if not rule(struct):
            return False
        
        # Recursively check nested structures
        if isinstance(struct, dict):
            return all(_check_recursive(v, depth + 1) for v in struct.values())
        elif isinstance(struct, (list, tuple)):
            return all(_check_recursive(item, depth + 1) for item in struct)
        
        return True
    
    return _check_recursive(structure)


class Invariant:
    """
    Class-based invariance operator with rule management.
    
    Provides persistent rule sets and validation tracking.
    """
    
    def __init__(self, default_rules: Optional[List[Callable]] = None):
        """
        Initialize Invariant operator with default rules.
        
        Parameters:
        -----------
        default_rules : Optional[List[Callable]]
            Default rules to apply
        """
        self.default_rules = default_rules or []
        self.validations = []
        
    def __call__(self, structure: Any, rules: Optional[List[Callable]] = None) -> Dict[str, Any]:
        """
        Execute invariance check.
        
        Parameters:
        -----------
        structure : Any
            Structure to validate
        rules : Optional[List[Callable]]
            Additional rules (combined with defaults)
            
        Returns:
        --------
        Dict[str, Any]
            Invariance result
        """
        all_rules = self.default_rules + (rules or [])
        result = invariant(structure, all_rules)
        self.validations.append(result)
        return result
    
    def add_rule(self, rule: Callable):
        """Add a new default rule."""
        self.default_rules.append(rule)
    
    def get_validation_count(self) -> int:
        """Return count of validations performed."""
        return len(self.validations)
    
    def get_invariant_count(self) -> int:
        """Return count of successful invariance validations."""
        return sum(1 for v in self.validations if v['is_invariant'])
