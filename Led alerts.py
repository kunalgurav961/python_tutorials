import time, RPi.GPIO as GPIO, glob

TEMP_SENSOR = glob.glob('/sys/bus/w1/devices/28*')[0] + '/w1_slave'
LED, THRESHOLD = 18, 30.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def get_temp():
    with open(TEMP_SENSOR, 'r') as f:
        return float(f.readlines()[1].split("t=")[1]) / 1000.0

try:
    while True:
        GPIO.output(LED, get_temp() > THRESHOLD)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
