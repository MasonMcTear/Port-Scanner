import  ipaddress
import socket

def port_scrubber(port_string):
    bad_ports = []
    clean_ports = []
    
    if '-' in port_string:
        if port_string.char.isalpha():
            print(f'{port_string} is not a valid port range....')
            bad_ports.append(port_string)
            return clean_ports, bad_ports
        else:
            ports_Min_Max = list(map(int, port_string.split('-')))
            port_string = list(range(ports_Min_Max[0], ports_Min_Max[1]+1))
    elif port_string != '':
        port_string = map(int, port_string.split())
    else:
        clean_ports = [20, 21, 22, 23 ,25, 53, 80, 110, 143, 443, 3389]
        return clean_ports, bad_ports
    
    for port in port_string:
        if port < 0 or port > 65535:
            bad_ports.append(port)
        else:
            clean_ports.append(port)

    if len(bad_ports) > 0:
        print('The following ports are invalid and will not be scanned: ')
        for port in bad_ports:
            print(' -', port)
    return clean_ports, bad_ports

def any_valid_ports(port_string):
    good_ports, bad_ports = port_scrubber(port_string)
    if len(good_ports) == 0 & len(bad_ports) > 0:
        return False, bad_ports
    else:
        return True, good_ports

def valid_target(target):
    target = str(target)
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            socket.gethostbyname(target)
            return socket.gethostbyname(target)
        except:
            return False

    


