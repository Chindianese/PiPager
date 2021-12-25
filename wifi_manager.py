import socket
import subprocess

def get_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    # print(local_ip)
    return local_ip


def get_hostname():
    hostname = socket.gethostname()

    return hostname


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False


def check_if_on_wifi_name(wifi_name):
    wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    data = wifi.decode('utf-8')
    if wifi_name in data:
       return True
    else:
       return False
