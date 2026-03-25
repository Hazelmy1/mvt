AC_PREREQ([2.69])
m4_define([MVT_VERSION], m4_normalize(m4_esyscmd([
python3 - <<'EOF'
import sys
from pathlib import Path
import re

version_file = Path("src/mvt/common/version.py")
if not version_file.exists():
    sys.stderr.write("Error: src/mvt/common/version.py not found\n")
    raise SystemExit(1)

match = re.search(r'MVT_VERSION\s*=\s*[\'"]([^\'"]+)[\'"]', version_file.read_text(encoding="utf-8"))
if not match:
    sys.stderr.write("Error: Could not extract MVT_VERSION from src/mvt/common/version.py\n")
    raise SystemExit(1)

print(match.group(1))
EOF
])))
AC_INIT([mvt], [MVT_VERSION], [https://github.com/mvt-project/mvt/issues])
AC_CONFIG_SRCDIR([pyproject.toml])
AC_CONFIG_MACRO_DIRS([m4])
AM_INIT_AUTOMAKE([foreign])
AM_PATH_PYTHON([3.10])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
