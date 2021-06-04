from progress.bar import Bar
import nmap

# IP DE TEST :
# beuchat : 213.186.33.4
# mbn : 80.247.233.138
# 0-1024

scanner = nmap.PortScanner()

ip_addr = input("Target IP : ")
portRange = input("Enter a port range (ex : 0-1024) : ")

with Bar('Processing', max=5) as bar:
    for i in range(5):
        # Do some work
        statusScan = scanner.scan(ip_addr, portRange, '-v -sS')
        bar.next()
        if statusScan:
            bar.finish()

    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
