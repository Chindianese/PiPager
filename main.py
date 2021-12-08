import firestore_manager
import os
import screen_effects

if __name__ == '__main__':
    print('Starting pager')
    lcd_enabled = False
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        path = os.path.join(__location__, 'lcdenabled')
        with open(path ) as f:
            lines = f.readlines()
            lcd_enabled = True
            print('lcd enabled')
    except IOError:
        lcd_enabled = False
        print('lcd disabled')
    if lcd_enabled:
        screen_effects.boot_splash()
    firestore_manager.init_firestore_listener(lcd_enabled)
