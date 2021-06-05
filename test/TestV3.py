"""
Fichier de test pour la progress bar : OK
Affichage propre via cast de list : Ok (80%)
"""
import nmap
from progress.bar import Bar

# IP DE TEST :
# scanme.nmap.org : 45.33.32.156
# 0-1024

Scanner = nmap.PortScanner()

ip_addr = input("Enter IP : ")
port_range = input("Enter a port range (ex : 0-1024) : ")
print()

# Spinner à faire tourner lors du scan : Scanner.scan(ip_addr, port_range, '-sS')

bar = Bar('Processing', max=3)
for i in range(3):
    state = Scanner.scan(ip_addr, port_range, '-sS')
    bar.next()
bar.finish()


print()
print("[+] Scan Information\n")
print("Target : ", ip_addr)
print("Ports Scanned : ", port_range)
print()
# Affichage sans cast (.state() retourne le status de l'adresse IP en une str)
ip_status = Scanner[ip_addr].state()
print("[*] Ip Status : ", ip_status)

# Affichage du protocol utilisé avec * : OK
protocol_list = Scanner[ip_addr].all_protocols()
print("[*] Protocol : ", *protocol_list)

# Affichage avec * : OK
open_port = Scanner[ip_addr]['tcp'].keys()
print("[*] Open Ports: ", *open_port)