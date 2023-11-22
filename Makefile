.PHONY: test system_analyzers network_analyzer start reg_device

.ONESHELL:

# TODO: make clean command

test:
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python -m pytest -v -s tests/

network_analyzer:
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/network_analyzer/network_analyzer.py

system_analyzer:
	sudo -E env PATH=$$PATH PYTHONPATH=./ python start.py

reg_device:
	export $(shell cat .env | xargs)

	PATH=$$PATH PYTHONPATH=./ python src/core/reg_device.py

test_coverage:
	export $(shell cat .env | xargs)

	sudo -E env PATH=$$PATH PYTHONPATH=./ coverage run -m pytest