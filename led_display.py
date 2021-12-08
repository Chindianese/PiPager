import RPi.GPIO as GPIO


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)


def on():
    print("LED ON")
    GPIO.output(18, True)


def off():
    print("LED OFF")
    GPIO.output(18, False)


def set(trigger):
    if trigger:
        on()
    else:
        off()
