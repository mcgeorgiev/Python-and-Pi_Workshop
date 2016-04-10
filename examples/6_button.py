# turns led on when button is pressed
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# we'll use variables to make it clear which pins are which
BUTTON = 11
LED = 12

# pin 11 is setup to accept an input. (using an internal pull down resistor)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
    while True:
        if GPIO.input(BUTTON) == True:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()