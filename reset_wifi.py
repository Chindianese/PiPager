import re
import os
import shutil


def reset_wpa():
    dst = "/etc/wpa_supplicant/wpa_supplicant.conf"
    print("copying template wpa to: ", dst)
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    src = os.path.join(__location__, 'wpa_supplicant.conf')
    shutil.copyfile(src, dst)


reset_wpa()