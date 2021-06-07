# Speed Test program of an exec
import time
import nmap

hostname = str(input("[?] Enter hostname : "))
port_range = str(input("[?] Range port (default value is 0-1024) : "))

start = time.perf_counter()
scanner = nmap.PortScanner()
scanner.scan(hostname, port_range)

end = time.perf_counter()
time_elapsed = end - start
print(time_elapsed)
