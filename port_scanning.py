import socket
from port_data import port_map

def scan_em(ports, target):
    bad_ports = []
    for port in ports:
        name = port_map.get(int(port))
        if name == None:
            name = 'PORT NAME UNKNOWN' 
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            print(f"Port {port} ({name}) is open on {target}")
            s.close()
        except ConnectionRefusedError:
                print(f"Port {port} ({name}) is closed on {target}")
                bad_ports.append(port)
        except socket.timeout:
                print(f"Port {port} ({name}) couldn't be reached on {target}")
                bad_ports.append(port)
        except Exception as e:
                print(e)
                bad_ports.append(port)
    if bad_ports.len() > 0:
          return bad_ports