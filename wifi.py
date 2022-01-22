import re
import os
import shutil

def request_event():
    op = input("Enter\n1 to add wifi. \n2 to reset all connections\nx to exit\n")
    if op == "1":
        request_add_network()
    elif op == "2":
        reset_wpa()
    elif op == "x":
        return 0
    else:
        request_event()
    return 0


def request_add_network():
    ssid = input("Enter SSID(wifi name, case sensitive): ")
    psk = input("Enter wifi password(case sensitive): ")
    add_wifi(ssid, psk)


def add_wifi(ssid, psk):
    filename = "/etc/wpa_supplicant/wpa_supplicant.conf"

    with open(filename, 'r+') as f:
        text = f.read()
        text = re.sub('defaultssid', ssid, text, 1)
        text = re.sub('defaultpassword', psk, text, 1)
        f.seek(0)
        f.write(text)
        f.truncate()
    print('Wifi added')
    print("Type 'sh reboot' restart the device. Disable hotspot AFTER typing 'sudo reboot'")


def reset_wpa():
    dst = "/etc/wpa_supplicant/wpa_supplicant.conf"
    print("copying template wpa to: ", dst)
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    src = os.path.join(__location__, 'wpa_supplicant.conf')
    shutil.copyfile(src, dst)


request_event()
