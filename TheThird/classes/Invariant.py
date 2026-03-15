"""
Invariant.py - The Invariant Engine Class

Enforces invariance across the system.
Provides comprehensive invariance checking and rule management.
"""

from typing import Any, Callable, List, Dict, Optional


class InvariantEngine:
    """
    The InvariantEngine enforces invariance rules across structures.
    
    It provides:
    - Rule management
    - Multi-level invariance checking
    - Violation tracking
    - Recursive invariance validation
    """
    
    def __init__(self, name: str = "DefaultInvariantEngine"):
        """
        Initialize an InvariantEngine instance.
        
        Parameters:
        -----------
        name : str
            Name of this engine instance
        """
        self.name = name
        self.rules = []
        self.validations = []
        self.violations = []
        
    def add_rule(self, rule: Callable, name: Optional[str] = None):
        """
        Add an invariance rule.
        
        Parameters:
        -----------
        rule : Callable
            Rule function that accepts a structure and returns bool
        name : Optional[str]
            Optional name for the rule
        """
        rule_entry = {
            'function': rule,
            'name': name or f'rule_{len(self.rules)}',
            'rule_id': len(self.rules)
        }
        self.rules.append(rule_entry)
    
    def check(self, structure: Any, rules: Optional[List[Callable]] = None) -> Dict[str, Any]:
        """
        Check invariance of a structure.
        
        Parameters:
        -----------
        structure : Any
            Structure to validate
        rules : Optional[List[Callable]]
            Additional rules to check (uses engine rules if None)
            
        Returns:
        --------
        Dict[str, Any]
            Validation result
        """
        # Use provided rules or engine rules
        if rules is not None:
            rule_list = [{'function': r, 'name': f'temp_{i}', 'rule_id': i} 
                        for i, r in enumerate(rules)]
        else:
            rule_list = self.rules
        
        if not rule_list:
            return {
                'structure': structure,
                'status': 'no_rules',
                'is_invariant': False,
                'engine': self.name
            }
        
        violations = []
        passed = []
        
        for rule_entry in rule_list:
            rule = rule_entry['function']
            try:
                if rule(structure):
                    passed.append(rule_entry['name'])
                else:
                    violations.append({
                        'rule': rule_entry['name'],
                        'rule_id': rule_entry['rule_id'],
                        'type': 'violation'
                    })
            except Exception as e:
                violations.append({
                    'rule': rule_entry['name'],
                    'rule_id': rule_entry['rule_id'],
                    'type': 'error',
                    'error': str(e)
                })
        
        # Record result
        result = {
            'structure': structure,
            'status': 'invariant' if not violations else 'violation',
            'is_invariant': len(violations) == 0,
            'rules_passed': passed,
            'violations': violations,
            'engine': self.name
        }
        
        self.validations.append(result)
        if violations:
            self.violations.extend(violations)
        
        return result
    
    def check_recursive(self, structure: Any, max_depth: int = 10) -> Dict[str, Any]:
        """
        Check invariance recursively through nested structures.
        
        Parameters:
        -----------
        structure : Any
            Root structure to validate
        max_depth : int
            Maximum recursion depth
            
        Returns:
        --------
        Dict[str, Any]
            Recursive validation result
        """
        violations = []
        
        def _check_level(struct, depth=0):
            if depth > max_depth:
                return
            
            # Check current level
            result = self.check(struct)
            if not result['is_invariant']:
                violations.extend(result['violations'])
            
            # Recurse into nested structures
            if isinstance(struct, dict):
                for value in struct.values():
                    _check_level(value, depth + 1)
            elif isinstance(struct, (list, tuple)):
                for item in struct:
                    _check_level(item, depth + 1)
        
        _check_level(structure)
        
        return {
            'structure': structure,
            'status': 'invariant' if not violations else 'violation',
            'is_invariant': len(violations) == 0,
            'violations': violations,
            'max_depth': max_depth,
            'engine': self.name
        }
    
    def get_violation_count(self) -> int:
        """Return total count of violations detected."""
        return len(self.violations)
    
    def get_validation_count(self) -> int:
        """Return total count of validations performed."""
        return len(self.validations)
    
    def get_success_rate(self) -> float:
        """
        Calculate success rate of validations.
        
        Returns:
        --------
        float
            Success rate (0.0 to 1.0)
        """
        if not self.validations:
            return 0.0
        
        successful = sum(1 for v in self.validations if v['is_invariant'])
        return successful / len(self.validations)
    
    def clear_history(self):
        """Clear validation history and violations."""
        self.validations = []
        self.violations = []
