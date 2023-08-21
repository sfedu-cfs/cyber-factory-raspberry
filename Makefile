.PHONY: test system_analyzers

.ONESHELL:

test:
	export $(shell cat .env | xargs)
	sudo -E env PATH=$$PATH PYTHONPATH=./ python -m pytest -v -s tests/system_analyzer/

system_analyzers:
	export $(shell cat .env | xargs)

	PYTHONPATH=./ python src/system_analyzer/apps.py > logs/apps_output.log
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/arp_table.py > logs/arp_table_output.log
	python src/system_analyzer/network_interfaces.py > logs/network_interfaces_output.log
	python src/system_analyzer/resources.py > logs/resources_output.log
	python src/system_analyzer/system_services.py > logs/system_services_output.log
	python src/system_analyzer/sfc.py > logs/sfc_output.log

hosts:
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/hosts.py > logs/hosts_output.log

ports:
	sudo -E env PATH=$$PATH PYTHONPATH=./ python src/system_analyzer/ports.py > logs/ports_output.log