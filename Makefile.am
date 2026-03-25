ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	pyproject.toml \
	README.md \
	LICENSE \
	src \
	tests \
	docs

check-local:
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) -m pytest -c $(top_srcdir)/pyproject.toml

.PHONY: check-local
