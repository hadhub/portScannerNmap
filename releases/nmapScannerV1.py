import nmap

# Création de l'objet
scanner = nmap.PortScanner()
# Input & Cast
ip_addr = input("Target IP : ")
type(ip_addr)
# Display Options
resp = input("""\n Options : 
                1)SYN ACK Scan
                2)Comprehensive Scan \n""")
# Scan de port : SYN
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
# Scan de port : SYN ; Detection des services & versions & OS & Scan Agressif
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    print("Please enter a valid option")


