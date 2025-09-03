import nmap

def ip(host):
    nm = nmap.PortScanner()
    nm.scan(host, '22-443')
    my_host = nm.all_hosts()
    return my_host



def wifi(host):
    nm = nmap.PortScanner()
    nm.scan(host, '22-443')
    my_host = nm.all_hosts()
    return my_host