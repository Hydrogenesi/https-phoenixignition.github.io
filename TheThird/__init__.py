"""
The Third - The Binding Pillar

This package provides the binding, sealing, and convergence operations
for the three-pillar Phoenix Archive architecture.

The Third is the structural anchor that ensures:
- Operators across pillars interoperate
- Universal laws remain consistent
- Recursion does not diverge
- The archive maintains internal sovereignty

Core modules:
- operators: Functional operators (bind, seal, converge, invariant, resolve)
- classes: Object-oriented interfaces (Binder, InvariantEngine, Resolver, ConvergenceMap)
"""

__version__ = '1.0.0'
__author__ = 'The Third Pillar'

# Make operators and classes available at package level
from . import operators as ops
from . import classes

__all__ = ['ops', 'classes', '__version__', '__author__']
