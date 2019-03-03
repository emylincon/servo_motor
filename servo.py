import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

try:
    while True:
        os.system('clear')
        print('Rotating Servo Motor . . .')
        GPIO.output(7,1)
        time.sleep(0.0015)
        GPIO.output(7,0)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
