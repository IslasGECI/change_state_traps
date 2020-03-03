.PHONY: clean mutation tests

mutation:
	mutmut run --paths-to-mutate change_state_traps 

tests:
	pytest --cov=change_state_traps --cov-report=term --verbose

clean:
	rm --force --recursive $$(find . -name "__pycache__")
	rm --force --recursive .pytest_cache
	rm --force .coverage
	rm --force .mutmut-cache