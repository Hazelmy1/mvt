AC_PREREQ([2.69])
m4_define([MVT_VERSION], m4_normalize(m4_esyscmd([
python - <<'EOF'
from pathlib import Path
import re

text = Path("src/mvt/common/version.py").read_text()
match = re.search(r'MVT_VERSION\s*=\s*"([^"]+)"', text)
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
