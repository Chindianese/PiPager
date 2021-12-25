import os

import os_manager
import uid_manager
import threading

import wifi_manager

global firestore_manager
global lcd_display

global lcd_enabled

global default_connection
default_connection = "PagerDefault"


def boot_screen():
    global lcd_enabled
    if lcd_enabled:
        import screen_effects
        import led_display
        led_display.init()
        screen_effects.boot_splash()


def firebase_init():
    global firestore_manager
    import firestore_manager


def import_lcd_display():
    global lcd_display
    import lcd_display


def check_lcd():
    global lcd_enabled
    lcd_enabled = False
    print('checking lcd enabled')
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, 'lcdenabled')
        with open(path) as f:
            lines = f.readlines()
            lcd_enabled = True
            print('lcd enabled')
            import_lcd_display()
            os_manager.isRPI = True
            return True
    except IOError:
        lcd_enabled = False
        print('lcd disabled')
        return False


def boot_firestore():
    t1 = threading.Thread(target=boot_screen)
    t2 = threading.Thread(target=firebase_init)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    global firestore_manager
    global lcd_enabled
    firestore_manager.init_firestore_listener(lcd_enabled)


def check_connection():
    print('checking connection')
    hostname = wifi_manager.get_hostname()
    ip = wifi_manager.get_ip()
    # print("hostname: ", hostname)
    is_connected = wifi_manager.is_connected()
    connection_name = wifi_manager.get_connection_name()
    connected_to_default = False
    global default_connection
    if connection_name.lower() == default_connection.lower():
        print("Connected to default: ", default_connection)
        connected_to_default = True
    else:
        connected_to_default = False
        print("Connected to: ", connection_name)

    print("Connected to internet: ", is_connected)
    print("ip: ", ip)

    if connected_to_default:
        return "DEFAULT"
    # if not is_connected:
        # return "NULL"
    return "CONNECTED"


def check_uid():
    uid = uid_manager.get_uid()
    if uid == "":
        print("set up UID with Pager/init.py")
        return False
    else:
        return True


if __name__ == '__main__':
    print('Starting pager')
    print('checking for update')
    # os.system('git pull origin master')
    check_lcd()
    isConnected = check_connection()
    print("Connection state", isConnected)
    if isConnected == "CONNECTED":
        uidPresent = check_uid()
        if uidPresent:
            boot_firestore()
    elif isConnected == "DEFAULT":
        ip = wifi_manager.get_ip()
        if lcd_enabled:
            lcd_display.show_on_lcd_line("PagerDefault ip", 1)
            lcd_display.show_on_lcd_line(ip,2)
    elif isConnected == "NULL":
        if lcd_enabled:
            lcd_display.show_on_lcd("No internet connection")
