import socket
import subprocess
import os

import os_manager


def get_ip():
    ip_address = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception as e:
        print(e)
    return ip_address


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


def get_connection_name():
    try:
        if os_manager.isRPI:
            print("checking pi wifi")
            data = subprocess.check_output(['sudo', 'iwgetid'])
            print(data)
            wifi = data.decode('utf-8')
            connection_name = wifi.split('"')[1]
            return connection_name
        else:
            print("checking non pi wifi")
            connection_name = ""
            wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
            data = wifi.decode('utf-8')
            split = data[data.find('SSID'):]
            split2 = split[split.find(':')+2:split.find('\r')]
            connection_name = split2
            return connection_name
    except Exception as e:
        print(e)
    return ""


def check_if_on_wifi_name(wifi_name):
    connection_name = get_connection_name()
    if wifi_name == connection_name:
        return True

    return False
