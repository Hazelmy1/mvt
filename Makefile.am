ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	pyproject.toml \
	README.md \
	LICENSE \
	scripts/check_test_prereqs.py \
	src \
	tests \
	docs

check-local:
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) scripts/check_test_prereqs.py
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) -m pytest -c $(top_srcdir)/pyproject.toml

.PHONY: check-local
