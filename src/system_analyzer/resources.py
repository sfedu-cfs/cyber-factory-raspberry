import os
import psutil


def dynamic_collect_send():
    """
    Collects system resource information and formats it into a dictionary.

    This function collects various system resource information, such as CPU usage, RAM usage, disk usage, and more.
    The collected information is then formatted into a dictionary structure.

    Returns:
        dict: A dictionary containing the collected system resource information.
    """
    avg_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    cpu_temp = psutil.sensors_temperatures()
    output = {
        "system_resources": {
            "cpu": {
                "cpu_usage": psutil.cpu_percent(),
                "cpu_frequency": psutil.cpu_freq().current,
                "avg_load": avg_load[0],
            },
            "ram": {
                "ram_usage": psutil.virtual_memory().percent,
                "swap_usage": psutil.swap_memory().percent,
            },
            "general": {
                "uptime": os.popen('uptime -p').read()[:-1],
                "disk_usage": psutil.disk_usage('/').percent,
            },
        },
    }
    return output
