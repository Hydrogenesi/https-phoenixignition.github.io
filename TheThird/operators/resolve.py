"""
resolve.py - The Resolution Operator

Finalizes cross-pillar interactions into stable, deterministic results.
Ensures that pillar interactions produce consistent, lawful outcomes.
"""

from typing import Any, Dict, Optional


def resolve(interaction: Dict[str, Any], deterministic: bool = True) -> Dict[str, Any]:
    """
    Resolve a cross-pillar interaction into a stable result.
    
    The resolve operator takes an interaction specification and produces
    a finalized, deterministic result that upholds structural laws.
    
    Parameters:
    -----------
    interaction : Dict[str, Any]
        The interaction to resolve, containing:
        - pillars: List of involved pillars
        - operation: The operation being performed
        - inputs: Input data
    deterministic : bool
        Whether to enforce deterministic resolution
        
    Returns:
    --------
    Dict[str, Any]
        A resolution result containing:
        - resolved: The final resolved value
        - interaction: Original interaction
        - resolution_status: Status of resolution
        - deterministic: Whether result is deterministic
    
    Examples:
    ---------
    >>> interaction = {
    ...     "pillars": ["phoenix", "hydrogenesi"],
    ...     "operation": "transform",
    ...     "inputs": {"value": 144}
    ... }
    >>> result = resolve(interaction)
    >>> result['resolution_status']
    'resolved'
    """
    if not isinstance(interaction, dict):
        return {
            'resolved': None,
            'interaction': interaction,
            'resolution_status': 'invalid_interaction',
            'deterministic': False,
            'error': 'Interaction must be a dictionary'
        }
    
    # Extract interaction components
    pillars = interaction.get('pillars', [])
    operation = interaction.get('operation', 'unknown')
    inputs = interaction.get('inputs', {})
    
    # Validate interaction
    if not pillars:
        return {
            'resolved': None,
            'interaction': interaction,
            'resolution_status': 'no_pillars',
            'deterministic': False,
            'error': 'No pillars specified in interaction'
        }
    
    # Resolve based on operation type
    if operation == 'transform':
        resolved = _resolve_transform(pillars, inputs, deterministic)
    elif operation == 'merge':
        resolved = _resolve_merge(pillars, inputs, deterministic)
    elif operation == 'cascade':
        resolved = _resolve_cascade(pillars, inputs, deterministic)
    else:
        resolved = _resolve_generic(pillars, operation, inputs, deterministic)
    
    return {
        'resolved': resolved,
        'interaction': interaction,
        'resolution_status': 'resolved',
        'deterministic': deterministic,
        'pillars_involved': len(pillars)
    }


def _resolve_transform(pillars: list, inputs: dict, deterministic: bool) -> dict:
    """Resolve a transformation interaction."""
    return {
        'type': 'transform',
        'result': inputs,
        'pillars': pillars,
        'deterministic': deterministic
    }


def _resolve_merge(pillars: list, inputs: dict, deterministic: bool) -> dict:
    """Resolve a merge interaction."""
    return {
        'type': 'merge',
        'merged_result': inputs,
        'pillars': pillars,
        'deterministic': deterministic
    }


def _resolve_cascade(pillars: list, inputs: dict, deterministic: bool) -> dict:
    """Resolve a cascade interaction."""
    return {
        'type': 'cascade',
        'cascade_result': [inputs] * len(pillars),
        'pillars': pillars,
        'deterministic': deterministic
    }


def _resolve_generic(pillars: list, operation: str, inputs: dict, deterministic: bool) -> dict:
    """Resolve a generic interaction."""
    return {
        'type': 'generic',
        'operation': operation,
        'result': inputs,
        'pillars': pillars,
        'deterministic': deterministic
    }


class Resolve:
    """
    Class-based resolution operator with interaction tracking.
    
    Maintains history of resolutions and provides analytical capabilities.
    """
    
    def __init__(self, force_deterministic: bool = True):
        """
        Initialize Resolve operator.
        
        Parameters:
        -----------
        force_deterministic : bool
            Whether to force deterministic resolution
        """
        self.force_deterministic = force_deterministic
        self.resolutions = []
        
    def __call__(self, interaction: Dict[str, Any], deterministic: Optional[bool] = None) -> Dict[str, Any]:
        """
        Execute resolution.
        
        Parameters:
        -----------
        interaction : Dict[str, Any]
            Interaction to resolve
        deterministic : Optional[bool]
            Override deterministic setting
            
        Returns:
        --------
        Dict[str, Any]
            Resolution result
        """
        is_deterministic = deterministic if deterministic is not None else self.force_deterministic
        result = resolve(interaction, is_deterministic)
        self.resolutions.append(result)
        return result
    
    def get_resolution_count(self) -> int:
        """Return count of resolutions performed."""
        return len(self.resolutions)
    
    def get_deterministic_count(self) -> int:
        """Return count of deterministic resolutions."""
        return sum(1 for r in self.resolutions if r.get('deterministic', False))
