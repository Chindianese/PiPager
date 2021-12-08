import os

import uid_manager
import threading

global firestore_manager


def boot_screen():
    if lcd_enabled:
        import screen_effects
        import led_display
        led_display.init()
        screen_effects.boot_splash()


def firebase_init():
    global firestore_manager
    import firestore_manager


if __name__ == '__main__':
    print('Starting pager')
    uid = uid_manager.get_uid()
    if uid == "":
        print("set up UID with Pager/init.py")
    else:
        lcd_enabled = False
        print('checking lcd enabled')
        try:
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
            path = os.path.join(__location__, 'lcdenabled')
            with open(path) as f:
                lines = f.readlines()
                lcd_enabled = True
                print('lcd enabled')
        except IOError:
            lcd_enabled = False
            print('lcd disabled')
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
        firestore_manager.init_firestore_listener(lcd_enabled)
