import socket
import platform

def collect_system_info():
    # Get IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Get OS details
    os_info = platform.system() + " " + platform.release()
    
    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "os_info": os_info
    }
