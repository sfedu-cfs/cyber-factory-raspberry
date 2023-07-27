import os
import configparser
import time

import requests
import psutil
import schedule


config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

def dynamic_collect_send():
    dict(psutil.virtual_memory()._asdict())
    avg_load = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    #cpu_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
    cpu_temp = psutil.sensors_temperatures()
    output = {
        "system_resources": {
            "cpu": {
                "cpu_usage": psutil.cpu_percent(),
                "cpu_frequency": psutil.cpu_freq().current,
                "avg_load": avg_load[0],
                #"temp": cpu_temp
            },
            "ram": {
                "ram_usage": psutil.virtual_memory().percent,
                "swap_usage": psutil.swap_memory().percent
            },
            "general": {
                "uptime": os.popen('uptime -p').read()[:-1],
                "disk_usage": psutil.disk_usage('/').percent                
            }
        }
        }
    #print(json.dumps(output, indent=4))
    requests.post(config["dynamic"]["url"], json=output)
    
schedule.every(config["dynamic"]["freq_collect"]).seconds.do(dynamic_collect_send)

while True:
    schedule.run_pending()
    
if __name__ == "__main__":
    dynamic_collect_send()