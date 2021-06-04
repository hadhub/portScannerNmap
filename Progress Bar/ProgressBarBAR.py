"""
Fichier de test pour la progress bar : OK
Affichage propre via cast de list : Ok (80%)
"""
from progress.bar import Bar
import nmap

# IP DE TEST :
# scanme.nmap.org : 45.33.32.156
# 0-1024

Scanner = nmap.PortScanner()

ip_addr = input("Target IP : ")
port_range = input("Enter a port range (ex : 0-1024) : ")

with Bar('Processing', max=5) as bar:
    for i in range(5):
        status_scan = Scanner.scan(ip_addr, port_range, '-v -sS')
        bar.next()
        if status_scan:
            bar.finish()

    # Comment cast 2 dictionnaires en 1 puis cast en STR XD MDR LOL
    print("Scan Information : ", Scanner.scaninfo())

    # Affichage sans cast (.state() retourne une str)
    ip_status = Scanner[ip_addr].state()
    print("Ip Status : ", ip_status)

    # Affichage du protocol utilisé avec * : OK
    protocol_list = Scanner[ip_addr].all_protocols()
    print("Protocol : ", *protocol_list)

    # Affichage avec * : OK
    open_port = Scanner[ip_addr]['tcp'].keys()
    print("Open Ports: ", *open_port)
