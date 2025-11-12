import socket

port_map = {
        20:  "FTP Data",
        21:  "FTP Control",
        22:  "SSH",
        23:  "Telnet",
        25:  "SMTP (Email)",
        53:  "DNS",
        67:  "DHCP Server",
        68:  "DHCP Client",
        69:  "TFTP",
        80:  "HTTP",
        110: "POP3",
        119: "NNTP",
        123: "NTP",
        135: "MS RPC",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service",
        143: "IMAP",
        161: "SNMP",
        162: "SNMP Trap",
        179: "BGP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB / CIFS",
        465: "SMTPS",
        514: "Syslog",
        515: "LPD (Printer)",
        587: "SMTP (Submission)",
        636: "LDAPS",
        993: "IMAPS",
        995: "POP3S",
        1080: "SOCKS Proxy",
        1194: "OpenVPN",
        1433: "Microsoft SQL Server",
        1521: "Oracle DB",
        1723: "PPTP",
        2049: "NFS",
        2181: "Zookeeper",
        2379: "etcd",
        2380: "etcd (Peer)",
        3306: "MySQL",
        3389: "RDP (Remote Desktop)",
        3690: "Subversion",
        4000: "Unreal (Game Server)",
        5000: "UPnP / Flask dev server",
        5432: "PostgreSQL",
        5632: "pcAnywhere",
        5900: "VNC",
        5985: "WinRM (HTTP)",
        5986: "WinRM (HTTPS)",
        6379: "Redis",
        8080: "HTTP-alt / Proxy",
        8443: "HTTPS-alt",
        9000: "SonarQube / PHP-FPM",
        9200: "Elasticsearch",
        11211: "Memcached",
        27017: "MongoDB",
        25565: "Minecraft Server",
}
# Creates a TCP socket with IPV4 addressing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    target = (input("Enter target IP address or domain: "))
    ports = input("Enter port(s) to scan (separate with spaces) or press Enter to scan default ports: ").split()
    
    if ports == []:
        ports = [20, 21, 22, 23 ,25, 53, 80, 110, 143, 443, 3389]
    
    for port in ports:
        name = port_map.get(int(port))

        if name == None:
            name = 'PORT NAME UNKNOWN'
        print(f"Scanning port {port} ({name}) on {target}...")
            
        try:
            s.connect((target, port))
            print(f"Port {port} ({name}) is open on {target}")
        except ConnectionRefusedError:
            print(f"Port {port} ({name}) is closed on {target}")
        except TimeoutError:
            print("Connection timed out, check if this host is reachable.")
        except Exception as e:
            print(e)
    
    loopCheck = input("Do you want to scan another target? (y/n): ")
    if loopCheck.lower() != 'y':
        break
