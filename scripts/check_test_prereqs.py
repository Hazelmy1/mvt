#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parent.parent
    config_path = project_root / "pyproject.toml"
    if not config_path.exists():
        sys.stderr.write("Error: pyproject.toml not found in project root.\n")
        return 1

    if importlib.util.find_spec("pytest") is None:
        sys.stderr.write(
            "Error: pytest is not installed. Install dev requirements first "
            "(e.g., run `make test-requirements`).\n"
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
