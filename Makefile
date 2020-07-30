all: mutants

.PHONY: all clean format install lint mutants tests

repo = change_state_traps

mutants:
	mutmut run --paths-to-mutate ${repo} 

tests:
	pytest --cov=${repo} --cov-report=term --verbose

format:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests

install:
	pip install --editable .

lint:
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests
	pylint ${repo}
	pylint tests

clean:
	rm --force .mutmut-cache
	rm --recursive --force ${repo}.egg-info
	rm --recursive --force ${repo}/__pycache__
	rm --recursive --force tests/__pycache__
	rm --recursive --force .pytest_cache
	rm --force .coverage
	rm --force coverage.xml