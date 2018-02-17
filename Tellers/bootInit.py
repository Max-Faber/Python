import sys
import urllib
import Adafruit_DHT
import RPi.GPIO as GPIO
from Wheel import Wheel

def initGPIO(wheels):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for wheel in wheels:
        GPIO.setup(wheel.output, GPIO.OUT)
        GPIO.setup(wheel.input, GPIO.IN)
        GPIO.output(wheel.output, GPIO.LOW)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

try:
    if humidity is not None and temperature is not None:
        wheelOne = Wheel(4, 19)
        wheelTen = Wheel(5, 13)
        wheelArray = [wheelOne, wheelTen]
        initGPIO(wheelArray)
        wheelTen.initZero()
        GPIO.cleanup()
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
except KeyboardInterrupt:
    GPIO.cleanup()