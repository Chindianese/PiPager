import lcd_display
import os_manager


if os_manager.isRPI:
    lcd_display.show_on_lcd_line("REBOOTING", 1)
    lcd_display.show_on_lcd_line("Approx 1 min", 2)

print("Rebooting")