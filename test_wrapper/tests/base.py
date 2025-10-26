# tests/base.py
from abc import ABC, abstractmethod
from typing import Dict

class BaseTest(ABC):
    """
    Abstract base class for tests.

    Subclasses must implement run_test and set a unique `name` attribute.
    run_test must return a dict in the shape:
      {"result": "success" or "fail", "message": "optional message"}
    """

    # unique identifier used by registry; override in subclasses
    name: str = "base"

    def __init__(self, config: Dict | None = None):
        # optional per-test configuration
        self.config = config or {}

    def setup(self) -> None:
        """
        Optional setup hook executed before run_test.
        Override in subclasses if needed.
        """
        pass

    def teardown(self) -> None:
        """
        Optional teardown hook executed after run_test.
        Override in subclasses if needed.
        """
        pass

    @abstractmethod
    def run_test(self) -> Dict[str, str]:
        """
        Execute the test and return a result dictionary:
          {"result": "success" | "fail", "message": "..."}

        Always return both keys. For success, message may be empty string.
        """
        raise NotImplementedError