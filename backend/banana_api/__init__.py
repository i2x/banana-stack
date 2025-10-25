# banana_api/__init__.py
import os

def load_tests(loader, tests, pattern):
    from . import tests as tests_pkg
    start_dir = os.path.dirname(tests_pkg.__file__)
    pattern = pattern or "test*.py"
    return loader.discover(start_dir=start_dir, pattern=pattern)
