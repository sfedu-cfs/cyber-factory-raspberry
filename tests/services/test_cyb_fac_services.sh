# this sh script runs python test for src.system_analyzer.arp_table.py with root permissions
PYTHONPATH=/home/lowqa/WORK/dev_repositories/factory_analyzer/
sudo -E /home/lowqa/WORK/dev_repositories/cyber-factory-raspberry/venv/bin/python -m pytest -v -s tests/services/test_cyber_factory_services.py

