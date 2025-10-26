# tests/examples.py
from .base import BaseTest
from .registry import TestRegistry

@TestRegistry.register
class HelloTest(BaseTest):
    name = "hello"

    def run_test(self) -> dict:
        return {"result": "success", "message": ""}


@TestRegistry.register
class GoobyeTest(BaseTest):
    name = "goodbye"

    def run_test(self) -> dict:
        return {"result": "fail", "message": "Goodbye test always fails."}