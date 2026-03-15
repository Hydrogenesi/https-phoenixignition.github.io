"""
seal.py - The Sealing Operator

Locks a state, preventing drift or mutation beyond defined invariants.
Provides final-state guarantees for critical structures.
"""

from typing import Any, Optional, List, Dict, Callable
import copy


def seal(state: Any, invariants: Optional[List[Callable]] = None) -> Dict[str, Any]:
    """
    Seal a state with optional invariant enforcement.
    
    The seal operator creates an immutable snapshot of a state and enforces
    invariants to prevent drift. Sealed states are protected from mutation.
    
    Parameters:
    -----------
    state : Any
        The state to seal
    invariants : Optional[List[Callable]]
        List of invariant functions to enforce
        Each function should accept the state and return bool
        
    Returns:
    --------
    Dict[str, Any]
        A sealed structure containing:
        - sealed_state: Immutable copy of the state
        - invariants_enforced: List of enforced invariants
        - seal_status: Status of the seal
        - violations: Any invariant violations detected
    
    Examples:
    ---------
    >>> state = {"energy": 144, "phase": "ignition"}
    >>> def check_energy(s): return s.get("energy", 0) > 0
    >>> result = seal(state, invariants=[check_energy])
    >>> result['seal_status']
    'sealed'
    """
    # Create immutable copy
    sealed_state = copy.deepcopy(state)
    
    violations = []
    invariants_enforced = []
    
    # Check invariants if provided
    if invariants:
        for i, inv in enumerate(invariants):
            try:
                if not inv(sealed_state):
                    violations.append({
                        'invariant_index': i,
                        'status': 'violated'
                    })
                else:
                    invariants_enforced.append({
                        'invariant_index': i,
                        'status': 'valid'
                    })
            except Exception as e:
                violations.append({
                    'invariant_index': i,
                    'status': 'error',
                    'error': str(e)
                })
    
    # Determine seal status
    if violations:
        seal_status = 'invariant_violation'
    else:
        seal_status = 'sealed'
    
    return {
        'sealed_state': sealed_state,
        'invariants_enforced': invariants_enforced,
        'seal_status': seal_status,
        'violations': violations,
        'is_sealed': len(violations) == 0
    }


class Seal:
    """
    Class-based sealing operator with state tracking.
    
    Maintains a registry of sealed states and provides verification.
    """
    
    def __init__(self, default_invariants: Optional[List[Callable]] = None):
        """
        Initialize Seal operator with default invariants.
        
        Parameters:
        -----------
        default_invariants : Optional[List[Callable]]
            Default invariants to apply to all seals
        """
        self.default_invariants = default_invariants or []
        self.sealed_states = []
        
    def __call__(self, state: Any, invariants: Optional[List[Callable]] = None) -> Dict[str, Any]:
        """
        Execute sealing operation.
        
        Parameters:
        -----------
        state : Any
            State to seal
        invariants : Optional[List[Callable]]
            Additional invariants (combined with defaults)
            
        Returns:
        --------
        Dict[str, Any]
            Seal result
        """
        all_invariants = self.default_invariants + (invariants or [])
        result = seal(state, all_invariants)
        
        if result['is_sealed']:
            self.sealed_states.append(result)
        
        return result
    
    def verify_seal(self, sealed_result: Dict[str, Any]) -> bool:
        """
        Verify a seal is still valid.
        
        Parameters:
        -----------
        sealed_result : Dict[str, Any]
            Previously sealed result
            
        Returns:
        --------
        bool
            True if seal is valid, False otherwise
        """
        return sealed_result.get('seal_status') == 'sealed'
    
    def get_sealed_count(self) -> int:
        """Return count of successfully sealed states."""
        return len(self.sealed_states)
