import socket
from port_parsing import parse_the_ports
from port_scanning import scan_em
from input_validation import validate_ports, validate_target

socket.setdefaulttimeout(5)
 
#Start Loop
print("Welcome to McScanner - The Peoples's Port Scanner")
while True:
    
    target = (input("Enter target IP address or domain: "))
    if validate_target(target):
        ports_string = input("Enter list of port(s) (space separated) to scan, a range ex: 2-999, or press Enter to scan default ports: ")
        #Port parsing
        ports = parse_the_ports(ports_string)
        if validate_ports(ports):
            #Scan the ports
            scan_em(ports, target)
    
    loopCheck = input("Do you want to scan another target? (y/n): ")
    if loopCheck.lower() != 'y':
        break
