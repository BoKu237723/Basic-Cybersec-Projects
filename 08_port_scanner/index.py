import socket
from datetime import datetime

ip = socket.gethostbyname(socket.gethostname())

def port_scan(target):
    try:
        print(f"Scanning the Target: {target}")
        print("Time started:", datetime.now())

        for port in range(20, 300):
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.settimeout(0.5)
            
            # connect_ex returns 0 if successful (port is open)
            result = soc.connect_ex((target, port))
            
            if result == 0:
                print(f"Port {port}: Open")
                
            soc.close()
        
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to the server.")

port_scan(ip)
