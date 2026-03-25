ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	pyproject.toml \
	README.md \
	LICENSE \
	src \
	tests \
	docs

check-local:
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) -c "import importlib.util, pathlib, sys; \
config = pathlib.Path('pyproject.toml'); \
config.exists() or sys.exit('Error: pyproject.toml not found in project root.'); \
importlib.util.find_spec('pytest') or sys.exit('Error: pytest is not installed. Install dev requirements first.')" && \
	$(PYTHON) -m pytest -c $(top_srcdir)/pyproject.toml

.PHONY: check-local
