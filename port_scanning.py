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
def scan_em(ports, target):
    for port in ports:
        name = port_map.get(int(port))
        if name == None:
            name = 'PORT NAME UNKNOWN' 
        print(f"Scanning port {port} ({name}) on {target}...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            print(f"Port {port} ({name}) is open on {target}")
            s.close()
        except ConnectionRefusedError:
                print(f"Port {port} ({name}) is closed on {target}")
                s.close()
        except socket.timeout:
                print(f"Port {port} ({name}) couldn't be reached on {target}")
                s.close()
        except Exception as e:
                print(e)
                s.close()