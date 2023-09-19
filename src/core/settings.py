import os
import configparser

# Construct the path to the settings file
config_path = os.path.join(os.path.dirname(__file__), '../../settings.ini')

# Check if the file exists
if not os.path.exists(config_path):
    # Set default values if the file doesn't exist
    default_config = """
    [NetworkAnalyzer]
    timings = 5, 20, 60, 300, 600, 1200, 2400, 3600

    [SendTimePeriods]
    collect_system_services = 2
    collect_hosts = 3
    collect_ports = 1
    collect_monitoring = 4
    collect_applications = 2
    collect_sfc = 1
    collect_arp_table =  4
    collect_network_interfaces = 2
    """
    config = configparser.ConfigParser()
    config.read_string(default_config)
else:
    # Create a parser object
    config = configparser.ConfigParser()
    # Read data from the settings file
    config.read(config_path)