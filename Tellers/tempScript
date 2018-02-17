import sys
import urllib
import Adafruit_DHT
import RPi.GPIO as GPIO
from Wheel import Wheel
import thread
import time

def init():
    wheelOne = Wheel(6, 19, "Wheel One")
    wheelTen = Wheel(5, 13, "Wheel Ten")
    wheelArray = [wheelOne, wheelTen]
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
        GPIO.output(wheel.output, GPIO.LOW)

def getOnes(number):
    return int(round(number % 10))

def getTens(number):
    return int(round(number // 10))

def update(wheels):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    for wheel in wheels:
        if wheel.wheelName == "Wheel One":
            wheel.setWheel(getOnes(temperature))
        elif wheel.wheelName == "Wheel Ten":
            wheel.setWheel(getTens(temperature))
    sendData(temperature, humidity)

sensor = Adafruit_DHT.AM2302
pin = 12
minute = 60

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

try:
    if humidity is not None and temperature is not None:
        wheels = init()
        while True:
            update(wheels)
            time.sleep(minute * 5)
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "Exiting, GPIO's cleaned up"

