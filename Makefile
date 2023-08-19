.PHONY: test, system_services

test:
	sudo -E env PATH=$$PATH python -m pytest -v -s


system_services:
	python src/system_analyzer/system_services.py
