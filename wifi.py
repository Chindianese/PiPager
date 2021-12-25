import re
import os


def request_add_network():
    ssid = input("Enter SSID(wifi name, case sensitive): ")
    psk = input("Enter wifi password(case sensitive): ")
    add_wifi(ssid, psk)


def add_wifi(ssid, psk):
    filename = "/etc/wpa_supplicant/wpa_supplicant.conf"

    with open(filename, 'r+') as f:
        text = f.read()
        text = re.sub('defaultssid', ssid, text)
        text = re.sub('defaultpsk', psk, text)
        f.seek(0)
        f.write(text)
        f.truncate()


request_add_network()