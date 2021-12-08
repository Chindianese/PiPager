import lcd_display
import time


def boot_splash():
    text = ""
    # lcd_display.show_on_lcd_line("   Booting...   ", 1)
    load_index = 0
    dot_index = 0
    for index in range(16):
        text += "."
        lcd_display.show_on_lcd_line(text, 2)
        if load_index % 2:
            if dot_index % 3 == 0:
                lcd_display.show_on_lcd_line("   Booting-..   ", 1)
            elif dot_index % 3 == 1:
                lcd_display.show_on_lcd_line("   Booting.-.   ", 1)
            elif dot_index % 3 == 2:
                lcd_display.show_on_lcd_line("   Booting..-   ", 1)
            dot_index += 1
        load_index += 1
        time.sleep(0.05)
