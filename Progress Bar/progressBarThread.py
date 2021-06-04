from threading import Thread
import nmap


scanner = nmap.PortScanner()

ip_addr = input("Target IP : ")
portRange = input("Enter a port range (ex : 0-1024) : ")

print("Nmap Version: ", scanner.nmap_version())
# Instanciation de l'objet Bar
scanner.scan(ip_addr, portRange, '-v -sS')
scan_thread = Thread(target=scanner.scan, args=(ip_addr, portRange,))
scan_thread.start()
while True:
    scan_thread.join(timeout=3)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    if not scan_thread.is_alive():
        break
    print('Nmap is still running...')
