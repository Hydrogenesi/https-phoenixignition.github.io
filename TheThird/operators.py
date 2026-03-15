"""
operators.py - The Third Operators Aggregation Module

This module provides a unified interface to all operators of The Third pillar.
It aggregates both functional and class-based operators for easy access.

The Third provides five core operator families:
- bind: Establishes structural relationships between pillars
- seal: Locks states with invariance guarantees
- converge: Resolves multi-pillar outputs into canonical form
- invariant: Applies invariance rules across structures
- resolve: Finalizes cross-pillar interactions

Each operator is available in both functional and class-based forms.
"""

# Import functional operators
from .operators.bind import bind, Bind
from .operators.seal import seal, Seal
from .operators.converge import converge, Converge
from .operators.invariant import invariant, Invariant, check_recursive_invariance
from .operators.resolve import resolve, Resolve

# Export all operators
__all__ = [
    # Functional operators
    'bind',
    'seal',
    'converge',
    'invariant',
    'resolve',
    # Class-based operators
    'Bind',
    'Seal',
    'Converge',
    'Invariant',
    'Resolve',
    # Utility functions
    'check_recursive_invariance'
]

# Operator registry for introspection
OPERATORS = {
    'bind': {
        'functional': bind,
        'class': Bind,
        'description': 'Establishes structural relationships between pillars'
    },
    'seal': {
        'functional': seal,
        'class': Seal,
        'description': 'Locks states with invariance guarantees'
    },
    'converge': {
        'functional': converge,
        'class': Converge,
        'description': 'Resolves multi-pillar outputs into canonical form'
    },
    'invariant': {
        'functional': invariant,
        'class': Invariant,
        'description': 'Applies invariance rules across structures'
    },
    'resolve': {
        'functional': resolve,
        'class': Resolve,
        'description': 'Finalizes cross-pillar interactions'
    }
}


def get_operator_info(operator_name: str) -> dict:
    """
    Get information about a specific operator.
    
    Parameters:
    -----------
    operator_name : str
        Name of the operator
        
    Returns:
    --------
    dict
        Operator information or None if not found
    """
    return OPERATORS.get(operator_name)


def list_operators() -> list:
    """
    List all available operators.
    
    Returns:
    --------
    list
        List of operator names
    """
    return list(OPERATORS.keys())
