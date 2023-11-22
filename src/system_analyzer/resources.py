import os
import psutil

from src.schemas.monitor_resources import (
    MonitorResource,
    CPUMonitorResource,
    RAMMonitorResource,
    GeneralMonitorResource
)
from src.core.log_config import logger


# TODO: почитать про @property


class SystemResourcesCollector:
    def collect(self):
        """
        Collects the system resources.

        This method collects various system resource information using the psutil library and creates instances of the
        corresponding Pydantic models. The collected information includes CPU load, CPU usage, average CPU load, RAM
        usage, swap usage, disk usage, and system uptime.

        Returns:
            MonitorResource: An instance of the MonitorResource class containing the collected system resource
            information.
        """
        system_resources = MonitorResource(
            cpu_load=self._cpu_monitor.cpu_load,
            cpu_usage=self._cpu_monitor.cpu_usage,
            cpu_avg_load=self._cpu_monitor.cpu_avg_load,
            cpu_temperature = self._cpu_monitor.cpu_temperature,
            ram_usage=self._ram_monitor.ram_usage,
            swap_usage=self._ram_monitor.swap_usage,
            disk_usage=self._general_monitor.disk_usage,
            uptime=self._general_monitor.uptime,
        )

        return system_resources

    @property
    def _cpu_monitor(self):
        """
        Gets the CPU monitor.

        This method collects the CPU load, CPU usage, average CPU load, and CPU temperature using the psutil library
        and creates an instance of the CPUMonitorResource Pydantic model.

        Returns:
            CPUMonitorResource: An instance of the CPUMonitorResource class containing the collected CPU information.
        """
        try:
            cpu_monitor = CPUMonitorResource(
                cpu_load=psutil.cpu_percent(),
                cpu_usage=psutil.cpu_percent(),
                cpu_avg_load=[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()][0],
                # cpu_temperature=psutil.sensors_temperatures()['cpu_thermal'][0].current
            )
        except Exception as e:
            logger.error(f"Error collecting CPU monitor: {e}")
            raise e

        return cpu_monitor

    @property
    def _ram_monitor(self):
        """
        Gets the RAM monitor.

        This method collects the RAM usage and swap usage using the psutil library and creates an instance of the
        RAMMonitorResource Pydantic model.

        Returns:
            RAMMonitorResource: An instance of the RAMMonitorResource class containing the collected RAM information.
        """
        try:
            ram_monitor = RAMMonitorResource(
                ram_usage=psutil.virtual_memory().percent,
                swap_usage=psutil.swap_memory().percent,
            )
        except Exception as e:
            logger.error(f"Error collecting RAM monitor: {e}")
            raise e

        return ram_monitor

    @property
    def _general_monitor(self):
        """
        Gets the general monitor.

        This method collects the disk usage and system uptime using the psutil library and creates an instance of the
        GeneralMonitorResource Pydantic model.

        Returns:
            GeneralMonitorResource: An instance of the GeneralMonitorResource class containing the collected general
            information.
        """
        try:
            general_monitor = GeneralMonitorResource(
                disk_usage=psutil.disk_usage('/').percent,
                uptime=os.popen('uptime -p').read()[:-1],
            )
        except Exception as e:
            logger.error(f"Error collecting general monitor: {e}")
            raise e

        return general_monitor
