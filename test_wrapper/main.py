# main.py
import importlib
import pkgutil
import sys
import json
import argparse
from typing import Dict, Any, List
from tests.registry import TestRegistry

def import_all_tests(package_name: str = "tests") -> None:
    """
    Import every module under the tests package so any @TestRegistry.register
    decorated classes perform registration on import.
    """
    pkg = importlib.import_module(package_name)
    pkg_path = getattr(pkg, "__path__", None)
    if not pkg_path:
        return
    for _finder, name, _ispkg in pkgutil.iter_modules(pkg_path):
        full_name = f"{package_name}.{name}"
        if full_name not in sys.modules:
            importlib.import_module(full_name)

def run_named_test(name: str, config: Dict[str, Any] | None = None) -> Dict[str, str]:
    """
    Instantiate and run a single registered test by name.
    Returns standardized result dict: {"result": "success"|"fail", "message": str}
    """
    cls = TestRegistry.get(name)
    if cls is None:
        msg = f"no test registered with name: {name}"
        print(f"[{name}] fail: {msg}")
        return {"result": "fail", "message": msg}

    inst = cls(config=config or {})
    try:
        res = inst.run_test()
    except Exception as exc:
        # Convert unexpected exceptions into a fail result with message
        res = {"result": "fail", "message": f"exception: {exc}"}

    status = res.get("result", "fail")
    message = res.get("message", "")
    if status == "success":
        print(f"[{name}] ✅ success")
    else:
        print(f"[{name}] ❌ fail: {message}")
    return {"result": status, "message": message}

def run_selected_tests(names: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Run the provided list of test names in order. Unknown names produce fail entries.
    """
    results: Dict[str, Dict[str, str]] = {}
    for n in names:
        results[n] = run_named_test(n)
    return results

def parse_test_list(s: str) -> List[str]:
    """
    Parse a comma-separated list of test names, trimming whitespace.
    Example: "goodbye, always_pass" -> ["goodbye", "always_pass"]
    """
    if not s:
        return []
    return [part.strip() for part in s.split(",") if part.strip()]

if __name__ == "__main__":
    # Ensure tests get imported and register themselves
    import_all_tests("tests")

    parser = argparse.ArgumentParser(description="Run selected registered tests; runs all if none specified")
    parser.add_argument(
        "--tests",
        type=str,
        help="Comma-separated list of test names to run, e.g. --tests goodbye,always_pass (optional)",
    )
    args = parser.parse_args()

    # Determine which tests to run:
    # - If --tests provided, use that list
    # - If not provided, run all registered tests
    if args.tests is not None and args.tests.strip() != "":
        requested = parse_test_list(args.tests)
    else:
        # run all registered tests in registry order
        requested = list(TestRegistry.all().keys())

    # Run requested tests
    results = run_selected_tests(requested)

    # Build final config-style summary: include message fields for failures
    final_config: Dict[str, str] = {}
    for name, res in results.items():
        final_config[name] = res["result"]
        if res["result"] != "success":
            final_config[f"{name}_message"] = res["message"]

    print("\nFinal Results Summary:")
    print(json.dumps(final_config, indent=2))