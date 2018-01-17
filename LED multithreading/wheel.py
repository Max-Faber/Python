import RPi.GPIO as GPIO
import time

class wheel():
	def __init__(self, output, input, interval, wheelName):
		self.output = output
		self.input = input
		self.interval = interval
		self.wheelName = wheelName

	def rotate(self):
		GPIO.output(self.output, GPIO.HIGH)
		time.sleep(self.interval)
		GPIO.output(self.output, GPIO.LOW)
		time.sleep(self.interval)