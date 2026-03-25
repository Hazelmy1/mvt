AC_PREREQ([2.69])
m4_define([MVT_VERSION], m4_esyscmd_s([python3 -c "import pathlib, re, sys; \
p = pathlib.Path('src/mvt/common/version.py'); \
text = p.read_text(encoding='utf-8') if p.exists() else sys.exit('Error: src/mvt/common/version.py not found'); \
m = re.search(r\"MVT_VERSION\\s*=\\s*(['\\\"])([^'\\\"]+)\\1\", text); \
sys.exit('Error: Could not extract MVT_VERSION from src/mvt/common/version.py') if m is None else print(m.group(2))"]))
AC_INIT([mvt], [MVT_VERSION], [https://github.com/mvt-project/mvt/issues])
AC_CONFIG_SRCDIR([pyproject.toml])
AC_CONFIG_MACRO_DIRS([m4])
AM_INIT_AUTOMAKE([foreign])
AM_PATH_PYTHON([3.10])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
