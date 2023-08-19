import os
import psutil

from src.schemas.monitor_resources import (MonitorResource, BaseMonitorResource, CPUMonitorResource, RAMMonitorResource,
                                           GeneralMonitorResource)
from src.core.log_config import logger


class SystemResourcesCollector:
    @staticmethod
    def collect():
        """
        Collects the system resources.

        This method collects various system resource information using the psutil library and creates instances of the
        corresponding Pydantic models. The collected information includes CPU load, CPU usage, average CPU load, RAM
        usage, swap usage, disk usage, and system uptime.

        Returns:
            MonitorResource: An instance of the MonitorResource class containing the collected system resource
            information.
        """
        try:
            cpu_monitor = CPUMonitorResource(
                cpu_load=psutil.cpu_percent(),
                cpu_usage=psutil.cpu_percent(),
                cpu_avg_load=[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()][0],
                # cpu_temperature=psutil.sensors_temperatures(),
            )

            ram_monitor = RAMMonitorResource(
                ram_usage=psutil.virtual_memory().percent,
                swap_usage=psutil.swap_memory().percent,
            )

            general_monitor = GeneralMonitorResource(
                disk_usage=psutil.disk_usage('/').percent,
                uptime=os.popen('uptime -p').read()[:-1],
            )

            system_resources = MonitorResource(
                system_resources=BaseMonitorResource(
                    cpu=cpu_monitor,
                    ram=ram_monitor,
                    general=general_monitor,
                )
            )
        except Exception as e:
            logger.error(f"Error collecting system resources: {e}")
            raise e

        return system_resources


sr = SystemResourcesCollector().collect()
print(sr.model_dump_json(by_alias=True, indent=4))
