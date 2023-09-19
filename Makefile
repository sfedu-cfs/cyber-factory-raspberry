.PHONY: test system_analyzers network_analyzer start

.ONESHELL:

# TODO: make clean command

test:
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python -m pytest -v -s tests/

system_analyzers:
	export $(shell cat .env | xargs)

	PYTHONPATH=./ python src/system_analyzer/apps.py > tmp/apps_output.log
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/arp_table.py > tmp/arp_table_output.log
	python src/system_analyzer/network_interfaces.py > tmp/network_interfaces_output.log
	python src/system_analyzer/resources.py > tmp/resources_output.log
	python src/system_analyzer/system_services.py > tmp/system_services_output.log
	python src/system_analyzer/sfc.py > tmp/sfc_output.log
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/hosts.py > tmp/hosts_output.log
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/ports.py > tmp/ports_output.log

network_analyzer:
	# TODO: make dynamic name of log file and put it in tmp directory
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/network_analyzer/network_analyzer.py > tmp/network_analyzer_output.log

start:
	sudo -E env PATH=$$PATH PYTHONPATH=./ python start.py