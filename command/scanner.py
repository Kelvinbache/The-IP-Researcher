import nmap


#Dns 
def wifi(host):
    nm = nmap.PortScanner()
    nm.scan(host + "/24", arguments="-sS -O -PE -PA21,23,80,3389")
    decisive = {}

    for red in nm.all_hosts():
    
        if "osmatch" in nm[red]:
    
            for os in nm[red]["osmatch"]:
                if "Android" in os["name"] or "iOS" in os["name"] or "Windows" in os["name"] or "Linux" in os["name"]:
                    decisive["System"] = os['name']
                    break
                    
    if decisive.get("System") is None:
          return "Not found devices"
    else:
          return decisive    