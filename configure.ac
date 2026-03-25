AC_PREREQ([2.69])
m4_define([MVT_VERSION], m4_esyscmd_s([python3 scripts/extract_version.py]))
AC_INIT([mvt], [MVT_VERSION], [https://github.com/mvt-project/mvt/issues])
AC_CONFIG_SRCDIR([pyproject.toml])
AC_CONFIG_MACRO_DIRS([m4])
AM_INIT_AUTOMAKE([foreign])
AM_PATH_PYTHON([3.10])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
