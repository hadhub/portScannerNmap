# Discovery scan using python-nmap
import nmap
from progress.bar import Bar

# Local IP addr - CIDR
ip = str(input("Enter the network address : "))
cidr = str(input("Enter CIDR notation (ex /24) : "))
host = ip + cidr

# Objects
DiscoveryScanner = nmap.PortScanner()
BarScan = Bar('Scanning : ', max=3)

# Progress Bar
for i in range(3):
    DiscoveryScanner.scan(hosts=host, arguments='-F')
    BarScan.next()
BarScan.finish()

# Display
for host in DiscoveryScanner.all_hosts():
    print(host)
