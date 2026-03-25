#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    version_path = Path(__file__).resolve().parent.parent / "src/mvt/common/version.py"
    if not version_path.exists():
        sys.stderr.write(f"Error: {version_path} not found\n")
        return 1

    match = re.search(
        r"MVT_VERSION\s*=\s*(['\"])(.*?)\1",
        version_path.read_text(encoding="utf-8"),
    )
    if not match:
        sys.stderr.write(f"Error: Could not extract MVT_VERSION from {version_path}\n")
        return 1

    sys.stdout.write(match.group(2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
