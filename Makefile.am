ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	pyproject.toml \
	README.md \
	LICENSE \
	scripts/extract_version.py \
	scripts/check_test_prereqs.py \
	src \
	tests \
	docs

install-exec-local:
	$(PYTHON) -m pip install --upgrade $(top_srcdir)

check-local:
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) scripts/check_test_prereqs.py
	$(AM_V_at)cd $(top_srcdir) && $(PYTHON) -m pytest -c $(top_srcdir)/pyproject.toml

.PHONY: check-local install-exec-local
