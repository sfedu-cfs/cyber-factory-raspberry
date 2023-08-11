.PHONY: test

test:
	sudo -E venv/bin/python -m pytest -v -s tests/
