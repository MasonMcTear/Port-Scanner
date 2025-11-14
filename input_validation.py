import  ipaddress
import socket

def validate_ports(ports):
    for port in ports:
        if port < 0 or port > 65535:
            print(f'{port} is not a valid port number....')
            return False
        else:
            continue
    return True

def validate_target(target):
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

    


