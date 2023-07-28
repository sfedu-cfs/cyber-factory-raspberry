import ipaddress
import random

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1


def random_ipv4(count=1):
    ip_list = []
    for _ in range(count):
        ip_list.append(ipaddress.IPv4Address._string_from_ip_int(
            random.randint(0, MAX_IPV4)
        ))
    
    if count == 1:
        return ip_list[0]
    return ip_list


def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
