from scapy.all import *
import requests, configparser



class Count:
    """
    This class is used to display the number of network packets 
    since the beginning of the program or during a specified time
    """
    def __init__(self, time):
        """
        args
        time: datetime type - need for start working. Gets current system time
        """
        self.url = None
        self.time_last_update = time # need for update object, when the set timing has passed 
        self.timing = 0 # preset time in settings.ini
        self.total_count = 0 # number of all packets? which were detected by the sniffer for timing 
        self.tcp_count = 0
        self.udp_count = 0
        self.http_request = 0
        self.http_response = 0
        self.arp_count = 0
        self.icmp_count = 0
        """
        The elements below are designed to store the number of packets 
        of the ModBus protocol by different function codes
        """
        self.modbus_01_request = 0
        self.modbus_02_request = 0
        self.modbus_03_request = 0
        self.modbus_04_request = 0
        self.modbus_05_request = 0
        self.modbus_06_request = 0
        self.modbus_15_request = 0
        self.modbus_16_request = 0
        self.modbus_01_response = 0
        self.modbus_02_response = 0
        self.modbus_03_response = 0
        self.modbus_04_response = 0
        self.modbus_05_response = 0
        self.modbus_06_response = 0
        self.modbus_15_response = 0
        self.modbus_16_response = 0
        
    def make_json(self):
        """
        Make JSON-object
        Returns:
            dict: data in JSON-form 
        """
        count_json = {
            "device_id": Count.get_mac(),
            "timing": self.timing,
            "all_proto_count": self.total_count,
            "tcp_count": self.tcp_count,
            "udp_count": self.udp_count,
            "http_request_count": self.http_request,
            "http_response_count": self.http_response,
            "arp_count": self.arp_count,
            "icmp_count": self.icmp_count,
            "modbus_01_request_count": self.modbus_01_request,
            "modbus_02_request_count": self.modbus_02_request,
            "modbus_03_request_count": self.modbus_03_request,
            "modbus_04_request_count": self.modbus_04_request,
            "modbus_05_request_count": self.modbus_05_request,
            "modbus_06_request_count": self.modbus_06_request,
            "modbus_15_request_count": self.modbus_15_request,
            "modbus_16_request_count": self.modbus_16_request,
            "modbus_01_response_count": self.modbus_01_response,
            "modbus_02_response_count": self.modbus_02_response,
            "modbus_03_response_count": self.modbus_03_response,
            "modbus_04_response_count": self.modbus_04_response,
            "modbus_05_response_count": self.modbus_05_response,
            "modbus_06_response_count": self.modbus_06_response,
            "modbus_15_response_count": self.modbus_15_response,
            "modbus_16_response_count": self.modbus_16_response
        }
        return count_json
    
    def send_to_server(self):
        config = configparser.ConfigParser()
        config.read("./src/network_analyzer/settings.ini")
        url = config["traffic"]["url"]
        requests.post(url, json=self.make_json())
    
    @staticmethod
    def get_mac():
        eth = Ether()
        return eth[Ether].src
    
    