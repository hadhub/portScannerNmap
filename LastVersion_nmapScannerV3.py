import nmap
import socket
from progress.bar import Bar

"""
Add :
[Automation] Put Default value (For V3) : OK
[Automation] Convert hostname to IPV4 format (For V3) : OK
[Design] Progess Bar (For V3) : OK

Code :
    - 1 Print menu : Asking user about the IP & Range Port
        + Convert hostname to IPV4 for scan 

    - 1 Scanning (SYN/ACK Scan)
        + Args : -sS
"""

print("-" * 50)
# Using str() when user copy & paste IP from web browser
hostname = str(input("[?] Enter hostname : "))
port_range = str(input("[?] Range port (default value is 0-1024) : "))
print("-" * 50)
# Verification of user inputs
if port_range == '':
    port_range = "0-1024"
else:
    print("[*] Value entered : ", port_range)

if hostname == '':
    print("[*] Enter valid hostname")
else:
    print("[*] Hostname entered : ", hostname)
# Hostname to ipV4 (socket)
ip_v4 = socket.gethostbyname(hostname)
print("[*] IpV4 of hostname : ", ip_v4)
print("-" * 50)

#  ! Scan SYN/ACK
# Instantiation of the Scanner object
Scanner = nmap.PortScanner()
bar = Bar('Processing', max=3)
for i in range(3):
    state = Scanner.scan(ip_v4, port_range)
    bar.next()
bar.finish()

print("-" * 50)
# Display without cast (.state() return the state of IP in str)
ip_status = Scanner[ip_v4].state()
print("[*] Ip Status : ", ip_status)

# Display of the used protocol
protocol_list = Scanner[ip_v4].all_protocols()
print("[*] Protocol : ", *protocol_list)

# Display of open ports
open_port = Scanner[ip_v4]['tcp'].keys()
print("[*] Open Ports: ", *open_port)
print("-" * 50)
