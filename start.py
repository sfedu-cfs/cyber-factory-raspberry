import schedule
import time
import threading

from src.services.cyber_factory_service import CyberFactoryService
from src.system_analyzer.system_services import SystemServicesCollector
from src.system_analyzer.hosts import HostCollector
from src.system_analyzer.ports import PortCollector
from src.system_analyzer.resources import SystemResourcesCollector
from src.system_analyzer.apps import AppsCollector
from src.system_analyzer.sfc import SFCCollector
from src.system_analyzer.arp_table import ArpTableCollector
from src.system_analyzer.network_interfaces import NetworkInterfaces
from src.core.settings import config
from src.network_analyzer.network_analyzer import start
from src.core.log_config import logger


def collect_system_services():
    services = SystemServicesCollector()
    return services.collect().model_dump(by_alias=True)


def collect_hosts():
    hosts = HostCollector()
    return hosts.collect().model_dump(by_alias=True)


def collect_ports():
    ports = PortCollector()
    return ports.collect()


def collect_resources():
    monitoring = SystemResourcesCollector()
    return monitoring.collect().model_dump(by_alias=True)


def collect_applications():
    applications = AppsCollector()
    return applications.collect().model_dump(by_alias=True)


def collect_sfc():
    sfc = SFCCollector()
    return sfc.collect().model_dump(by_alias=True)


def collect_arp_table():
    arp_table = ArpTableCollector()
    return arp_table.collect().model_dump(by_alias=True)


def collect_network_interfaces():
    network_interfaces = NetworkInterfaces()
    return network_interfaces.get_list_network_interfaces().model_dump_json(by_alias=True)


def collect_network_analyzer_and_send():
    # Implement the logic to collect count packets data
    count_packets_data = start()


lock = threading.Lock()


def job(collector_func, send_func):
    lock.acquire()
    try:
        collector_data = collector_func()
        service.__getattribute__(send_func)(collector_data)
    finally:
        lock.release()


# Create an instance of the CyberFactoryService class
service = CyberFactoryService()

# Schedule the send functions with custom time periods
for send_func, time_period in config["SendTimePeriods"].items():
    # Extract the collector function name
    collector_func_name = send_func.replace("send_", "collect_")

    # Convert the time period to hours
    time_period_hours = int(time_period)

    # Get the collector function
    collector_func = globals()[collector_func_name]

    # Schedule the send function with the specified time period and pass arguments to the collector function
    # schedule.every(time_period_hours).hours.do(service.__getattribute__(send_func), collector_func())
    schedule.every(time_period_hours).seconds.do(job, collector_func=collector_func, send_func=send_func)
# Start the thread to collect and send count packets data
# count_packets_thread = threading.Thread(target=collect_network_analyzer_and_send)
# count_packets_thread.start()

# Run the scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
