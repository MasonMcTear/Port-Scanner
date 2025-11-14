def parse_the_ports(ports_string):
    if '-' in ports_string:
        ports_range = ports_string.split('-')
        ports_mapped = map(int , ports_range)
        ports_Min_Max = list(ports_mapped)
        return list(range(ports_Min_Max[0], ports_Min_Max[1]+1))
    elif ports_string != '':
        ports_mapped = map(int , ports_string.split())
        return list(ports_mapped)
    else:
        return [20, 21, 22, 23 ,25, 53, 80, 110, 143, 443, 3389]