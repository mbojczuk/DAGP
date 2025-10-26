# Workflows Testing Framework

The idea is you can expand as many tests in the wrapper as you want, and then on a pull request (PR), it will print out errors to users.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- GitHub repository with Actions enabled

### Adding the Workflow

1. Create a directory in your repository called `.github/workflows`.
2. Inside this directory, create a file named `run-tests.yml` and copy the run-tests.yml

### Running the Tests
To run the tests, simply push your changes to the repository or create a pull request. The GitHub Actions workflow will automatically trigger and run the tests defined in your test_wrapper/main.py.

Adding Tests
1. Create a New Test: To add a new test, create a new Python file in the test_wrapper/tests/ directory. For example, new_test.py.
2. Implement the Test: Your test class should inherit from BaseTest and implement the run() method. Here’s a simple example:
```python
# tests/examples.py
from .base import BaseTest
from .registry import TestRegistry

@TestRegistry.register
class HelloTest(BaseTest):
    name = "hello_again"

    def run_test(self) -> dict:
        # some logic
        return {"result": "success", "message": ""}
```
3. Register the Test: Ensure your test class is registered by using the @TestRegistry.register decorator.
4. Run the Tests: You can specify which tests to run by modifying the --tests argument in the run-tests.yml file or by passing it directly in the command line.

Example Command
To run specific tests, you can modify the command in the workflow:
```bash
python "${TEST_WRAPPER_DIR}/${MAIN_RUNNER}" --tests hello,some_name,whatever > "${LOG_PATH}" 2>&1 || true
```
Conclusion
This framework allows you to easily add and manage tests in your project. By following the steps above, you can ensure that your tests are run automatically on every push or pull request, providing immediate feedback on the status of your code changes.

