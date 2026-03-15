"""
Binder.py - The Binder Class

Manages structural relationships between pillars.
Provides advanced binding capabilities with tracking and validation.
"""

from typing import Any, Optional, Callable, List, Dict


class Binder:
    """
    The Binder class manages structural relationships across pillars.
    
    It provides:
    - Persistent binding management
    - Law enforcement
    - Binding validation
    - Relationship tracking
    """
    
    def __init__(self, name: str = "DefaultBinder", laws: Optional[List[Callable]] = None):
        """
        Initialize a Binder instance.
        
        Parameters:
        -----------
        name : str
            Name of this binder instance
        laws : Optional[List[Callable]]
            Default laws to enforce on all bindings
        """
        self.name = name
        self.laws = laws or []
        self.bindings = []
        self.binding_map = {}
        
    def bind(self, source: Any, target: Any, law: Optional[Callable] = None) -> Dict[str, Any]:
        """
        Create a binding between source and target.
        
        Parameters:
        -----------
        source : Any
            The source to bind
        target : Any
            The target to bind
        law : Optional[Callable]
            Optional law to enforce (in addition to default laws)
            
        Returns:
        --------
        Dict[str, Any]
            Binding result with structure and status
        """
        # Apply all laws
        active_laws = self.laws + ([law] if law else [])
        
        for law_func in active_laws:
            try:
                if not law_func(source, target):
                    return {
                        'source': source,
                        'target': target,
                        'bound': False,
                        'status': 'law_violation',
                        'binder': self.name
                    }
            except Exception as e:
                return {
                    'source': source,
                    'target': target,
                    'bound': False,
                    'status': 'law_error',
                    'error': str(e),
                    'binder': self.name
                }
        
        # Create binding
        binding = {
            'source': source,
            'target': target,
            'bound': True,
            'status': 'bound',
            'binder': self.name,
            'laws_applied': len(active_laws),
            'binding_id': len(self.bindings)
        }
        
        self.bindings.append(binding)
        
        # Update binding map
        source_key = str(id(source))
        if source_key not in self.binding_map:
            self.binding_map[source_key] = []
        self.binding_map[source_key].append(binding)
        
        return binding
    
    def get_bindings(self, source: Optional[Any] = None) -> List[Dict[str, Any]]:
        """
        Get bindings, optionally filtered by source.
        
        Parameters:
        -----------
        source : Optional[Any]
            If provided, return only bindings from this source
            
        Returns:
        --------
        List[Dict[str, Any]]
            List of bindings
        """
        if source is None:
            return self.bindings
        
        source_key = str(id(source))
        return self.binding_map.get(source_key, [])
    
    def validate_all_bindings(self) -> Dict[str, Any]:
        """
        Validate all bindings against current laws.
        
        Returns:
        --------
        Dict[str, Any]
            Validation summary
        """
        valid_count = 0
        invalid_count = 0
        
        for binding in self.bindings:
            if binding['status'] == 'bound':
                valid_count += 1
            else:
                invalid_count += 1
        
        return {
            'total_bindings': len(self.bindings),
            'valid': valid_count,
            'invalid': invalid_count,
            'binder': self.name
        }
    
    def add_law(self, law: Callable):
        """
        Add a new law to enforce on future bindings.
        
        Parameters:
        -----------
        law : Callable
            Law function to add
        """
        self.laws.append(law)
    
    def clear_bindings(self):
        """Clear all bindings."""
        self.bindings = []
        self.binding_map = {}
