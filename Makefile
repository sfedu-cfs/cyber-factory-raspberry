.PHONY: test system_analyzers network_analyzer start reg_device

.ONESHELL:

# TODO: make clean command

test:
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python -m pytest -v -s tests/

system_analyzer:
	sudo -E env PATH=$$PATH PYTHONPATH=./ python start.py

config:
	export $(shell cat .env | xargs)

	PATH=$$PATH PYTHONPATH=./ python src/core/start_conf_checker.py

test_coverage:
	export $(shell cat .env | xargs)

	sudo -E env PATH=$$PATH PYTHONPATH=./ coverage run -m pytest