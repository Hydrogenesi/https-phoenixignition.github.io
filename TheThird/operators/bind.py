"""
bind.py - The Binding Operator

Establishes structural relationships between Phoenix and Hydrogenesi outputs.
Ensures cross-pillar coherence and maintains linkage integrity.
"""

from typing import Any, Optional, Dict, Callable


def bind(source: Any, target: Any, law: Optional[Callable] = None) -> Dict[str, Any]:
    """
    Bind source to target with optional law enforcement.
    
    The bind operator creates a structural relationship between outputs from
    different pillars, ensuring they remain coherent and lawful.
    
    Parameters:
    -----------
    source : Any
        The source output (typically from Phoenix)
    target : Any
        The target output (typically from Hydrogenesi)
    law : Optional[Callable]
        Optional law function to enforce during binding
        
    Returns:
    --------
    Dict[str, Any]
        A binding structure containing:
        - source: The original source
        - target: The original target
        - bound: The bound result
        - law_applied: Whether a law was enforced
        - coherence: Coherence status
    
    Examples:
    ---------
    >>> phoenix_output = {"ignition": "active", "energy": 144}
    >>> hydro_output = {"flow": "recursive", "depth": 3}
    >>> result = bind(phoenix_output, hydro_output)
    >>> result['coherence']
    'valid'
    """
    # Apply law if provided
    if law is not None:
        try:
            law_result = law(source, target)
            if not law_result:
                return {
                    'source': source,
                    'target': target,
                    'bound': None,
                    'law_applied': True,
                    'coherence': 'law_violation',
                    'error': 'Law enforcement failed'
                }
        except Exception as e:
            return {
                'source': source,
                'target': target,
                'bound': None,
                'law_applied': True,
                'coherence': 'error',
                'error': str(e)
            }
    
    # Create binding structure
    bound_structure = {
        'phoenix_source': source,
        'hydrogenesi_target': target,
        'binding_type': 'cross_pillar',
        'timestamp': 'sealed'
    }
    
    return {
        'source': source,
        'target': target,
        'bound': bound_structure,
        'law_applied': law is not None,
        'coherence': 'valid'
    }


class Bind:
    """
    Class-based binding operator for advanced binding patterns.
    
    Provides stateful binding with tracking and history.
    """
    
    def __init__(self, law: Optional[Callable] = None):
        """
        Initialize Bind operator with optional law.
        
        Parameters:
        -----------
        law : Optional[Callable]
            Law function to enforce on all bindings
        """
        self.law = law
        self.bindings = []
        
    def __call__(self, source: Any, target: Any, law: Optional[Callable] = None) -> Dict[str, Any]:
        """
        Execute binding operation.
        
        Parameters:
        -----------
        source : Any
            Source to bind
        target : Any
            Target to bind
        law : Optional[Callable]
            Optional law override
            
        Returns:
        --------
        Dict[str, Any]
            Binding result
        """
        active_law = law if law is not None else self.law
        result = bind(source, target, active_law)
        self.bindings.append(result)
        return result
    
    def get_bindings(self) -> list:
        """Return all bindings created by this operator."""
        return self.bindings
    
    def clear(self):
        """Clear binding history."""
        self.bindings = []
