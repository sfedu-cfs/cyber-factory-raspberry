from src.database.models.apps import App, AppCurrent
from src.database.models.arp_table import ArpTable, ArpTableCurrent
# from src.database.models.count_packet import CountPacketsAll, CountPacketsInput, CountPacketsOutput
from src.database.models.hosts import Hosts, HostsCurrent
from src.database.models.interfaces import NetworkInterfaces, NetworkInterfacesCurrent
from src.database.models.monitor_resources import MonitorResources
from src.database.models.ports import Ports, PortsCurrent
from src.database.models.sfc import SFC, SFCCurrent
from src.database.models.system_services import SystemServices, SystemServicesCurrent
from src.database.connection import Base, engine
from src.core.log_config import logger

Base.metadata.create_all(engine)

# Log the table creation
logger.info("Tables created in the database")
