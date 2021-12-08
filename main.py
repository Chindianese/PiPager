import os

import uid_manager

if __name__ == '__main__':
    print('Starting pager')
    uid = uid_manager.get_uid()
    if uid == "":
        print("set up UID with Pager/init.py")
    else:
        lcd_enabled = False
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
        if lcd_enabled:
            import screen_effects
            import led_display
            led_display.init()
            screen_effects.boot_splash()
        import firestore_manager
        firestore_manager.init_firestore_listener(lcd_enabled)
