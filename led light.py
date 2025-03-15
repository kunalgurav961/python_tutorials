import RPi.GPIO as GPIO
import time

TRIG, ECHO, LED = 23, 24, 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0: start = time.time()
    while GPIO.input(ECHO) == 1: end = time.time()
    return round((end - start) * 17150, 2)

try:
    while True:
        dist = get_distance()
        GPIO.output(LED, dist < 10)
        print(f"Distance: {dist} cm")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
