import socket
import fcntl
import struct
import subprocess
import os
from dotenv import set_key

from src.system_analyzer.network_interfaces import ni


def get_primary_interface_name():
    try:
        default_gateway = os.popen("ip route show default").read().split()
        interface_name = default_gateway[default_gateway.index('dev') + 1]
        return interface_name
    except ValueError:
        return None


def get_mac_address(interface_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', bytes(interface_name[:15], 'utf-8')))
    return ''.join(['%02x:' % b for b in info[18:24]])[:-1]


def get_ip_address(interface_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', bytes(interface_name[:15], 'utf-8'))
        )[20:24])
    except IOError:
        return None


def get_gateway_address(interface_name):
    try:
        proc = subprocess.Popen(['ip', 'route', 'show', 'dev', interface_name], stdout=subprocess.PIPE)
        default_route = proc.stdout.read().decode('utf-8')
        gateway_address = default_route.split()[2]
        return gateway_address
    except IndexError:
        return None


def set_default_iface():
    interface_name = get_primary_interface_name()
    if interface_name is None:
        print("Could not find the primary network interface.")
        return
    mac_address = get_mac_address(interface_name)
    write_to_env(interface_name, mac_address)


def set_iface(interface_name):
    mac_address = get_mac_address(interface_name)
    write_to_env(interface_name, mac_address)


def write_to_env(interface_name, mac_address):
    env_path = '.env'
    set_key(env_path, 'NET_IFACE', interface_name)
    set_key(env_path, 'MAC_ADDRESS', mac_address)

    ip_address = get_ip_address(interface_name)
    if ip_address is not None:
        set_key('.env', 'IP_ADDRESS', ip_address)
    default_gateway = get_gateway_address(interface_name)
    if default_gateway is not None:
        set_key('.env', 'DEFAULT_GATEWAY', default_gateway)


if __name__ == "__main__":
    print("This module can help you to setup network interface for working.")
    print("Please, choose network interface for working:")
    print("1) Default (will be used primary network interface)")
    network_interfaces = ni.collect().model_dump(by_alias=True)["items"]
    for interface in network_interfaces:
        print(f"{network_interfaces.index(interface) + 2}) {interface['name']}")
    print("Enter network interface number:")
    iface_number = str(input())

    if iface_number == "1":
        set_default_iface()
    else:
        set_iface(network_interfaces[int(iface_number) - 2]["name"])
