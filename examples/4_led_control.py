
import RPi.GPIO as GPIO # imports the RP1.GPIO library and renames it GPIO 
import time # imports the time module

GPIO.setmode(GPIO.BOARD) # refers to the pins as numbers

GPIO.setup(12, GPIO.OUT) # setup pin 12 as an output

GPIO.output(12, GPIO.LOW) # sets it to LOW = 0v

GPIO.output(12, GPIO.HIGH) # sets it to HIGH = 3.3v

time.sleep(2) # waits two seconds

GPIO.cleanup() # resets the pin outputs

