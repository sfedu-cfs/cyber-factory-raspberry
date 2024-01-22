import schedule
import time

from sqlalchemy.exc import IntegrityError

from src.system_analyzer.system_services import SystemServicesCollector
from src.system_analyzer.hosts import HostCollector
from src.system_analyzer.ports import PortCollector
from src.system_analyzer.resources import SystemResourcesCollector
from src.system_analyzer.apps import AppsCollector
from src.system_analyzer.sfc import SFCCollector
from src.system_analyzer.arp_table import ArpTableCollector
from src.system_analyzer.network_interfaces import NetworkInterfaces
from src.system_analyzer.connections import ConnectionsCollector
from src.core.settings import config
from src.database.dao.apps_dao import AppDAO, AppCurrentDAO
from src.database.dao.hosts_dao import HostsDAO, HostsCurrentDAO
from src.database.dao.ports_dao import PortsDAO, PortsCurrentDAO
from src.database.dao.monitor_resources_dao import MonitorResourcesDAO
from src.database.dao.system_services_dao import SystemServicesDAO, SystemServicesCurrentDAO
from src.database.dao.sfc_dao import SFCDao, SFCCurrentDao
from src.database.dao.arp_table_dao import ArpTableDAO, ArpTableCurrentDAO
from src.database.dao.interfaces_dao import NetworkInterfacesDAO, NetworkInterfacesCurrentDAO
from src.database.dao.connections_dao import ConnectionsDAO, ConnectionsCurrentDAO
from src.database.connection import Session


class Collector:
    def __init__(self, collector_class, dao_class, dao_current_class=None):
        self.collector_class = collector_class
        self.dao_class = dao_class
        self.dao_current_class = dao_current_class

    def collect(self):
        session = Session()
        try:
            if self.dao_current_class is None:
                collector = self.collector_class()
                dao = self.dao_class(db=session)
                data = collector.collect()
                dao.create(data.model_dump())
                session.commit()
            else:
                collector = self.collector_class()
                dao = self.dao_class(db=session)
                current_dao = self.dao_current_class(db=session)
                # Удаляем все записи из текущей таблицы
                current_dao.delete_all()
                data = collector.collect()
                # Проверяем, что данные не пустые
                if type(data) != list and data.items:
                    for item in data.items:
                        if not current_dao.exists(item):
                            current_dao.create(item.model_dump())
                        if dao.exists(item):
                            continue
                        dao.create(item.model_dump())
                    session.commit()
                elif type(data) == list:
                    for host in data:
                        ip = host.ip_address
                        for item in host.items:
                            current_dao.create(item.model_dump(), ip)
                            if dao.exists(item, ip):
                                continue
                            dao.create(item.model_dump(), ip)
                        session.commit()

        except IntegrityError as e:
            session.rollback()
        finally:
            session.close()


collectors = [
    Collector(SystemServicesCollector, SystemServicesDAO, SystemServicesCurrentDAO),
    Collector(HostCollector, HostsDAO, HostsCurrentDAO),
    Collector(PortCollector, PortsDAO, PortsCurrentDAO),
    Collector(SystemResourcesCollector, MonitorResourcesDAO),
    Collector(AppsCollector, AppDAO, AppCurrentDAO),
    Collector(SFCCollector, SFCDao, SFCCurrentDao),
    Collector(ArpTableCollector, ArpTableDAO, ArpTableCurrentDAO),
    Collector(NetworkInterfaces, NetworkInterfacesDAO, NetworkInterfacesCurrentDAO),
    Collector(ConnectionsCollector, ConnectionsDAO, ConnectionsCurrentDAO)
]


def job(collector):
    collector.collect()


def schedule_coroutine(job, collector):
    def wrapper():
        job(collector)

    return wrapper


def main():
    for collector, time_period in zip(collectors, config["SendTimePeriods"].values()):
        print(collector.collector_class.__name__, time_period)
        time_period_hours = int(time_period)
        schedule.every(time_period_hours).seconds.do(schedule_coroutine(job, collector))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
