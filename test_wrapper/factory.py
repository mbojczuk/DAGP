# factory.py
from typing import Optional
from tests.registry import TestRegistry
from tests.base import BaseTest

class TestFactory:
    """
    Factory that creates test instances by name using the TestRegistry.
    """

    @staticmethod
    def create(name: str, config: Optional[dict] = None) -> BaseTest:
        """
        Create an instance of the named test class.
        Raises KeyError if the test is not registered.
        """
        cls = TestRegistry.get(name)
        if cls is None:
            raise KeyError(f"No test registered under name: {name}")
        # instantiate with provided config
        return cls(config=config)

    @staticmethod
    def available() -> list:
        """
        Return list of available test names.
        """
        return list(TestRegistry.all().keys())