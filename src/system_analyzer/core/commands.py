GET_NETWORK_INTERFACES_IPS_COMMAND = "ip addr | grep inet|grep -v 'inet6'|awk '{print $NF, $2}'"
GET_NETWORK_INTERFACES_NAMES_COMMAND = """ip addr | awk '/^[0-9]+:/ {sub(/:/,"",$2); print $2}'"""
GET_INSTALLED_APPLICATIONS = """echo "$(lsb_release -si)\t$(lsb_release -sr)" && dpkg-query -W 
-f='${Package}\t${Version}\n'"""
GET_SYSTEM_SERVICES_INFO = ["systemctl", "list-units", "--type=service", "--no-pager"]
# NMAP
SCAN_TCP_PORT_COMMAND = "nmap -oX {} {}"
SCAN_UPD_PORT_COMMAND = "nmap  -sU -oX {} {}"
SCAN_PROTOCOLS_COMMAND = "sudo nmap -sO -oX {} {}"
