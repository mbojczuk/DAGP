# tests/example2.py
from .base import BaseTest
from .registry import TestRegistry

@TestRegistry.register
class AlwaysPassTest(BaseTest):
    """
    Simple test that always returns success.
    """
    name = "always_pass"

    def run_test(self) -> dict:
        # perform trivial check and return standardized dict
        return {"result": "success", "message": ""}