# tests/registry.py
from typing import Dict, Type
from .base import BaseTest

class TestRegistry:
    """
    Simple registry that maps test names to test classes.

    Use @TestRegistry.register on test classes to register them when their module is imported.
    """
    _registry: Dict[str, Type[BaseTest]] = {}

    @classmethod
    def register(cls, test_cls: Type[BaseTest]) -> Type[BaseTest]:
        name = getattr(test_cls, "name", test_cls.__name__)
        if name in cls._registry:
            raise KeyError(f"Test already registered with name: {name}")
        cls._registry[name] = test_cls
        return test_cls

    @classmethod
    def get(cls, name: str):
        return cls._registry.get(name)

    @classmethod
    def all(cls):
        # return a copy to avoid external mutation
        return dict(cls._registry)