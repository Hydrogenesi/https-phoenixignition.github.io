"""
ConvergenceMap.py - The ConvergenceMap Class

Maps and tracks convergence operations across pillars.
Provides visualization and analysis of convergence patterns.
"""

from typing import Any, Dict, List, Optional


class ConvergenceMap:
    """
    The ConvergenceMap class tracks and analyzes convergence operations.
    
    It provides:
    - Convergence tracking
    - Pattern analysis
    - Strategy management
    - Convergence history
    """
    
    def __init__(self, name: str = "DefaultConvergenceMap", default_strategy: str = "canonical"):
        """
        Initialize a ConvergenceMap instance.
        
        Parameters:
        -----------
        name : str
            Name of this convergence map
        default_strategy : str
            Default convergence strategy
        """
        self.name = name
        self.default_strategy = default_strategy
        self.convergences = []
        self.patterns = {}
        
    def converge(self, *outputs, strategy: Optional[str] = None, label: Optional[str] = None) -> Dict[str, Any]:
        """
        Converge multiple outputs.
        
        Parameters:
        -----------
        *outputs : Any
            Outputs to converge
        strategy : Optional[str]
            Convergence strategy to use
        label : Optional[str]
            Optional label for this convergence
            
        Returns:
        --------
        Dict[str, Any]
            Convergence result
        """
        active_strategy = strategy or self.default_strategy
        
        if not outputs:
            return {
                'converged': None,
                'status': 'no_inputs',
                'strategy': active_strategy,
                'map': self.name
            }
        
        # Perform convergence based on strategy
        if active_strategy == "canonical":
            converged = self._canonical_convergence(outputs)
        elif active_strategy == "merge":
            converged = self._merge_convergence(outputs)
        elif active_strategy == "prioritize":
            converged = self._prioritize_convergence(outputs)
        elif active_strategy == "average":
            converged = self._average_convergence(outputs)
        else:
            converged = self._custom_convergence(outputs, active_strategy)
        
        # Create result
        result = {
            'converged': converged,
            'sources': list(outputs),
            'strategy': active_strategy,
            'status': 'converged',
            'source_count': len(outputs),
            'map': self.name,
            'label': label
        }
        
        # Track convergence
        self.convergences.append(result)
        
        # Update pattern tracking
        pattern_key = f"{active_strategy}_{len(outputs)}"
        if pattern_key not in self.patterns:
            self.patterns[pattern_key] = 0
        self.patterns[pattern_key] += 1
        
        return result
    
    def _canonical_convergence(self, outputs: tuple) -> Dict:
        """Create canonical form convergence."""
        return {
            'canonical_form': True,
            'pillar_count': len(outputs),
            'unified_output': {f'pillar_{i}': out for i, out in enumerate(outputs)}
        }
    
    def _merge_convergence(self, outputs: tuple) -> Any:
        """Merge all outputs."""
        merged = {}
        for output in outputs:
            if isinstance(output, dict):
                merged.update(output)
            else:
                merged[f'value_{len(merged)}'] = output
        return merged
    
    def _prioritize_convergence(self, outputs: tuple) -> Any:
        """Prioritize first output."""
        if not outputs:
            return None
        
        result = outputs[0] if isinstance(outputs[0], dict) else {'primary': outputs[0]}
        
        for i, output in enumerate(outputs[1:], 1):
            if isinstance(output, dict):
                for key, value in output.items():
                    if key not in result:
                        result[key] = value
            else:
                result[f'supplement_{i}'] = output
        
        return result
    
    def _average_convergence(self, outputs: tuple) -> Any:
        """Average numeric outputs."""
        numeric_values = []
        
        for output in outputs:
            if isinstance(output, (int, float)):
                numeric_values.append(output)
            elif isinstance(output, dict):
                for value in output.values():
                    if isinstance(value, (int, float)):
                        numeric_values.append(value)
        
        if numeric_values:
            return {
                'average': sum(numeric_values) / len(numeric_values),
                'count': len(numeric_values),
                'values': numeric_values
            }
        
        return {'average': None, 'count': 0}
    
    def _custom_convergence(self, outputs: tuple, strategy: str) -> Dict:
        """Custom convergence strategy."""
        return {
            'type': 'custom',
            'strategy': strategy,
            'outputs': list(outputs)
        }
    
    def get_pattern_analysis(self) -> Dict[str, Any]:
        """
        Analyze convergence patterns.
        
        Returns:
        --------
        Dict[str, Any]
            Pattern analysis results
        """
        total = len(self.convergences)
        
        return {
            'total_convergences': total,
            'patterns': self.patterns,
            'strategies_used': list(set(c['strategy'] for c in self.convergences)),
            'average_source_count': sum(c['source_count'] for c in self.convergences) / total if total > 0 else 0,
            'map': self.name
        }
    
    def get_convergences_by_strategy(self, strategy: str) -> List[Dict[str, Any]]:
        """
        Get all convergences using a specific strategy.
        
        Parameters:
        -----------
        strategy : str
            Strategy to filter by
            
        Returns:
        --------
        List[Dict[str, Any]]
            Convergences using that strategy
        """
        return [c for c in self.convergences if c['strategy'] == strategy]
    
    def get_convergences_by_label(self, label: str) -> List[Dict[str, Any]]:
        """
        Get all convergences with a specific label.
        
        Parameters:
        -----------
        label : str
            Label to filter by
            
        Returns:
        --------
        List[Dict[str, Any]]
            Convergences with that label
        """
        return [c for c in self.convergences if c.get('label') == label]
    
    def clear_history(self):
        """Clear convergence history."""
        self.convergences = []
        self.patterns = {}
