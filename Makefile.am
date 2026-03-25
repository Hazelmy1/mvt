ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	pyproject.toml \
	README.md \
	LICENSE \
	src \
	tests \
	docs \
	Makefile

check-local:
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) -m pytest

.PHONY: check-local
