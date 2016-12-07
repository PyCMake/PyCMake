.PHONY: clean-pyc clean-build clean-skbuild docs clean

help:
	@echo "$(MAKE) [target]"
	@echo
	@echo "  targets:"
	@echo "    clean-build - remove build artifacts"
	@echo "    clean-pyc   - remove Python file artifacts"
	@echo "    lint        - check style with flake8"
	@echo "    test        - run tests quickly with the default Python"
	@echo "    test-all    - run tests on every Python version with tox"
	@echo "    coverage    - check code coverage quickly with the default Python"
	@echo "    docs        - generate Sphinx HTML documentation, including API docs"
	@echo "    release     - package and upload a release"
	@echo "    dist        - package"
	@echo

clean: clean-build clean-pyc clean-skbuild
	rm -fr htmlcov/
	find . -name '.coverage' -exec rm -f {} +
	find . -name 'coverage.xml' -exec rm -f {} +
	rm -rf .cache

clean-build:
	rm -fr build/
	rm -fr dist/
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	find . -type f -name 'MANIFEST' -exec rm -f {} +
	find tests/samples/*/dist/ -type d -exec rm -rf {} + > /dev/null 2>&1 || true

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-skbuild:
	rm -rf _skbuild
	find tests/samples/*/_skbuild/ -type d -exec rm -rf {} + > /dev/null 2>&1 || true

lint:
	flake8

test:
	python setup.py test

test-all:
	tox

coverage: test
	coverage html
	open htmlcov/index.html || xdg-open htmlcov/index.html

docs-only:
	rm -f docs/skbuild.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ -M  skbuild
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

docs: docs-only
	open docs/_build/html/index.html || xdg-open docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
