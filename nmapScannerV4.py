import nmap
import socket
from progress.bar import Bar

# Objects
scanner = nmap.PortScanner()


def host_discovery():
    try:
        # Local IP addr - CIDR
        ip = str(input("Enter the network address : "))
        cidr = str(input("Enter CIDR notation (ex /24) : "))
        host = ip + cidr

        # Progress Bar
        bar_scan = Bar('Scanning : ', max=3)
        for i in range(3):
            scanner.scan(hosts=host, arguments='-F')
            bar_scan.next()
        bar_scan.finish()

    except ValueError:
        print()
        print("Incorrect Value")

    except KeyboardInterrupt:
        print()
        print("You pressed CTRL+C")

    except socket.gaierror:
        print()
        print("Hostname or Ports are not valid")

    # Display
    for host in scanner.all_hosts():
        print(host)


def soft_scan():
    try:
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

        bar_scan = Bar('Scanning : ', max=3)
        #  ! Scan SYN/ACK
        for i in range(3):
            scanner.scan(ip_v4, port_range)
            bar_scan.next()
        bar_scan.finish()

        print("-" * 50)
        # Display without cast (.state() return the state of IP in str)
        ip_status = scanner[ip_v4].state()
        print("[*] Ip Status : ", *ip_status)

        # Display of the used protocol
        protocol_list = scanner[ip_v4].all_protocols()
        print("[*] Protocol : ", *protocol_list)

        # Display of open ports
        open_port = scanner[ip_v4]['tcp'].keys()
        print("[*] Open Ports: ", *open_port)
        print("-" * 50)

    except ValueError:
        print()
        print("Incorrect Value")

    except KeyboardInterrupt:
        print()
        print("You pressed CTRL+C")

    except socket.gaierror:
        print()
        print("Hostname or Ports are not valid")


# Main Program
print("1 - Host Discovery")
print("2 - Soft Port Scanner")

selection = int(input("> "))

if selection == 1:
    print("Host Discovery")
    host_discovery()

elif selection == 2:
    print("Soft Port Scanner")
    soft_scan()

elif selection >= 3:
    print()
    print("No module")
