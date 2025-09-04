import nmap

#Dns 
def ip(host):
    nm = nmap.PortScanner()
    ip = nm.scan(host + "/24", arguments="-sO -PE -PA21,23,80,3389")
    return ip


#Dns 
def wifi(host):
    nm = nmap.PortScanner()
    nm.scan(host + "/24", arguments="-sS -O -PE -PA21,23,80,3389")
    decisive = {}

    for red in nm.all_hosts():
    
        if "osmatch" in nm[red]:
    
            for os in nm[red]["osmatch"]:
                if "Android" in os["name"] or "iOS" in os["name"] or "Windows" in os["name"] or "Linux" in os["name"]:
                    decisive["system"] = os['name']
                    break
                    
    if decisive.get("system") is None:
          return "Not found devices"
    else:
          return decisive    
    
    