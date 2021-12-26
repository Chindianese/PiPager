import lcd_display
import time
import led_display
import version_number


def boot_splash():
    print("starting splash")
    bottom_row = ""
    # lcd_display.show_on_lcd_line("   Booting...   ", 1)
    load_index = 0
    dot_index = 0
    for index in range(16):
        if index < len(version_number.version):
            bottom_row += version_number.version[index]
        else:
            bottom_row += "."
        lcd_display.show_on_lcd_line(bottom_row, 2)
        if load_index % 2:
            led_display.on()
            if dot_index % 3 == 0:
                lcd_display.show_on_lcd_line("   Booting-..   ", 1)
            elif dot_index % 3 == 1:
                lcd_display.show_on_lcd_line("   Booting.-.   ", 1)
            elif dot_index % 3 == 2:
                lcd_display.show_on_lcd_line("   Booting..-   ", 1)
            dot_index += 1
        else:
            led_display.off()
        load_index += 1
        time.sleep(0.4)

    led_display.off()
    print("done splash")


def blink_led(dur, rep, init_state):
    trigger = init_state
    for index in range(rep*2):
        led_display.set(trigger)
        trigger = not trigger
        time.sleep(dur)
