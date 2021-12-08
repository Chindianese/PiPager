#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import sys

sys.path.append('../drivers')
import drivers
from time import sleep
import textwrap


# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()


def debug_lcd():
    # Main body of code
    try:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        display.lcd_display_string("Screen works!", 1)  # Write line of text to first line of display
        display.lcd_display_string("Line 2", 2)  # Write line of text to second line of display
        sleep(2)  # Give time for the message to be read
        display.lcd_display_string("I am a display!",
                                   1)  # Refresh the first line of display with a different message
        sleep(2)  # Give time for the message to be read
        display.lcd_clear()  # Clear the display of any data
        sleep(0.2)  # Give time for the message to be read
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()


def show_on_lcd(full_text):
    if len(full_text) == 0:
        print('text of length 0')
        return
    if full_text.isspace():
        return
    # Main body of code
    # Remember that your sentences can only be 16 characters long!
    print("Writing to display")
    display.lcd_clear()
    # lines = textwrap.wrap(full_text, 16, break_long_words=True)
    lines = full_text.TextWrapper(width=16, break_long_words=False, replace_whitespace=False)
    display.lcd_display_string(lines[0], 1)  # Write line of text to first line of display
    if len(lines) > 1:
        display.lcd_display_string(lines[1], 2)  # Write line of text to second line of display
    # sleep(2)  # Give time for the message to be read


def show_on_lcd_line(text, line_number):
    if len(text) == 0:
        print('text of length 0')
        return
    # Main body of code
    # Remember that your sentences can only be 16 characters long!
    print("Writing to line: ", line_number)
    display.lcd_display_string(text, line_number)  # Write line of text to first line of display
    # sleep(2)  # Give time for the message to be read
