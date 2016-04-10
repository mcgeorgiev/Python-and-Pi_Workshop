# asks user for number of times to flash the led
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)

print('How many times will I flash?')
flash_number = int(input())

# while loop. when flash_number is greater than 0 loop
while flash_number > 0:

    GPIO.output(12, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.2)

# decrease the value of flash_number
    flash_number = flash_number - 1

GPIO.cleanup()