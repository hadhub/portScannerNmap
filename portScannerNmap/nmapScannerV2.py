import nmap
# Importation de la lib Bar et de l'objet Bar
# from progress.bar import Bar

# Creation de l'objet
scanner = nmap.PortScanner()
# Input ; IP ; Port number
ip_addr = input("Target IP : ")
portRange = input("Enter a port range (ex : 0-1024) : ")
# Display Options
resp = input("""\n 
Options : 
    1) SYN ACK Scan
    2) Comprehensive Scan
    3) Host Discovery (Soon)
    
> """)
# Scan de port : SYN
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    # Instanciation de l'objet Bar
    scanner.scan(ip_addr, portRange, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
# Scan de port : SYN ; Detection des services & versions & OS & Scan Agressif
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, portRange, '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
# Erreur si l'utilisateur se trompe d'options de scan
elif resp >= '4':
    print("Please enter a valid option")

