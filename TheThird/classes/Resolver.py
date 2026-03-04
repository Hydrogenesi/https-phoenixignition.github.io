"""
Resolver.py - The Resolver Class

Handles cross-pillar interaction resolution.
Provides deterministic resolution of complex multi-pillar operations.
"""

from typing import Any, Dict, List, Optional


class Resolver:
    """
    The Resolver class manages cross-pillar interaction resolution.
    
    It provides:
    - Deterministic resolution
    - Interaction tracking
    - Resolution strategy management
    - Conflict resolution
    """
    
    def __init__(self, name: str = "DefaultResolver", deterministic: bool = True):
        """
        Initialize a Resolver instance.
        
        Parameters:
        -----------
        name : str
            Name of this resolver instance
        deterministic : bool
            Whether to enforce deterministic resolution by default
        """
        self.name = name
        self.deterministic = deterministic
        self.resolutions = []
        self.conflicts = []
        
    def resolve(self, interaction: Dict[str, Any], force_deterministic: Optional[bool] = None) -> Dict[str, Any]:
        """
        Resolve a cross-pillar interaction.
        
        Parameters:
        -----------
        interaction : Dict[str, Any]
            The interaction to resolve
        force_deterministic : Optional[bool]
            Override default deterministic setting
            
        Returns:
        --------
        Dict[str, Any]
            Resolution result
        """
        is_deterministic = force_deterministic if force_deterministic is not None else self.deterministic
        
        # Validate interaction
        if not isinstance(interaction, dict):
            return {
                'resolved': None,
                'status': 'invalid',
                'error': 'Interaction must be a dictionary',
                'resolver': self.name
            }
        
        pillars = interaction.get('pillars', [])
        operation = interaction.get('operation', 'unknown')
        inputs = interaction.get('inputs', {})
        
        if not pillars:
            return {
                'resolved': None,
                'status': 'no_pillars',
                'error': 'No pillars specified',
                'resolver': self.name
            }
        
        # Resolve based on operation
        if operation == 'bind':
            resolved = self._resolve_bind(pillars, inputs, is_deterministic)
        elif operation == 'transform':
            resolved = self._resolve_transform(pillars, inputs, is_deterministic)
        elif operation == 'merge':
            resolved = self._resolve_merge(pillars, inputs, is_deterministic)
        elif operation == 'cascade':
            resolved = self._resolve_cascade(pillars, inputs, is_deterministic)
        else:
            resolved = self._resolve_generic(pillars, operation, inputs, is_deterministic)
        
        # Create result
        result = {
            'resolved': resolved,
            'interaction': interaction,
            'status': 'resolved',
            'deterministic': is_deterministic,
            'pillars_involved': len(pillars),
            'resolver': self.name
        }
        
        self.resolutions.append(result)
        return result
    
    def _resolve_bind(self, pillars: List[str], inputs: Dict, deterministic: bool) -> Dict:
        """Resolve a binding interaction."""
        return {
            'type': 'bind',
            'bound_pillars': pillars,
            'result': inputs,
            'deterministic': deterministic
        }
    
    def _resolve_transform(self, pillars: List[str], inputs: Dict, deterministic: bool) -> Dict:
        """Resolve a transformation interaction."""
        return {
            'type': 'transform',
            'transformed_data': inputs,
            'pillars': pillars,
            'deterministic': deterministic
        }
    
    def _resolve_merge(self, pillars: List[str], inputs: Dict, deterministic: bool) -> Dict:
        """Resolve a merge interaction."""
        return {
            'type': 'merge',
            'merged_output': inputs,
            'pillars': pillars,
            'deterministic': deterministic
        }
    
    def _resolve_cascade(self, pillars: List[str], inputs: Dict, deterministic: bool) -> Dict:
        """Resolve a cascade interaction."""
        return {
            'type': 'cascade',
            'cascade_layers': [inputs] * len(pillars),
            'pillars': pillars,
            'deterministic': deterministic
        }
    
    def _resolve_generic(self, pillars: List[str], operation: str, inputs: Dict, deterministic: bool) -> Dict:
        """Resolve a generic interaction."""
        return {
            'type': 'generic',
            'operation': operation,
            'result': inputs,
            'pillars': pillars,
            'deterministic': deterministic
        }
    
    def detect_conflicts(self, interaction1: Dict[str, Any], interaction2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Detect conflicts between two interactions.
        
        Parameters:
        -----------
        interaction1 : Dict[str, Any]
            First interaction
        interaction2 : Dict[str, Any]
            Second interaction
            
        Returns:
        --------
        Dict[str, Any]
            Conflict analysis
        """
        conflicts = []
        
        # Check pillar overlap
        pillars1 = set(interaction1.get('pillars', []))
        pillars2 = set(interaction2.get('pillars', []))
        overlap = pillars1 & pillars2
        
        if overlap:
            conflicts.append({
                'type': 'pillar_overlap',
                'pillars': list(overlap)
            })
        
        # Check operation compatibility
        op1 = interaction1.get('operation')
        op2 = interaction2.get('operation')
        if op1 == op2 and overlap:
            conflicts.append({
                'type': 'operation_conflict',
                'operation': op1
            })
        
        result = {
            'has_conflicts': len(conflicts) > 0,
            'conflicts': conflicts,
            'resolver': self.name
        }
        
        if conflicts:
            self.conflicts.append(result)
        
        return result
    
    def get_resolution_count(self) -> int:
        """Return count of resolutions performed."""
        return len(self.resolutions)
    
    def get_conflict_count(self) -> int:
        """Return count of conflicts detected."""
        return len(self.conflicts)
    
    def clear_history(self):
        """Clear resolution history."""
        self.resolutions = []
        self.conflicts = []
