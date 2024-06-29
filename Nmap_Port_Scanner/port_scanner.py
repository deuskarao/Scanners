import nmap
import re
import subprocess


cmd = "pip install python-nmap"

p2 = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p2.wait()

if p2.returncode == 0:
    print("\nRequirements | Successful ✔ ")
else:
    print("\nPlease run >> pip install python-nmap")


ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535


open_ports = []

while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    port_range = input("""
    Range of ports you want to scan : <int>-<int>\n
    Enter port range : """)

    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()

for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))

        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"\nPort {port} : {port_status}\n")
    except:
        print(f"Can not scan port {port}")
