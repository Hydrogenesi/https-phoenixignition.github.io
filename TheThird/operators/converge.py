"""
converge.py - The Convergence Operator

Resolves multi-pillar outputs into a single canonical form.
Ensures unified output from disparate pillar sources.
"""

from typing import Any, Dict, List


def converge(*outputs, strategy: str = "canonical") -> Dict[str, Any]:
    """
    Converge multiple outputs into a single canonical form.
    
    The converge operator takes outputs from multiple pillars and produces
    a unified, canonical result following the specified strategy.
    
    Parameters:
    -----------
    *outputs : Any
        Variable number of outputs to converge
    strategy : str
        Convergence strategy ("canonical", "merge", "prioritize")
        
    Returns:
    --------
    Dict[str, Any]
        A convergence result containing:
        - converged: The unified output
        - sources: List of source outputs
        - strategy: Strategy used
        - convergence_status: Status of convergence
    
    Examples:
    ---------
    >>> phoenix = {"type": "ignition", "value": 144}
    >>> hydro = {"type": "flow", "depth": 3}
    >>> result = converge(phoenix, hydro, strategy="canonical")
    >>> result['convergence_status']
    'converged'
    """
    if not outputs:
        return {
            'converged': None,
            'sources': [],
            'strategy': strategy,
            'convergence_status': 'no_inputs'
        }
    
    if len(outputs) == 1:
        return {
            'converged': outputs[0],
            'sources': list(outputs),
            'strategy': strategy,
            'convergence_status': 'single_input'
        }
    
    # Apply convergence strategy
    if strategy == "canonical":
        # Create canonical form with all inputs
        converged = {
            'canonical_form': True,
            'pillar_count': len(outputs),
            'unified_output': {}
        }
        
        for i, output in enumerate(outputs):
            converged['unified_output'][f'pillar_{i}'] = output
            
    elif strategy == "merge":
        # Merge all dictionary outputs
        converged = {}
        for output in outputs:
            if isinstance(output, dict):
                converged.update(output)
            else:
                converged[f'value_{len(converged)}'] = output
                
    elif strategy == "prioritize":
        # Prioritize first output, supplement with others
        converged = outputs[0] if isinstance(outputs[0], dict) else {'primary': outputs[0]}
        for i, output in enumerate(outputs[1:], 1):
            if isinstance(output, dict):
                for key, value in output.items():
                    if key not in converged:
                        converged[key] = value
            else:
                converged[f'supplement_{i}'] = output
    else:
        return {
            'converged': None,
            'sources': list(outputs),
            'strategy': strategy,
            'convergence_status': 'invalid_strategy',
            'error': f'Unknown strategy: {strategy}'
        }
    
    return {
        'converged': converged,
        'sources': list(outputs),
        'strategy': strategy,
        'convergence_status': 'converged'
    }


class Converge:
    """
    Class-based convergence operator with history tracking.
    
    Maintains convergence history and provides analytical capabilities.
    """
    
    def __init__(self, default_strategy: str = "canonical"):
        """
        Initialize Converge operator.
        
        Parameters:
        -----------
        default_strategy : str
            Default convergence strategy
        """
        self.default_strategy = default_strategy
        self.convergences = []
        
    def __call__(self, *outputs, strategy: str = None) -> Dict[str, Any]:
        """
        Execute convergence operation.
        
        Parameters:
        -----------
        *outputs : Any
            Outputs to converge
        strategy : str
            Strategy override
            
        Returns:
        --------
        Dict[str, Any]
            Convergence result
        """
        active_strategy = strategy if strategy is not None else self.default_strategy
        result = converge(*outputs, strategy=active_strategy)
        self.convergences.append(result)
        return result
    
    def get_convergence_count(self) -> int:
        """Return count of convergence operations."""
        return len(self.convergences)
    
    def get_successful_convergences(self) -> List[Dict[str, Any]]:
        """Return all successful convergences."""
        return [c for c in self.convergences if c['convergence_status'] == 'converged']
