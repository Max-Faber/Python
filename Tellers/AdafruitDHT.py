import sys
import urllib
import Adafruit_DHT
import RPi.GPIO as GPIO
from Wheel import Wheel
import thread
import time
import math
from astral import Astral

def initWheels():
    wheelTen = Wheel(5, 13, "Wheel Ten", 16, 20)
    wheelOne = Wheel(6, 19, "Wheel One", 16, 20)
    wheelDecimal = Wheel(21, 26, "Wheel Decimal", 16, 20)
    wheelArray = [wheelTen, wheelOne, wheelDecimal]
    initGPIO(wheelArray)
    for wheel in wheelArray:
        print "Initializing " + wheel.wheelName
        wheel.initZero()
        print wheel.wheelName + " is set to Zero\n"
    return wheelArray

def sendData(temperature, humidity):
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    parametersURL = 'http://pa1fp:peertronics@127.0.0.1:8080/json.htm?type=command&param=udevice&idx=7&svalue='
    parametersURL = parametersURL + '{0:.2f}'.format(temperature) + ';' + '{0:.2f}'.format(humidity) + ';0'
    hf = urllib.urlopen(parametersURL)
    print 'Transmitted URL: ' + parametersURL
    print 'Response: ' + hf.read()
    hf.close

def initGPIO(wheels):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for wheel in wheels:
        GPIO.setup(wheel.output, GPIO.OUT)
        GPIO.setup(wheel.input, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(wheel.errorLED1, GPIO.OUT)
        GPIO.setup(wheel.errorLED2, GPIO.OUT)
        GPIO.output(wheel.output, GPIO.LOW)
        GPIO.output(wheel.errorLED1, GPIO.LOW)
        GPIO.output(wheel.errorLED2, GPIO.LOW)

def getOnes(number):
    if number < 0:
        number = number * -1
    return int(number % 10)

def getTens(number):
    if number < 0:
        number = number * -1
    return int(round(number // 10))

def getDecimals(number):
    if number < 0:
        number = number * -1
    frac = math.modf(number)[0]
    return int(round(frac * 10))

def getNumbers(numbers):
    print "Ones: " + str(getOnes(numbers))
    print "Tens: " + str(getTens(numbers))
    print "Fraction: " +str(getDecimals(numbers))

def update(wheels, temperature, humidity):
    for wheel in wheels:
        print "Updating " + wheel.wheelName
        if wheel.wheelName == "Wheel One":
            wheel.setWheel(getOnes(temperature))
        elif wheel.wheelName == "Wheel Ten":
            wheel.setWheel(getTens(temperature))
        elif wheel.wheelName == "Wheel Decimal":
            wheel.setWheel(getDecimals(temperature))
    sendData(temperature, humidity)

def checkFreezing(temperature):
    if(temperature < 0):
        print "Freezing"
        GPIO.output(minus_LED, GPIO.HIGH)
    else:
        print "Not freezing"
        GPIO.output(minus_LED, GPIO.LOW)

sensor = Adafruit_DHT.AM2302
pin = 12
minute = 60
minus_LED = 16
wheel_lights = 20

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

try:
    if humidity is not None and temperature is not None:
        wheels = initWheels()
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            checkFreezing(temperature)
            update(wheels, temperature, humidity)
            time.sleep(minute * 5)
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "Exiting, GPIO's cleaned up"

