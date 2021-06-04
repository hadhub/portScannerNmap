import nmap

scanner = nmap.PortScanner()

ip_addr = input("Target IP : ")
portRange = input("Enter a port range (ex : 0-1024) : ")

scanner.scan(ip_addr, portRange, '-v -sS')

print(scanner.scaninfo())
print("Ip Status: ", scanner[ip_addr].state())
print(scanner[ip_addr].all_protocols())
print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
