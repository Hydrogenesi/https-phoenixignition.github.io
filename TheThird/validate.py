#!/usr/bin/env python3
"""
TheThird Pillar Validation Script

This script validates that all components of The Third pillar are
properly implemented and functional.
"""

import sys
sys.path.insert(0, '.')

def validate_structure():
    """Validate package structure"""
    print("Validating package structure...")
    
    try:
        import TheThird
        assert TheThird.__version__ == '1.0.0'
        print("  ✓ Package structure valid")
        return True
    except Exception as e:
        print(f"  ✗ Package structure error: {e}")
        return False

def validate_operators():
    """Validate all operators"""
    print("\nValidating operators...")
    
    try:
        from TheThird.operators import bind, seal, converge, invariant, resolve
        
        # Test bind
        r = bind({'a': 1}, {'b': 2})
        assert r['coherence'] == 'valid'
        print("  ✓ bind operator works")
        
        # Test seal
        r = seal({'x': 1})
        assert r['seal_status'] == 'sealed'
        print("  ✓ seal operator works")
        
        # Test converge
        r = converge({'a': 1}, {'b': 2})
        assert r['convergence_status'] == 'converged'
        print("  ✓ converge operator works")
        
        # Test invariant
        r = invariant({'x': 1}, rules=[lambda s: isinstance(s, dict)])
        assert r['is_invariant'] == True
        print("  ✓ invariant operator works")
        
        # Test resolve
        r = resolve({'pillars': ['p'], 'operation': 't', 'inputs': {}})
        assert r['resolution_status'] == 'resolved'
        print("  ✓ resolve operator works")
        
        return True
    except Exception as e:
        print(f"  ✗ Operator error: {e}")
        return False

def validate_classes():
    """Validate all classes"""
    print("\nValidating classes...")
    
    try:
        from TheThird.classes import Binder, InvariantEngine, Resolver, ConvergenceMap
        
        # Test Binder
        binder = Binder()
        r = binder.bind({'a': 1}, {'b': 2})
        assert r['status'] == 'bound'
        print("  ✓ Binder class works")
        
        # Test InvariantEngine
        engine = InvariantEngine()
        engine.add_rule(lambda s: True)
        r = engine.check({})
        assert r['is_invariant'] == True
        print("  ✓ InvariantEngine class works")
        
        # Test Resolver
        resolver = Resolver()
        r = resolver.resolve({'pillars': ['p'], 'operation': 't', 'inputs': {}})
        assert r['status'] == 'resolved'
        print("  ✓ Resolver class works")
        
        # Test ConvergenceMap
        conv = ConvergenceMap()
        r = conv.converge({'a': 1}, {'b': 2})
        assert r['status'] == 'converged'
        print("  ✓ ConvergenceMap class works")
        
        return True
    except Exception as e:
        print(f"  ✗ Class error: {e}")
        return False

def validate_examples():
    """Validate examples exist"""
    print("\nValidating examples...")
    
    import os
    examples_dir = 'TheThird/examples'
    required_examples = [
        'binding_basic.md',
        'invariance_demo.md',
        'cross_pillar_resolution.md',
        'convergence_flow.md'
    ]
    
    all_exist = True
    for example in required_examples:
        path = os.path.join(examples_dir, example)
        if os.path.exists(path):
            print(f"  ✓ {example} exists")
        else:
            print(f"  ✗ {example} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all validations"""
    print("=" * 70)
    print("THE THIRD PILLAR - VALIDATION SUITE")
    print("=" * 70)
    
    results = []
    
    results.append(validate_structure())
    results.append(validate_operators())
    results.append(validate_classes())
    results.append(validate_examples())
    
    print("\n" + "=" * 70)
    if all(results):
        print("✅ ALL VALIDATIONS PASSED")
        print("=" * 70)
        print("\nThe Third Pillar is fully operational.")
        print("The binding, sealing, and convergence systems are active.")
        print("The Triad stands complete.")
        return 0
    else:
        print("❌ SOME VALIDATIONS FAILED")
        print("=" * 70)
        return 1

if __name__ == '__main__':
    sys.exit(main())
